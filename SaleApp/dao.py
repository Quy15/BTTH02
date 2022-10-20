import json
from  SaleApp import app
def load_categories():
    with open (f'{app.root_path}/Data/categories.json', encoding='utf-8') as f:
        return json.load(f)

def load_products():
    with open (f'{app.root_path}/Data/products.json', encoding='utf-8') as f:
        return json.load(f)