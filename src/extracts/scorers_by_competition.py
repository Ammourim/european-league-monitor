#%%
import os
import requests
from pathlib import Path
from dotenv import load_dotenv
import json
import logging
import time
from src.utils.paths import BRONZE_SCORERS



logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

load_dotenv()

LIGAS = ['PL', 'PD', 'BL1', 'CL', 'FL1', 'SA', 'BSA', 'WC'] 

API_KEY=os.getenv('API_KEY')
headers = { 'X-Auth-Token': API_KEY }


bronze = BRONZE_SCORERS
bronze.mkdir(parents=True, exist_ok=True)


def extract_scorers():
    logger.info(f'Extraindo scorers de {len(LIGAS)} ligas!')
    
    for liga in LIGAS:
        logger.info(f'Extraindo scorers da liga: {liga}')
        URL = f'http://api.football-data.org/v4/competitions/{liga}/scorers'
        caminho = bronze / f'scorers-{liga}.json'

        try:
            response = requests.get(f'{URL}', headers=headers, timeout=10)
            response.raise_for_status()
            dados = response.json()

            with open(caminho, 'w', encoding='utf-8') as f:
                json.dump(dados, f, indent=4)

            logger.info(f'scorers da liga {liga} salvos com sucesso!')
            
        except requests.HTTPError as e:
            logger.error(f'Erro ao extrair scorers da liga {liga}: {e}')
        time.sleep(2)
        logger.info(f'Extracao finalizada!')

extract_scorers()