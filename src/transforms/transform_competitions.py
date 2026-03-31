#%%
import pandas as pd
import json
from pathlib import Path
from src.utils.paths import BRONZE_COMPETITIONS
#%%
with open(BRONZE_COMPETITIONS/'', encoding='utf-8') as competitions:
    dados = json.load(competitions)
#%%
df_temporadas = pd.json_normalize(dados['seasons'])
colunas = ['id', 'startDate', 'endDate', 'winner.name', 'winner.tla']
#%%
