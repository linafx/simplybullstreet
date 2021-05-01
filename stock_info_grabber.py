import requests
import json

base_url = "https://financialmodelingprep.com/api/v3/company/stock/list"
base_results = requests.get(base_url)
base_json = base_results.json()

company_info = open("company_info", "w")
company_info.write(str(base_json))
company_info.close()
