#!/bin/bash

python3.9 -m venv venv

source venv/bin/activate

python3 -m pip install -r requirements.txt

python3.9 main.py




