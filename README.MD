⚽ European League Monitor
🚧 Status do Projeto: Em Desenvolvimento (Fase Inicial)

Pipeline de Engenharia de Dados para extração e processamento de estatísticas de futebol europeu e mundial.

📖 Descrição
O European League Monitor é um projeto de Engenharia de Dados focado em consumir dados da API football-data.org.

No seu estágio atual, o projeto realiza a ingestão da camada Bronze (Raw). Ele conecta-se à API para extrair dados brutos sobre as principais competições (Premier League, Champions League, Brasileirão, etc.) e os salva localmente em formato JSON para processamento posterior em Python com Pandas.

🏗️ Arquitetura e Fluxo Atual
No momento, o projeto implementa a primeira etapa de um fluxo ETL em ambiente local:

Ingestão (Extract): O script src/extracts/competitions.py faz chamadas à API autenticadas por token.

Armazenamento Local (Bronze): Os dados são salvos em sua forma original (JSON) na pasta data/bronze/competitions/.

Exploração/Transformação (Work in Progress): O script src/transforms/transform_competitions.py e o arquivo notebook.py iniciam a leitura dos JSONs locais e o achatamento (flattening) das estruturas aninhadas usando pandas.json_normalize.

⚙️ Tecnologias e Ferramentas
Linguagem: Python >= 3.13

Manipulação de Dados: pandas

Requisições HTTP: requests

Gerenciamento de Dependências: Poetry

Variáveis de Ambiente: python-dotenv

Ambiente de Desenvolvimento: Jupyter Notebooks (ipykernel)

📂 Estrutura de Pastas (Atual)
A estrutura reflete os módulos já iniciados:

Plaintext
📦 european-league-monitor
 ┣ 📂 data/
 ┃ ┗ 📂 bronze/
 ┃   ┗ 📂 competitions/       # Arquivos JSON brutos extraídos (Ex: competition-PL.json)
 ┣ 📂 src/
 ┃ ┣ 📂 extracts/             
 ┃ ┃ ┣ 📜 competitions.py     # Script funcional de extração das ligas
 ┃ ┃ ┣ 📜 matches.py          # (A implementar)
 ┃ ┃ ┣ 📜 standings.py        # (A implementar)
 ┃ ┃ ┗ 📜 teams.py            # (A implementar)
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
O script fará o download das competições listadas e criará os arquivos JSON na pasta data/bronze/competitions/.

Bash
poetry run python src/extracts/competitions.py
Teste a transformação inicial:

Bash
poetry run python src/transforms/transform_competitions.py
🗺️ Roadmap e Próximos Passos
Como o projeto está em desenvolvimento, as próximas atualizações incluirão:

[ ] Expansão da Ingestão: Implementar os scripts pendentes (matches.py, teams.py, standings.py) para buscar partidas e classificações.

[ ] Rate Limiting: Adicionar pausas (time.sleep) aos loops de extração para evitar o bloqueio (Erro 429) da API em consultas massivas.

[ ] Camada Silver: Evoluir os scripts de transformação para limpar os dados brutos e salvá-los no formato Parquet.

[ ] Orquestração e Nuvem: (Futuro) Migrar a execução para um orquestrador e o armazenamento para um Data Lake em nuvem.