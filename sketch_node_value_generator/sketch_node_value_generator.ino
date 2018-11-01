static const int nodes[] = {1258, 4568, 7898, 9889};
static const int node_count = 4;
static const int MGE_LEN = 20;


void setup() {
  Serial.begin(9600);
  randomSeed(analogRead(0));

}

void loop() {
  for (int n = 0; n < node_count; n++) {
    delay(2000);
    int randNumber = random(15, 40);
    char tbs[MGE_LEN];
    sprintf(tbs, "{\"%d\": %d}", nodes[n],randNumber);
    Serial.println(tbs);
  }

}
