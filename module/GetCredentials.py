import yaml

with open('credentials.yaml', 'r') as f:
    credentials = yaml.safe_load(f)

API_KEY = credentials["API_KEY"]
BASE_CURRENCY = credentials["BASE_CURRENCY"]

API_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{BASE_CURRENCY}"
HISTORY = "Data\history.json"
CONVERSION_FACTORS = "Data/conversion_data.json"
CURRENCY_DATA = "Data/currency_data.json"