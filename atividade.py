import argparse
import os
import json
import requests


diretorio = "C:/Users/bruvieira/Desktop/Nova_pasta/Atividade_Github"
nome_arquivo = "atividade.json"
caminho_completo = os.path.join(diretorio, nome_arquivo)

def url(usuario):
    return f"https://api.github.com/users/{usuario}/events"

def salva_json():
    url = url(usuario)

    resposta = requests.get(url)

    if resposta.status_code == 200:
        if os.path.exists(caminho_completo):
            with open("atividade.json", "r", encoding="utf-8") as arquivo:
                json.dumb("atividade.json", )



def main():

    parser = argparse.ArgumentParser(description="Buscador de atividade GitHub")
    parser.add_argument("usuario", type=str,help="Nome de usuario que deseja procurar atividade")

    args = parser.parse_args()






if __name__=="__main__":
    main()




