#%%
import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()

API_KEY=os.getenv('API_KEY')
URL = 'http://api.football-data.org/v4/competitions/'
headers = { 'X-Auth-Token': API_KEY }

response = requests.get(f'{URL}/PL', headers=headers)   
response.raise_for_status()
# %%
dados = response.json()
print(dados)
#%%
caminho = os.path.join('..','data', 'bronze', 'Premier-league_bronze.json') 

with open(caminho, 'w', encoding='utf-8') as arquivo:
    json.dump(dados, arquivo)