import subprocess

# Run the 'date' command
p = subprocess.Popen(['date'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

# Capture the output
output = p.communicate()

# Print the raw output
print(output)  # This prints a tuple of (stdout, stderr)
print(output[0])  # Output in bytes

# Decode and print the standard output
stdout = output[0].decode('utf-8').strip()
print(stdout)
