FROM python:3.9

ADD main.py . 

CMD ["./installWindows.ps1"]