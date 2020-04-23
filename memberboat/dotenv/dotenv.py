from typing import Union, Dict
from pathlib import Path
import os

__author__ = "Hawken Rives"
__copyright__ = "Copyright (C) 2019  Hawken MacKay Rives"
__license__ = "AGPL"
__version__ = "3.0"


def read(*, filepath: Union[Path, str]) -> Dict:
	args = {}

	try:
		with open(filepath, 'r', encoding='UTF-8') as infile:
			for line in infile:
				line = line.strip()

				if line.startswith('#'):
					continue

				if not line:
					continue

				key, value = line.split('=')
				key = key.strip()
				value = value.strip()

				assert key

				args[key] = value
	except FileNotFoundError:
		return {}

	return args


def load(filepath: Union[Path, str] = './.env') -> None:
	args = read(filepath=filepath)

	for key, value in args.items():
		os.environ[key] = value
