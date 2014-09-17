import os
import time
import datetime

rmcommand = 'rm -rf /data/usereventlog/*.tar.gz /data/usereventlog/unzip/data/usereventlog/*'
os.system(rmcommand)
todaytime = datetime.date.today()
timestamp_end=str(int(time.mktime(todaytime.timetuple())))+'000'
yesterday = todaytime - datetime.timedelta(days=1)
timestamp_begin = str(int(time.mktime(yesterday.timetuple())))+'000'
unzipfilename = "UserEventLog"+str(yesterday)+".json.en.tar.gz"
filename = "UserEventLog"+str(yesterday)+".json.en"
unzipcommand =  "tar zxvf /data/usereventlog/"+unzipfilename+' -C /data/usereventlog/unzip/'
os.system(unzipcommand);
decryptfilename = "UserEventLog"+str(yesterday)+".json"
decryptcommand = 'openssl smime  -decrypt -in /data/usereventlog/unzip/data/usereventlog/'+filename+' -inkey /data/usereventlog/rsakey0.pem  -out /data/usereventlog/decrypt/'+decryptfilename
os.system(decryptcommand)
mongocommad = 'mongoimport -d UserEventLog -c UserEventLog /data/usereventlog/decrypt/'+decryptfilename
os.system(mongocommad)
scpcommand='scp /data/usereventlog/decrypt/'+decryptfilename+' root@192.168.3.62:/data/usereventlog/decrypt'
os.system(scpcommand)
