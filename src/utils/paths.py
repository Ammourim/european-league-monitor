from pathlib import Path

# raiz do projeto
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# camadas
DATA_DIR = BASE_DIR / "data"

BRONZE_DIR = DATA_DIR / "bronze"
SILVER_DIR = DATA_DIR / "silver"

# datasets específicos
#CAMADA BRONZE
BRONZE_COMPETITIONS = BRONZE_DIR / "competitions"
BRONZE_MATCHES = BRONZE_DIR / "matches_by_competition"
BRONZE_SCORERS = BRONZE_DIR / "scorers_by_competition"
BRONZE_STANDINGS = BRONZE_DIR / "standings_by_competition"
BRONZE_TEAMS = BRONZE_DIR / "teams_by_competition"
#CAMADA SILVER
SILVER_COMPETITIONS = SILVER_DIR / "competitions"

#CAMADA GOLD




