#! /bin/bash

counter=1

while [ $counter -le 601 ]
do
	echo ********************************************
	curl -v --silent "https://api.datadoghq.com/api/v2/metrics/zstallDelete.metric/all-tags" -H "Accept: application/json" -H "DD-API-KEY: <PUT KEY HERE" -H "DD-APPLICATION-KEY: <PUT KEY HERE" --stderr - | grep 'x-rate'
	echo ********************************************

done

echo ALL DONE
