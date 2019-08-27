import random
from fabric.contrib.files import append, exists
from fabric.api import cd, env, local, run
from fabric.network import ssh

REPO_URL = 'https://github.com/elihro/obey_testing_goat_superlists.git'
env.hosts = ['superlists-staging.irodevelpment.xyz']
env.user = 'iro'

def _get_latest_source():
	if exists('.git'):
		run('git fetch')
	else:
		run(f'git clone {REPO_URL} .')
	current_commit = local("git log -n 1 --format=%H", capture=True)
	run(f'git reset --hard {current_commit}')
	
def _update_virtualenv():
	if not exists('virtualenv/bin/pip'):
		run(f'python3.6 -m evenv virtualenv')
	run('./virtualenv/bin/pip install -r requeriments.txt')

def deploy():	
	site_folder = f'/home/{env.user}/sites/{env.hosts[0]}'
	run(f'mkdir -p {site_folder}')	
	with cd(site_folder):
		_get_latest_source()
		_update_virtualenv()
	