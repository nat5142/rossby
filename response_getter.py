import requests
import json


output_dir = './responses'
base_path = 'https://api.weather.gov/'
endpoint = 'alerts/active/area/PA'

resp = requests.get(base_path+endpoint, params={})

with open('{}/{}.json'.format(output_dir, endpoint.replace('/', '_').replace(',', '.')), 'w') as jfile:
    jfile.write(json.dumps(resp.json()))
