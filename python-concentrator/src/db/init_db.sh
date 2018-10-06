#!/bin/bash
export PYTHONPATH=${PYTHONPATH}:../:
python3 create_db.py
python3 initial_values.py
