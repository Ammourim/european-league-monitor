#%%
import os
import requests
from pathlib import Path
from dotenv import load_dotenv
import json
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

load_dotenv()

API_KEY=os.getenv('API_KEY')
URL = 'http://api.football-data.org/v4/competitions/'
headers = { 'X-Auth-Token': API_KEY }

LIGAS = ['PL', 'PD', 'BL1', 'CL', 'FL1', 'SA', 'BSA', 'WC'] 

bronze = Path(__file__) / '..' / '..'/ '..' / 'data' / 'bronze' / 'competitions'
bronze.mkdir(parents=True, exist_ok=True)

print(bronze.resolve())

def extract_league():
    logger.info(f'Extraindo {len(LIGAS)} ligas')
    
    for liga in LIGAS:
        logger.info(f'Extraindo liga: {liga}')
        caminho = bronze / f'competition-{liga}.json'

        try:
            response = requests.get(f'{URL}{liga}', headers=headers, timeout=10)
            response.raise_for_status()
            dados = response.json()

            with open(caminho, 'w', encoding='utf-8') as f:
                json.dump(dados, f, indent=4)

            logger.info(f'Liga {liga} salva com sucesso!')
            
        except requests.HTTPError as e:
            logger.error(f'Erro ao extrair liga {liga}: {e}')
        
        logger.info(f'Extracao finalizada!')

extract_league()