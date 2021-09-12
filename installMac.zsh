#!/usr/bin/env zsh

brew update  

brew install pkg-config xquartz 

brew install sdl2 sdl2_gfx sdl2_image sdl2_mixer sdl2_net sdl2_ttf 

python3 -m venv venv

source venv/bin/activate

pip3 install wheel

pip3 install venvdotapp

venvdotapp

pip3 install -r requirements.txt

pip3 uninstall pygame -y

pip3 install git+https://github.com/nelsonlove/pygame
