#!/usr/bin/env python3
# Author ID: jashanpreet_singh

import subprocess

def free_space():
    # Launch the command and capture the output
    p = subprocess.Popen("df -h / | awk '{print $4}'", shell=True, stdout=subprocess.PIPE)
    output = p.communicate()[0]
    return output.decode('utf-8').strip()

if __name__ == '__main__':
    print(free_space())

