import yaml


def read(filepath):
	file_data = []
	try:
		for f in filepath:
			with open(f.name, "r", encoding='UTF-8') as infile:
				data = yaml.safe_load(f)
				file_data.append(data)

	except FileNotFoundError:
		return []
	except yaml.YAMLError:
		return []

	return file_data
