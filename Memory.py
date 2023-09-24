import os
import subprocess 

commands = ['date',
            'top -b -n 1 -o +%MEM | head -n 17',
            'cat /proc/meminfo',
            'cat /proc/$(pgrep jerusd)/status',
            'cat /proc/zoneinfo',
            'df -kh `cat /proc/mounts | grep tmpfs | cut -d" " -f2`',
            'date',
            'sleep 30']

while True:
    for cmd in commands:
        os.system(cmd)
	output = subprocess.check_output("top -b -n 1 -o +%MEM | head -n 17", shell=True, text=True)
	jerusd_line = next(line for line in output.splitlines() if 'jerusd.main' in line)
	columns = jerusd_line.split()
	pid_value = columns[0]
	res_value = columns[5].rstrip('g')
	if res_value > 5:
		os.system(f'kill -6 {pid_value}')
	
