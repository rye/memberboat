import os
import argparse
import pathlib
import attr

from github import Github, GithubIntegration

from memberboat.readfile import read as read_file
from memberboat.dotenv import load as load_dotenv
load_dotenv()

# import http.client

# http.client.HTTPConnection.debuglevel = 1

# Usage
#   memberboat validate -- find and validate configuration files
#   memberboat apply -- apply the configuration
#   - --dry-run -- only check and print what would happen


@attr.s
class User():
	username = attr.ib()
	type = attr.ib()
	year = attr.ib()
	email = attr.ib()
	role = attr.ib()


def get_installation_token(owner, repo, integration_id, private_key):
	integration = GithubIntegration(integration_id=int(integration_id),
	                                private_key=private_key)

	installation = integration.get_installation(owner, repo)

	return integration.get_access_token(installation.id.value).token


def apply(files=[], dry_run=False):
	if dry_run:
		print("(dry run)")


def validate(files=[]):
	print("validating")
	contents = read_file(files)
	print(contents)
	# users_dict = make_dict(contents)
	# print(users_dict)

	# for f in users_dict:

	# 	user = User(u.username, type=u.type, year=u.year, email=u.email, role=u.role)
	# 	print(user)


def main():
	parser = argparse.ArgumentParser(
	    prog='memberboat', description='Synchronize membership with GitHub')

	parser.add_argument('-f',
	                    '--file',
	                    type=argparse.FileType('r'),
	                    required=True,
	                    action='append',
	                    help='the file containing membership information')

	subparsers = parser.add_subparsers(title='subcommands',
	                                   description='valid subcommands',
	                                   dest='subcommand')

	validate_parser = subparsers.add_parser(
	    'validate', help='validate the configuration files')

	apply_parser = subparsers.add_parser('apply',
	                                     help='apply the configuration')
	apply_parser.add_argument('-d',
	                          '--dry-run',
	                          action='store_true',
	                          help='only print what would be done')

	args = parser.parse_args()

	if args.subcommand == 'apply':
		apply(files=args.file, dry_run=args.dry_run)
	else:
		validate(files=args.file)

	token = get_installation_token(
	    os.environ['GITHUB_ORG_NAME'], os.environ['GITHUB_REPO_NAME'],
	    os.environ['GITHUB_APP_ID'],
	    open(os.environ['GITHUB_APP_PRIVATE_KEY_FILE'], 'rb').read().strip())

	g = Github(token)

	print(g.rate_limiting)


if __name__ == "__main__":
	main()
