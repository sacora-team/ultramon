#!/bin/bash
sudo apt install venv 
sudo apt install pip
python -m venv venv
souce venv/bin/activate
python -m pip install -r requirements.txt
python main.py
