#!/bin/bash

chr="\""
comma=","
file="agents.txt"
cp $file $file."_backup"
while read -r line
do
 echo "${chr}$line${chr}${comma}"
done <$file > newfile
mv newfile $file