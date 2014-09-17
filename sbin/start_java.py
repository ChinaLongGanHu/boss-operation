#!/usr/bin/env python
# -*- coding: utf8 -*-

import subprocess
from datetime import datetime
import sys,os

LogFileFormat='%Y%m%d_%H_%M_%S_%f'

if len(sys.argv) < 4:
    print 'usage: launch_java.py [program dir] [log dir] [main class] [instance num]'
    sys.exit(1)

programDir = sys.argv[1]
logDir = sys.argv[2]
mainClass = sys.argv[3]

if len(sys.argv) > 4:
    instanceNum = sys.argv[4]
else:
    instanceNum = "1"

logOutDir = logDir + '/' + mainClass
daomonPathBase = logOutDir + '/' + datetime.now().strftime(LogFileFormat)
daemonOutLog = daomonPathBase + '.out'
daomonPid = daomonPathBase + '.pid'

classpath = programDir + "/conf"
        
buildDir = os.getcwd()

for jarFile in os.listdir(programDir+'/lib'):
    if jarFile.endswith('.jar'):
        classpath += ':' + programDir + '/lib/' + jarFile
if os.path.exists(logOutDir) == False:
    os.makedirs(logOutDir)

jvmStartCmd = []
jvmStartCmd.append('java')
jvmStartCmd.append('-server')
jvmStartCmd.append('-Xms256m')
jvmStartCmd.append('-Xmx2048m')
jvmStartCmd.append('-classpath')
jvmStartCmd.append(classpath)
jvmStartCmd.append(mainClass)
jvmStartCmd.append(instanceNum)

outputFile = open(daemonOutLog, 'w+')
pidFile = open(daomonPid, 'w+')
newProc = subprocess.Popen(jvmStartCmd, stdout=outputFile, stderr=outputFile)
pidFile.write(str(newProc.pid))
pidFile.close()
os.chdir(buildDir)

print 'pid:' + str(newProc.pid)


