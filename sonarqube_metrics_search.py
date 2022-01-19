import json , requests, pprint
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

myToken = os.environ.get("TOKEN")
host = os.environ.get("HOST")

api = '/api/metrics/search'
params = '?ps=500'

url = host+api+params
#print(url)

session = requests.Session()
session.auth = myToken, ''

call = getattr(session, 'get')
res = call(url)

binary = res.content
output = json.loads(binary)

for metric in output['metrics']:
	print(metric['key'])

print("Number of metrics:")	
print(len(output['metrics']))