import redis
import json
import time
import sys

file_path = sys.argv[1]

r_store = redis.Redis(host='localhost', port=6379, db=0)

with open('generated/' + file_path) as json_string:
	data = json.load(json_string)

	start = time.time() * 1000

	for entity in data:
		r_store.set(entity['id'], json.dumps(entity))

	end = time.time() * 1000

	print('Took {} milliseconds to import {} entities'.format(round(end - start), len(data)))
	print('Import speed yields {} entities per second'.format(len(data) / (end - start) * 1000))
