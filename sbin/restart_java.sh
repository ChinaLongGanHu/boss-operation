#!/bin/bash

if [ $# != 5 ] ; then echo "usage: restart_java.sh [basepath] [servicename] [detailname] [classname] [instancenum]" ; exit 1 ; fi

base=$1
name=$2
detailname=$3
classname=$4
instance=$5

start_sh=start_java
stop_sh=stop_java

basepath=${base}/${name}
detailpath=${basepath}/${detailname}
console_logs_path=${base}/console_logs

mkdir ${detailpath}
mkdir ${console_logs_path}

cd ${basepath}
rm -rf ${detailname}
tar -xf ${detailname}.tar
${stop_sh} ${console_logs_path} ${classname}
cd ${console_logs_path}/${classname}
rm -rf *
${start_sh} ${detailpath} ${console_logs_path} ${classname} ${instance}