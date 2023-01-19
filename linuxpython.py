# How to user linnx Command in python....

from subprocess import check_output

command = 'ls -sSh'
output = check_output(command.split()).decode()
print(output)
