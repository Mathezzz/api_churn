# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 20:07:00 2024

@author: ander
"""

from flask import Flask, request, jsonify
from joblib import load
import sklearn
import os
import base64

app = Flask(__name__)

# Carregar o modelo salvo
modelo = load('modelos/best_model.pkl')

# Teste de rota para verificar se a API está rodando
@app.route('/')
def home():
    return "API de Previsão de Churn está on"

@app.route('/prever', methods=['POST'])
def prever():
    dados = request.get_json()
    
    # Vamos extrair e formatar os dados para predição
    try:
        dados_entrada = [dados['input']]
    except KeyError:
        return jsonify({"erro": "Chave de dados incorreta. Envie os dados em formato json com a chave 'input' "}), 400
    
    try:
        predicao = modelo.predict(dados_entrada)
    except ValueError as e:
        return jsonify({"erro": "Dados enviados incorretos. Verifique o formato e a quantidade de dados enviados"}), 400
    return jsonify({'predicao': int(predicao[0])})

