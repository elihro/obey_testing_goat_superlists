import random
from fabric.contrib.files import append, exists
from fabric.api import cd, env, local, run

REPO_URL = 'https://github.com/elihro/obey_testing_goat_superlists.git'
env.user = 'iro'
env.host = 'hola'

def deploy():
	site_folder = f'/home/{env.user}/sites/{env.host}'
	run(f'mkdir -p {site_folder}')