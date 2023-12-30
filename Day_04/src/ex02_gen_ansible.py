import yaml


with open("../materials/todo.yml", "r") as f:
    data = yaml.safe_load(f)

# Create the Ansible playbook
playbook = {
    'name': 'Deploy',
    'hosts': 'host',
    'tasks': []
}

if data['server']['install_packages']:
    playbook['tasks'].append({
        'yum': {
            'name': data['server']['install_packages'],
            'state': 'present'
        },
        'name': 'Install packages'
    })

if data['server']['exploit_files']:
    playbook['tasks'].append({
        'name': 'Copy files',
        'copy': {
            'src': data['server']['exploit_files'],
            'dest': '/path/to/destination'
        }
    })

if data['server']['exploit_files']:
    playbook['tasks'].append({
        'name': 'Run files on a remote server',
        'command': ['python3 /path/to/destination/exploit.py', 'python3 /path/to/destination/consumer.py -e 4815162342,3133780085']
    })


with open('deploy.yml', 'w') as f:
    yaml.dump(playbook, f)
