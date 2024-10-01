import os
# Capture the return value of 'ls'
ls_return = os.system('ls')
print('The contents of ls_return:', ls_return)

# Capture the return value of 'whoami'
whoami_return = os.system('whoami')
print('The contents of whoami_return:', whoami_return)

# Capture the return value of 'ifconfig'
ifconfig_return = os.system('ifconfig')
print('The contents of ifconfig_return:', ifconfig_return)
