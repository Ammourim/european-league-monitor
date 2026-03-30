#%%
import pandas as pd
import os
import json
#%%
with open('../../data/bronze/competitions.json', encoding='utf-8') as competitions:
    dados = json.load(competitions)
#%%
df_temporadas = pd.json_normalize(dados['seasons'])
colunas = ['id', 'startDate', 'endDate', 'winner.name', 'winner.tla']
#%%
