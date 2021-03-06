import sqlite3
from collections import deque

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from config.constants import DB_NAME, VALID_NODES

MAX_DATA_LEN = 15

DB_PATH = str(DB_NAME)

app = dash.Dash('vehicle-data')

app.layout = html.Div([
    html.Div([html.H2('Temperature', style={'float': 'left'})]),
    dcc.Dropdown(id='lora-nodes',
                 options=[{'label': v, 'value': k} for k, v in VALID_NODES.items()],
                 value=list(VALID_NODES.keys())[:3],
                 multi=True),
    html.Div(children=html.Div(id='graphs'), className='row'),
    dcc.Interval(id='graph-update', interval=10000),
], className="container", style={'width': '98%', 'margin-left': 10, 'margin-right': 10, 'max-width': 50000})


@app.callback(
    dash.dependencies.Output('graphs', 'children'),
    [dash.dependencies.Input('lora-nodes', 'value')],
    events=[dash.dependencies.Event('graph-update', 'interval')]
)
def update_graph(data_names):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    graphs = []
    if len(data_names) > 2:
        class_choice = 'col s12 m6 l4'
    elif len(data_names) == 2:
        class_choice = 'col s12 m6 l6'
    else:
        class_choice = 'col s12'

    for data_name in data_names:
        temp_values = cursor.execute('''SELECT time_stamp, temperature FROM temperature 
        WHERE node_id == {} ORDER BY time_stamp DESC LIMIT {}'''.format(data_name, MAX_DATA_LEN)).fetchall()
        x_values = deque(maxlen=MAX_DATA_LEN)
        y_values = deque(maxlen=MAX_DATA_LEN)
        for t in temp_values:
            x_values.append(t[0])
            y_values.append(t[1])
        data = go.Scatter(
            x=list(x_values),
            y=list(y_values),
            name='Scatter',
            fill="tozeroy",
            fillcolor="#6897bb"
        )
        if (not x_values) or (not y_values):
            continue

        try:
            layout = go.Layout(xaxis=dict(range=[min(x_values), max(x_values)]),
                               yaxis=dict(range=[min(y_values), max(y_values)]),
                               margin={'l': 50, 'r': 1, 't': 45, 'b': 30},
                               title='{} - {}'.format(data_name, VALID_NODES[data_name][:30]),
                               autosize=True)

            graphs.append(html.Div(dcc.Graph(
                id=data_name,
                animate=True,
                figure={'data': [data], 'layout': layout}
            ), className=class_choice))
        except (ValueError, TypeError, KeyError):
            print("Error adding layout {} to graph.".format(data_name))
    conn.close()
    return graphs


external_css = ["https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/css/materialize.min.css"]
for css in external_css:
    app.css.append_css({"external_url": css})

external_js = ['https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/js/materialize.min.js']
for js in external_css:
    app.scripts.append_script({'external_url': js})

if __name__ == '__main__':
    if not DB_NAME.exists():
        print('No se pudo conectar a la DB')
        exit(1)
    app.run_server(debug=True, host='0.0.0.0')
