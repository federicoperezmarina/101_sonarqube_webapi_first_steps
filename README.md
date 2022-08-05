# 101_sonarqube_webapi_first_steps
This repository explains how to use sonarqube webapi.

We can find here the documentation of the [sonarqube api](https://sonarcloud.io/web_api/)

## Table of Contents (api)
* [Sonarqube project search](#sonarqube-project-search)
* [Sonarqube metrics search](#sonarqube-metrics-search)
* [Sonarqube measure search](#sonarqube-measure-search)
* [Sonarqube measures by project](#sonarqube-measures-by-project)

## Sonarqube project search
Here you can find an example with the code of the api/project/search 
file: [sonarqube_projects_search.py](sonarqube_projects_search.py)

Code:
```python
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
```

How to run the code:
```sh
python sonarqube_projects_search.py
```

## Sonarqube metrics search
Here you can find an example of the api/metrics/search 
file: [sonarqube_metrics_search.py](sonarqube_metrics_search.py)

Code:
```python
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
```

How to execute the code:
```sh
python sonarqube_metrics_search.py
```

Output
```sh
new_technical_debt
blocker_violations
bugs
burned_budget
business_value
classes
code_smells
cognitive_complexity
comment_lines
comment_lines_density
comment_lines_data
class_complexity
file_complexity
function_complexity
complexity_in_classes
complexity_in_functions
branch_coverage
new_branch_coverage
conditions_to_cover
new_conditions_to_cover
confirmed_issues
coverage
new_coverage
critical_violations
complexity
last_commit_date
development_cost
new_development_cost
directories
duplicated_blocks
new_duplicated_blocks
duplicated_files
duplicated_lines
duplicated_lines_density
new_duplicated_lines_density
new_duplicated_lines
duplications_data
effort_to_reach_maintainability_rating_a
executable_lines_data
false_positive_issues
file_complexity_distribution
files
function_complexity_distribution
functions
generated_lines
generated_ncloc
info_violations
violations
line_coverage
new_line_coverage
lines
ncloc
ncloc_language_distribution
lines_to_cover
new_lines_to_cover
sqale_rating
new_maintainability_rating
major_violations
minor_violations
ncloc_data
new_blocker_violations
new_bugs
new_code_smells
new_critical_violations
new_info_violations
new_violations
new_lines
new_major_violations
new_minor_violations
new_vulnerabilities
open_issues
quality_profiles
projects
public_api
public_documented_api_density
public_undocumented_api
quality_gate_details
alert_status
reliability_rating
new_reliability_rating
reliability_remediation_effort
new_reliability_remediation_effort
reopened_issues
security_rating
new_security_rating
security_remediation_effort
new_security_remediation_effort
skipped_tests
sonarjava_feedback
statements
team_size
sqale_index
sqale_debt_ratio
new_sqale_debt_ratio
uncovered_conditions
new_uncovered_conditions
uncovered_lines
new_uncovered_lines
test_execution_time
test_errors
test_failures
test_success_density
tests
vulnerabilities
wont_fix_issues
Number of metrics:
105
```

## Sonarqube measure search
Here you can find an example of the api/measure/search [sonarqube_measure_search.py](sonarqube_measure_search.py)

## Sonarqube measures by project
Here you can find an example more complex using two api api/project/search and api/measure/component [sonarqube_measures_by_project.py](sonarqube_measures_by_project.py)
