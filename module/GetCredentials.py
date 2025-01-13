import yaml

with open('CREDENTIALS.yaml', 'r') as f:
    credentials = yaml.safe_load(f)

API_KEY = credentials["API_KEY"]
BASE_CURRENCY = credentials["BASE_CURRENCY"]

API_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{BASE_CURRENCY}"
HISTORY = "Data\history.json"
DATA_DIRECTORY = "Data"
THEME_DIRECTORY = 'resources\Themes'