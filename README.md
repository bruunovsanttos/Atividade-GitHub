# Atividade-GitHub
Neste projeto foi uilizada a [API do Github](https://docs.github.com/en/rest/activity/events?apiVersion=2022-11-28) com base no projeto criado no [Roadmap.sh](https://roadmap.sh/projects/github-user-activity) para verificar as atividades de usuários da rede Github.  

# Requisitos de Projeto
* Busca e exibe eventos recentes de um usuário no GitHub. 📥
* Salva as atividades em um arquivo JSON para consulta offline. 💾
* Lida com erros de maneira elegante (usuários inválidos, falhas de conexão, etc.).✅
* Suporte a múltiplos tipos de eventos 🛠️, como:
  * Pushes (commits enviados).
  * Issues abertas ou comentadas.
  * Estrelas adicionadas a repositórios.

# Ferramentas do Projeto 🔨🔧  
### Linguagem de programação
#### Python 3.12  🐍
### Bibliotecas Utilizadas📚
[Argparse](https://docs.python.org/pt-br/3/library/argparse.html#module-argparse) A utilização dessa biblioteca consiste na manipulação correta dos argumentos dados pelo usuário do programa, sem que ocorram erros.  

[JSON](https://docs.python.org/pt-br/3/library/json.html) Utilizada para a manipulação do arquivo que serve de base para as adições e atualizações de despesas.

[OS](https://docs.python.org/pt-br/3/library/os.html#module-os) Para manipulação de caminhos do programa e controle dos arquivos.

[Requests]()