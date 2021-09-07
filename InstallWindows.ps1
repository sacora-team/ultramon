$Usuario = Read-host -Prompt "Nombre del usuario? "
$Juego = Read-host -Prompt "Carpeta del juego?(estas parado en C:/users/{$Usuario}/) "

cd C:/users/$Usuario/$Juego

git clone https://github.com/sacora-team/ultramon.git

python3 -m ensurepip

python3 -m pip install --upgrade pip

pip3 install virtualenv
