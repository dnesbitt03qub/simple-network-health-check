#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import time
import sys

HOSTNAME = "google.com"
SYSTEM_CALL = "ping -c 1 " + HOSTNAME
DEFAULT_LOG_FILE_NAME = 'log'
LOG_EXTENSION = '.csv'
SLEEP_DURATION = 1
HEADER = 'Time,Reachable,Ping\n'

def ping_network(log_file):
    # Loops until interrupted
    while True: 

        host_reachable = False
        ping_time = 0.0
        timestamp = time.time()

        # get network details from `ping`
        try:
            # Get the second line
            response = subprocess.check_output(SYSTEM_CALL, shell=True).decode("utf-8").rstrip().split('\n')[1]
            host_reachable = True
        
            # Split the line
            res_split = response.split()
            
            # Extract the details
            ping_time = float(res_split[7].split('=')[1])
        except:
            pass
        
        print(timestamp, host_reachable, ping_time)
        log_file.write('{},{},{}\n'.format(timestamp, host_reachable, ping_time))
        log_file.flush()
    
        # sleep to avoid using unnessary resources
        time.sleep(SLEEP_DURATION)
        
def print_help():
    print('This program logs out network health.')
    print('The default log name is', str(DEFAULT_LOG_FILE_NAME + LOG_EXTENSION))
    print('Add your name as an argument to change the log name (####.csv where #### is the name given)')
    
    
if __name__ == '__main__':
    # Get the log path
    log_path = DEFAULT_LOG_FILE_NAME
    args = sys.argv[1:]
    if len(args) > 0:
        if args[0] == '-h':
            print_help()
            quit()
        log_path = args[0]
    log_path += LOG_EXTENSION
    
    # Try to open the file - if it doesn't open it is empty and needs a header
    try:
        log_file = open(log_path, 'r')
    except:
        log_file = open(log_path, 'w')
        log_file.write(HEADER)
        
    # Open the log file
    log_file = open(log_path, 'a')
    
    try:
        ping_network(log_file)
    except KeyboardInterrupt:
        pass
    
    log_file.close()