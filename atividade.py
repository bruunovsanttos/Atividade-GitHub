import argparse
import os
import json
import requests


diretorio = os.getcwd()
nome_arquivo = "atividade.json"
caminho_completo = os.path.join(diretorio, nome_arquivo)

def url_requerida(usuario):
    return f"https://api.github.com/users/{usuario}/events"

def salva_json(usuario):
    url = url_requerida(usuario)
    try:

        resposta = requests.get(url)
        #print(f"Status Code: {resposta.status_code}")
        #print(f"Conteúdo da Resposta: {resposta.text[:200]}")

        if resposta.status_code == 200:
            atividades = resposta.json()
            if atividades:
                with open(caminho_completo, "w", encoding="utf-8") as arquivo:
                    json.dump(resposta.json(), arquivo, ensure_ascii=False, indent=4)
                    print(f"A atividade do usuario {usuario} foi salva arquivo {nome_arquivo}")
            else:
                print(f"Não foi possivel encontrar atividade do usuário {usuario}")

        elif resposta.status_code == 404:
            print(f"Erro: usuário {usuario} não encontrado")
        else:
            print(f"Erro ao buscar atividade do usuário {usuario}. Status code {resposta.status_code}")

    except requests.exceptions.RequestException as erro:
        print(f"Erro de conexão com a API: {erro}")



#aqui esta como funciona corretamente verificar onde esta o erro para atender o codigo de uma forma satisfatoria.

        #resposta = requests.get(url)

        # Exibir a resposta da API para depuração
        #print(f"Status Code: {resposta.status_code}")
        #print(f"Conteúdo Completo da Resposta: {resposta.text}")  # Exibe o conteúdo completo da resposta da API

        #if resposta.status_code == 200:
            # Verifica se há conteúdo na resposta
         #   atividades = resposta.json()
          #  if atividades:
           #     with open(caminho_completo, "w", encoding="utf-8") as arquivo:
            #        json.dump(atividades, arquivo, ensure_ascii=False, indent=4)
             #       print(f"A atividade do usuário {usuario} foi salva com sucesso no arquivo {nome_arquivo}")
            #else:
             #   print(f"O usuário {usuario} não tem atividades recentes.")
        #elif resposta.status_code == 404:
         #   print(f"Erro: Usuário {usuario} não encontrado no GitHub.")
        #else:
         #   print(f"Erro ao buscar a atividade do usuário {usuario}. Status code: {resposta.status_code}")

    #except requests.exceptions.RequestException as e:
     #   print(f"Erro de conexão com a API: {e}")


def exibir_atividade():
    if os.path.exists(caminho_completo):
        with open(caminho_completo, "r", encoding="utf-8") as arquivo:
            atividades = json.load(arquivo)

            if atividades:
                print("\n Atividades Recentes: ")
                for atividade in atividades:
                    tipo = atividade['type']
                    repositorio = atividade['repo']['name']

                    if tipo == 'PushEvent':
                        commits = atividade['payload']['commits']
                        for commit in commits:
                            menssagem = commit['message']
                        print(f"Enviados {len(commits)} Commits feitos no repositório: {repositorio}.\n Menssagem do commit: {menssagem}")

                    elif tipo == 'IssueCommentEvent':
                        issue_acao = atividade['payload']['action']
                        nome = atividade['payload']['issue']['title']
                        print(f"Issue {issue_acao}: {nome} no repositório {repositorio}")

                    elif tipo == 'WatchEvent':
                        print(f"O repositório {repositorio} foi estrelado.")

                    elif tipo == 'ForkEvent':
                        print(f"O repositório {repositorio} foi forkado")

def main():

    parser = argparse.ArgumentParser(description="Buscador de atividade GitHub")
    parser.add_argument("usuario", type=str,help="Nome de usuario que deseja procurar atividade")

    args = parser.parse_args()

    salva_json(args.usuario)
    exibir_atividade()

if __name__=="__main__":
    main()




