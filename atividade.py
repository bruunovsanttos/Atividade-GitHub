import argparse
import urllib
import os
import json

diretorio = "C:/Users/bruvieira/Desktop/Nova_pasta/Atividade_Github"
nome_arquivo = "atividade.json"
caminho_completo = os.path.join(diretorio, nome_arquivo)

def url(usuario):
    return f"https://api.github.com/users/{usuario}/events"

def salva_json():
    if os.path.exists(caminho_completo):
        with open("atividade.json", "r", encoding="utf-8") as arquivo:
            atividade = json.load(arquivo)






