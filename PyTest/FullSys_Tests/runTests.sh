#!/bin/bash

python3 -m /tmp/venv3
source /tmp/venv3/bin/activate

pip install --upgrade pip
pip install -r requirements.txt
pytest --html-report=./report1.html
