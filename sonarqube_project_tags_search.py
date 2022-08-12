import json , requests, pprint
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

myToken = os.environ.get("TOKEN")
host = os.environ.get("HOST")

api = '/api/project_tags/search'
params = '?ps=100'
url = host+api+params

session = requests.Session()
session.auth = myToken, ''

call = getattr(session, 'get')
res = call(url)
print(res.status_code)

binary = res.content
output = json.loads(binary)

print(output)