@echo off
title Quebra Cabeca do Ray
:: Abre em modo app independente limpo sem abas
start msedge --app="%~dp0quebra-cabeca.html" || start chrome --app="%~dp0quebra-cabeca.html" || start "" "%~dp0quebra-cabeca.html"
exit
