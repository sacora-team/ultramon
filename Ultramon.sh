#!/bin/bash

sudo apt install software-properties-common -y

sudo add-apt-repository ppa:deadsnakes/ppa

sudo apt install python3.9 -y

sudo apt install python3.9-venv -y

sudo apt install python3-pip -y

python3.9 -m venv venv

source venv/bin/activate

python3 -m pip install -r requirements.txt

python3.9 main.py



