import os
import time
import datetime

rmzipcommand='rm -rf /data/usereventlog/zipfile/*'
os.system(rmzipcommand)
todaytime = datetime.date.today()
timestamp_end=str(int(time.mktime(todaytime.timetuple())))+'000'
yesterday = todaytime - datetime.timedelta(days=1)
timestamp_begin = str(int(time.mktime(yesterday.timetuple())))+'000'
filename = "UserEventLog"+str(yesterday)+".json"
command_export_mongo = 'mongoexport --port 27001 --host mongo2 -d UserEventLog -c UserEventLog -q \'{"_ct":{"$gte":'+str(timestamp_begin)+',"$lte":'+str(timestamp_end)+'}}\' --out /data/usereventlog/'+filename
os.system(command_export_mongo)
exprotfilename = filename+".en"
encryptcommad = 'openssl smime -encrypt -in /data/usereventlog/'+filename+' -out /data/usereventlog/'+exprotfilename +' /data/usereventlog/mycert-rsa.pem'
os.system(encryptcommad)
exprotfilenamezip = exprotfilename+'.tar.gz'
zipcommand = 'tar -zcvf /data/usereventlog/zipfile/'+exprotfilenamezip+' /data/usereventlog/'+exprotfilename;
os.system(zipcommand)
rmcommand = 'rm -rf /data/usereventlog/'+filename+' /data/usereventlog/'+exprotfilename;
os.system(rmcommand)
