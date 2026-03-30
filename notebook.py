#%%
import pandas as pd
import os 
import json
#%%
with open('data/bronze/areas.json', encoding='utf-8') as PL:
    dados = json.load(PL)
dados
#%%
df_areas = pd.json_normalize(dados['areas'])
#%%
df_areas['parentArea'].unique()
#%%
df_europa = df_areas[df_areas['parentArea'] == 'Europe']
df_europa
# %%
df_paises = df_europa[df_europa['']]