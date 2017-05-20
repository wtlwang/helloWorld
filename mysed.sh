#!/bin/bash
ls $1 |while read myline
do
home=$1"/"
sed -i "s/host='[0-9]*\.[0-9\.]*'/host='222.20.94.67'/g" ${home}${myline}
  #cat two strings
done



