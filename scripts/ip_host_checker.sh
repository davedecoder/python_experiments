#!/bin/bash

array=( "somedomain.com" )
for i in "${array[@]}"
do
    if host $i | grep "xxx.xxx.xxx.xxx"; then
        echo "ok"
    else
        echo $i "not found"
    fi

done