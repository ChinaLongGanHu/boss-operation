#!/usr/bin/env python
# -*- coding: utf8 -*-

import subprocess
from datetime import datetime
import sys,os,signal

LogFileFormat='%Y%m%d_%H_%M_%S_%f'

if len(sys.argv) < 3:
    print 'usage: stop_java.py [log dir] [main class]'
    sys.exit(1)

logDir = sys.argv[1]
mainClass = sys.argv[2]

logOutDir = logDir + '/' + mainClass

if os.path.exists(logOutDir) == False:
    os.makedirs(logOutDir)
    
for file in os.listdir(logOutDir):
    if file.endswith('.pid'):
        with open (logOutDir + '/' + file, "r") as myfile:
            pid=myfile.read().replace('\n', '')
            try:
                os.kill(int(pid), signal.SIGKILL)
                print 'kill success, pid=' + pid
            except:
                i=1

