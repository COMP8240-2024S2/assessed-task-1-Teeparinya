import subprocess

#Define the shell command to run Stanford NER
commands = [
    './ner.sh wikipedia.txt > stanford-wikipedia.txt',
    './ner.sh fanwiki.txt > stanford-fanwiki.txt'
]

#To run all commands
for command in commands:
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Successfully executed: {command}")
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {command}. Error: {e}")
