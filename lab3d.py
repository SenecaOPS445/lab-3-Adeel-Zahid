#!/usr/bin/env python3
import subprocess

# Author ID: azahid19

def free_space():
    command = "df -h | grep '/$' | awk '{print $4}'"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, _ = process.communicate()
    
    return output.decode('utf-8').strip()

print(free_space())
