import json , requests, pprint
import os
from os.path import join, dirname
from dotenv import load_dotenv
import pymongo
import datetime
from random import randint
from time import sleep

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

myclient = pymongo.MongoClient(os.environ.get("MONGODB_SERVER"))
mydb = myclient[os.environ.get("MONGODB_DATABASE")]
mycollection = mydb[os.environ.get("MONGODB_COLLECTION")]

myToken = os.environ.get("TOKEN")
host = os.environ.get("HOST")

now = datetime.datetime.now()

api = '/api/projects/search'
params = '?ps=500'
url = host+api+params

session = requests.Session()
session.auth = myToken, ''

call = getattr(session, 'get')
res = call(url)
print(res.status_code)

binary = res.content
output = json.loads(binary)

for project in output['components']:

	api = '/api/measures/component'
	metrics = '?metricKeys=alert_status,bugs,reliability_rating,vulnerabilities,security_rating,code_smells,sqale_rating,duplicated_lines_density,coverage,ncloc,ncloc_language_distribution'

	component = '&component='+project['key']

	url = host+api+metrics+component
	print(url)

	res = call(url)
	#print(res.content)
	sleep(randint(1,2))

	binary = res.content
	output = json.loads(binary)
	output["date"] = now.strftime("%Y-%m-%d")
	output["url"] = url
	output["name"] = output["component"]["name"]
	output["key"] = output["component"]["key"]

	mycollection.update_one({'component.key':output['component']['key'],"date":now.strftime("%Y-%m-%d")},{'$set':output},upsert=True)
	for metric in output['component']['measures']:
		print(metric)
