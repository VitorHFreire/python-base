#!/usr/bin/env python3

""" Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente o programa exibe a
correspondende.

Como usar:

Tenha a variável LANG devidamente configurada, ex:

    export LANG=pt_BR

Execução:

    python3 arquivo.py

"""

current_language = "en_US"

msg = "Hello, World"

if current_language == "pt_BR":
    "Olá, Mundo"

print(msg)

