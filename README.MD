⚽ European League Monitor
🚧 Status do Projeto: Em Desenvolvimento (Fase Inicial)

Pipeline de Engenharia de Dados para extração e processamento de estatísticas de futebol europeu e mundial.

📖 Descrição
O European League Monitor é um projeto de Engenharia de Dados focado em consumir dados da API football-data.org.

No seu estágio atual, o projeto realiza a ingestão da camada Bronze (Raw). Ele conecta-se à API para extrair dados brutos sobre as principais competições (Premier League, Champions League, Brasileirão, etc.), seus respectivos times e histórico de partidas, salvando-os localmente em formato JSON para processamento posterior em Python com Pandas.

🏗️ Arquitetura e Fluxo Atual
No momento, o projeto implementa a primeira etapa de um fluxo ETL em ambiente local:

Ingestão (Extract): Os scripts no diretório src/extracts/ fazem chamadas à API autenticadas por token. O limite de requisições da API (Rate Limiting) já está sendo tratado com pausas (time.sleep) entre as chamadas.

Armazenamento Local (Bronze): Os dados são salvos em sua forma original (JSON) separados por domínio nas pastas data/bronze/competitions/, data/bronze/matches/ e data/bronze/teams/.

Exploração/Transformação (Work in Progress): O script src/transforms/transform_competitions.py e o arquivo notebook.py iniciam a leitura dos JSONs locais e o achatamento (flattening) das estruturas aninhadas usando pandas.json_normalize.

⚙️ Tecnologias e Ferramentas
Linguagem: Python >= 3.13

Manipulação de Dados: pandas

Requisições HTTP: requests

Gerenciamento de Dependências: Poetry

Variáveis de Ambiente: python-dotenv

Ambiente de Desenvolvimento: Jupyter Notebooks (ipykernel)

📂 Estrutura de Pastas (Atual)
A estrutura reflete os módulos já iniciados e a separação dos dados na camada bronze:

Plaintext
📦 european-league-monitor
 ┣ 📂 data/
 ┃ ┗ 📂 bronze/
 ┃   ┣ 📂 competitions/       # Arquivos JSON brutos extraídos (Ex: competition-PL.json)
 ┃   ┣ 📂 matches/            # Arquivos JSON brutos de partidas
 ┃   ┗ 📂 teams/              # Arquivos JSON brutos de times
 ┣ 📂 src/
 ┃ ┣ 📂 extracts/             
 ┃ ┃ ┣ 📜 competitions.py             # Script de extração das ligas
 ┃ ┃ ┣ 📜 matches_by_competition.py   # Script de extração de partidas
 ┃ ┃ ┣ 📜 teams_by_competition.py     # Script de extração de times
 ┃ ┃ ┣ 📜 scorers_by_competition.py   # (A implementar)
 ┃ ┃ ┗ 📜 standings_by_competition.py # (A implementar)
 ┃ ┗ 📂 transforms/           
 ┃   ┗ 📜 transform_competitions.py # Script inicial de transformação com Pandas
 ┣ 📜 .env.example            # Template de chaves da API
 ┣ 📜 .gitignore              # Ignora dados locais e credenciais
 ┣ 📜 notebook.py             # Rascunho para análises exploratórias
 ┣ 📜 poetry.lock             # Lock de versões
 ┗ 📜 pyproject.toml          # Configurações do Poetry
🚀 Como Executar o Projeto (Estágio Atual)
Pré-requisitos
Python 3.13+ instalado.

Poetry instalado.

Chave de API gerada no site football-data.org.

Passo a passo
Clone o repositório:

Bash
git clone https://github.com/seu-usuario/european-league-monitor.git
cd european-league-monitor
Instale as dependências usando o Poetry:

Bash
poetry install
Configure o ambiente:
Crie um arquivo .env na raiz do projeto baseado no exemplo (se houver) ou adicione:

Snippet de código
API_KEY=sua_chave_de_api_aqui
Execute a ingestão da camada Bronze:
Os scripts farão o download dos dados e os organizarão nas respectivas pastas dentro de data/bronze/.

Bash
poetry run python src/extracts/competitions.py
poetry run python src/extracts/teams_by_competition.py
poetry run python src/extracts/matches_by_competition.py
Teste a transformação inicial:

Bash
poetry run python src/transforms/transform_competitions.py
🗺️ Roadmap e Próximos Passos
Como o projeto está em desenvolvimento, as próximas atualizações incluirão:

[x] Tratamento de Rate Limit: Adicionadas pausas (time.sleep) aos loops de extração para evitar o bloqueio (Erro 429) da API.

[ ] Expansão da Ingestão: Implementar os scripts pendentes para buscar artilheiros (scorers_by_competition.py) e classificações (standings_by_competition.py).

[ ] Camada Silver: Evoluir os scripts de transformação para limpar os dados brutos de todas as entidades (matches, teams, etc) e salvá-los no formato Parquet.

[ ] Orquestração e Nuvem: (Futuro) Migrar a execução para um orquestrador e o armazenamento para um Data Lake em nuvem.