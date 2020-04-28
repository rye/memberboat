def read(filepath):
	file_data = []
	try:
		for f in filepath:
			with open(f.name, "r", encoding='UTF-8') as infile:
				data = infile.read()
				file_data.append(data)

	except FileNotFoundError:
		return []

	return file_data


def make_dict(file_data):
	array_of_dicts = []

	for data in file_data:
		my_dict = {}
		line_data = data.split('\n')

		for line in line_data:
			if line.startswith('#'):
				continue

			if line == '---':
				continue

			if line.startswith('- '):
				line = line[1:]

			if line.startswith('users:'):
				continue

			if not line:
				continue

			key, value = line.split(':')
			key = key.strip()
			value = value.strip()

			assert key

			my_dict[key] = value

		array_of_dicts.append(my_dict)

	return array_of_dicts
