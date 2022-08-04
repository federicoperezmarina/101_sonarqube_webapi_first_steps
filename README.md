# 101_sonarqube_webapi_first_steps
This repository explains how to use sonarqube webapi.

We can find here the documentation of the [sonarqube api](https://sonarcloud.io/web_api/)

## Table of Contents (api)
* [Sonarqube project search](#sonarqube-project-search)
* [Sonarqube metrics search](#sonarqube-metrics-search)
* [Sonarqube measure search](#sonarqube-measure-search)
* [Sonarqube measures by project](#sonarqube-measures-by-project)

## Sonarqube project search
Here you can find an example of the api/project/search [sonarqube_projects_search.py](sonarqube_projects_search.py)

'''python
import json , requests, pprint
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

myToken = os.environ.get("TOKEN")
host = os.environ.get("HOST")

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
	print(project)

'''

## Sonarqube metrics search
Here you can find an example of the api/metrics/search [sonarqube_metrics_search.py](sonarqube_metrics_search.py)

## Sonarqube measure search
Here you can find an example of the api/measure/search [sonarqube_measure_search.py](sonarqube_measure_search.py)

## Sonarqube measures by project
Here you can find an example more complex using two api api/project/search and api/measure/component [sonarqube_measures_by_project.py](sonarqube_measures_by_project.py)
