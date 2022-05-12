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
import os

# os.environ = um dicionário Python contendo variáveis e seus valores.
# os.getenv(Blá) = função usada para buscar o valor de uma variável específica(Blá).

current_language = os.getenv("LANG", "en_US")[:5]

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "fr_FR":
    msg = "Bonjour, Monde!"

print(msg)

