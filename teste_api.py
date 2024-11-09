# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 20:24:01 2024

@author: ander
"""

import requests

# URL da API
url = 'http://127.0.0.1:5000/prever'

# Dados de entrada
dados_entrada = [25, 14, 4, 27, 598, False, False, False, True, False]
dados = {"input": dados_entrada}

# Fazer a requisição POST
response = requests.post(url, json=dados)

# Exibir o resultado
print(response.json())
