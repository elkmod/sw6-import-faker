import redis
import json
import time
import sys

file_path = sys.argv[1]

r_store = redis.Redis(host='localhost', port=6379, db=0)

with open('generated/' + file_path) as json_string:
	data = json.load(json_string)

	entity_dict = {}

	for i in range(0, len(data)):
		entity_dict[data[i]['id']] = json.dumps(data[i])
	
	start = time.time() * 1000

	r_store.mset(entity_dict)

	end = time.time() * 1000

	print('Took {} milliseconds to import {} entities using mset'.format(round(end - start), len(data)))
	print('Import speed yields {} entities per second'.format(len(data) / (end - start) * 1000))