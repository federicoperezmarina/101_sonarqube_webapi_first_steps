import json , requests, pprint
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

myToken = os.environ.get("TOKEN")
host = os.environ.get("HOST")

api = '/api/measures/search'
metrics = '?metricKeys=alert_status,bugs,reliability_rating,vulnerabilities,security_rating,code_smells,sqale_rating,duplicated_lines_density,coverage,ncloc,ncloc_language_distribution'

#projects separated by coma
projects = '&projectKeys='+'XXXXX' 

url = host+api+metrics+projects
#print(url)

session = requests.Session()
session.auth = myToken, ''

call = getattr(session, 'get')
res = call(url)

binary = res.content
output = json.loads(binary)

for metric in output['measures']:
	print(metric)