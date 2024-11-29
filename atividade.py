import argparse
import os
import json
import requests


diretorio = "C:/Users/bruvieira/Desktop/Nova_pasta/Atividade_Github"
nome_arquivo = "atividade.json"
caminho_completo = os.path.join(diretorio, nome_arquivo)

def url_requerida(usuario):
    return f"https://api.github.com/users/{usuario}/events"

def salva_json(usuario):
    url = url_requerida(usuario)
    try:

        resposta = requests.get(url)

        if resposta.status_code == 200:
            if os.path.exists(caminho_completo):
                with open(caminho_completo, "w", encoding="utf-8") as arquivo:
                    json.dump(resposta.json(), arquivo, ensure_ascii=False, indent=4)
                    print(f"A atividade do usuario {usuario} foi salva com sucesso no arquivo {nome_arquivo}")
            else:
                print(f"Não foi possivel encontrar atividade do usuário {usuario}")

        elif resposta.status_code == 404:
            print(f"Erro: usuário {usuario} não encontrado")
        else:
            print(f"Erro ao buscar atividade do usuário {usuario}. Status code {resposta.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão com a API: {e}")


def exibir_atividade():
    if os.path.exists(caminho_completo):
        with open(caminho_completo, "r", encoding="utf-8") as arquivo:
            atividades = json.load(arquivo)

            if atividades:
                for atividade in atividades:
                    tipo = atividade.get('type')
                    repo = atividade['repo']['name']

                    if tipo == 'PushEvent':
                        print(f"Commits feitos no {repo}")


def main():

    parser = argparse.ArgumentParser(description="Buscador de atividade GitHub")
    parser.add_argument("usuario", type=str,help="Nome de usuario que deseja procurar atividade")

    args = parser.parse_args()

    salva_json(args.usuario)
    exibir_atividade()

if __name__=="__main__":
    main()




