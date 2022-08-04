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
	port=9200
)
#resp = es.info()
#print(resp)

index = os.environ.get("ELASTIC_INDEX")


#doc_id = "076efd88-5746-4b5f-9046-081c73af1c4c"
#result = es.delete(index=index, id=doc_id)
result = es.delete_by_query(index=index, body={"query": {"match_all": {}}})

print(result)

