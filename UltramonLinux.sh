#!/bin/bash

<<<<<<< HEAD
=======
source InstaladorLinux.sh

cd /home/$varname/$carpetaDelJuego/ultramon/

>>>>>>> e2d11495bde8704504385d269b132a6f7af83179
python3.9 -m venv venv

source venv/bin/activate

python3 -m pip install -r requirements.txt

python3.9 main.py




