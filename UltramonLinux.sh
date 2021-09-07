#!/bin/bash


echo Cual es el user de este dispositivo?

read varname

echo Donde Estaba la carpeta del juego?

read carpetaDelJuego

cd /home/$varname/$carpetaDelJuego/ultramon/

python3.9 -m venv venv

source venv/bin/activate

python3 -m pip install -r requirements.txt

python3.9 main.py




