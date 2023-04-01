import datetime
import json


def replace_json_field(data: dict, field: str) -> None:
	if isinstance(data, dict):
		for key, value in data.items():
			if key == field:
				data[key] = str(datetime.datetime.now())
			replace_json_field(value, field)
	elif isinstance(data, list):
		for item in data:
			replace_json_field(item, field)


with open('example.json', 'r') as raw_file, open('output.json', 'w') as file:
	obj = json.load(raw_file)
	replace_json_field(obj, 'updated')
	json.dump(obj, file, indent=2)
