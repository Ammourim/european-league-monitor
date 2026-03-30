#%%
import requests
import os
from dotenv import load_dotenv
import json
import time

load_dotenv()

API_KEY=os.getenv('API_KEY')
URL = 'http://api.football-data.org/v4/competitions/'
headers = { 'X-Auth-Token': API_KEY }

LIGA = ['PL', 'PD', 'BL1', 'CL', 'FL1', 'SA', 'BSA', 'WC'] 

for i in LIGA:
    caminho = os.path.join('..','..','data', 'bronze', f'competition-{i}.json')
    response = requests.get(f'{URL}{i}', headers=headers)
    response.raise_for_status()
    dados = response.json()
    with open(caminho, 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo)