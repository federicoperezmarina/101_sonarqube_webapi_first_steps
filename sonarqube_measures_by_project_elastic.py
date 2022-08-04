import json
import requests
import os
from os.path import join, dirname
from dotenv import load_dotenv
from elasticsearch import Elasticsearch
import datetime
import uuid
from random import randint
from time import sleep


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

#es = Elasticsearch(["localhost"],port=9200)
es = Elasticsearch(
	[
		os.environ.get("ELASTIC_HOST_1"),
		os.environ.get("ELASTIC_HOST_2"),
		os.environ.get("ELASTIC_HOST_3"),
		os.environ.get("ELASTIC_HOST_4"),
		os.environ.get("ELASTIC_HOST_5"),
	],
	http_auth=(os.environ.get("ELASTIC_USER"),os.environ.get("ELASTIC_PASSWORD")),
	port=os.environ.get("ELASTIC_PORT")
)
#resp = es.info()
#print(resp)
#exit()

index = os.environ.get("ELASTIC_INDEX")

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
	metrics = '''?metricKeys=alert_status,bugs,reliability_rating,vulnerabilities,security_rating,code_smells,sqale_rating,duplicated_lines_density,coverage,ncloc,ncloc_language_distribution'''
	#metrics = 'new_technical_debt,blocker_violations,bugs,burned_budget,business_value,classes,code_smells,cognitive_complexity,comment_lines,comment_lines_density,comment_lines_data,class_complexity,file_complexity,function_complexity,complexity_in_classes,complexity_in_functions,branch_coverage,new_branch_coverage,conditions_to_cover,new_conditions_to_cover,confirmed_issues,coverage,new_coverage,critical_violations,complexity,last_commit_date,development_cost,new_development_cost,directories,duplicated_blocks,new_duplicated_blocks,duplicated_files,duplicated_lines,duplicated_lines_density,new_duplicated_lines_density,new_duplicated_lines,duplications_data,effort_to_reach_maintainability_rating_a,executable_lines_data,false_positive_issues,file_complexity_distribution,files,function_complexity_distribution,functions,generated_lines,generated_ncloc,info_violations,violations,line_coverage,new_line_coverage,lines,ncloc,ncloc_language_distribution,lines_to_cover,new_lines_to_cover,sqale_rating,new_maintainability_rating,major_violations,minor_violations,ncloc_data,new_blocker_violations,new_bugs,new_code_smells,new_critical_violations,new_info_violations,new_violations,new_lines,new_major_violations,new_minor_violations,new_vulnerabilities,open_issues,quality_profiles,projects,public_api,public_documented_api_density,public_undocumented_api,quality_gate_details,alert_status,reliability_rating,new_reliability_rating,reliability_remediation_effort,new_reliability_remediation_effort,reopened_issues,security_rating,new_security_rating,security_remediation_effort,new_security_remediation_effort,skipped_tests,sonarjava_feedback,statements,team_size,sqale_index,sqale_debt_ratio,new_sqale_debt_ratio,uncovered_conditions,new_uncovered_conditions,uncovered_lines,new_uncovered_lines,test_execution_time,test_errors,test_failures,test_success_density,tests,vulnerabilities,wont_fix_issues'
	component = '&component='+project['key']

	url = host+api+metrics+component
	print(url)

	res = call(url)
	#print(res.content)
	sleep(randint(1,2))

	binary = res.content
	output = json.loads(binary)
	elastic_info = {}
	elastic_info["date"] = now.strftime("%Y-%m-%d")
	
	elastic_info["name"] = output["component"]["name"]
	elastic_info["key"] = output["component"]["key"]
	elastic_info["qualifier"] = output["component"]["qualifier"]

	for metric in output['component']['measures']:
		print(metric)
		elastic_info[metric['metric']] = metric['value']

	elastic_info["url"] = url
	print(elastic_info)

	doc_id = uuid.uuid4()
	es.index(index=index, id=doc_id, document=elastic_info)

	print("Indexed document to index \"" + index + "\" with id " + str(doc_id))
	result = es.get(index=index, id=doc_id)
	print(result)

	#exit()