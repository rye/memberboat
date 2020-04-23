"""
Copyright (C) 2019  Hawken MacKay Rives
https://github.com/degreepath/auditor

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from typing import Union, Dict
from pathlib import Path
import os


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
