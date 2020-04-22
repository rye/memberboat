import os
import argparse

from github import Github, GithubIntegration

# import http.client

# http.client.HTTPConnection.debuglevel = 1

# Usage
#   memberboat validate -- find and validate configuration files
#   memberboat apply -- apply the configuration
#   - --dry-run -- only check and print what would happen


def get_installation_token(owner, repo):
	integration_id = os.environ['GITHUB_APP_ID']
	private_key_file = os.environ['GITHUB_APP_PRIVATE_KEY_FILE']

	with open(private_key_file, "r") as file:
		private_key = file.read().strip().encode()

		integration = GithubIntegration(integration_id=int(integration_id),
		                                private_key=private_key)

		installation = integration.get_installation(owner, repo)

		return integration.get_access_token(installation.id.value).token


def main():
	parser = argparse.ArgumentParser(
	    prog='memberboat', description='Synchronize membership with GitHub')

	parser.add_argument('-f',
	                    '--file',
	                    type=argparse.FileType('r'),
	                    required=True,
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

	token = get_installation_token(os.environ['GITHUB_ORG_NAME'],
	                               os.environ['GITHUB_REPO_NAME'])

	g = Github(token)

	print(g.rate_limiting)


if __name__ == "__main__":
	main()
