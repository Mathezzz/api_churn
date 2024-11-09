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
    dados_entrada = [dados['input']]
    predicao = modelo.predict(dados_entrada)
    return jsonify({'predicao': int(predicao[0])})

@app.route('/upload', methods=['POST'])
def upload_image():
    # Verifica se os dados em Base64 foram incluídos na requisição
    data = request.json
    # print(data)
    
    if not data or 'imagem' not in data:
        return jsonify({"error": "Dados incompletos: 'imagem' é obrigatório"})
    
    # Extrai a imagem em Base64
    file_base64 = data['imagem']
    print(file_base64)
    
    # Ajusta o padding da string Base64, se necessário
    missing_padding = len(file_base64) % 4
    if missing_padding != 0:
        file_base64 += '=' * (4 - missing_padding)
    # Define o nome do arquivo (pode usar um padrão ou gerar automaticamente)
    filename = "imagem_recebida.jpg"  # ou use uma função para gerar nomes únicos
    
    # Converte de Base64 para bytes
    try:
        file_data = base64.b64decode(file_base64)
    except (base64.binascii.Error, ValueError) as e:
        print(e)
        return jsonify({"error": "Base64 inválido"})
    
    return jsonify({"filename": filename})
