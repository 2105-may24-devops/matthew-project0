#!/usr/bin/env bash
#this file is for testing project 0


ex_path=~/matthew-project0-production
test_path=~/project-data

#start venv
source "$ex_path/venv/bin/activate"

#test1 make sure /project-data isn't present
if [[ -d $test_path ]] ; then
	         
		echo "error: test failed dir present" > error_logs.txt && exit 1
	else
		echo "test 1: pass "
	
fi
#run non interative program 
$ex_path/venv/bin/python3 $ex_path/main.py collection.txt 0

#test3 check if collection_file.txt is created
if [[ -e "$test_path/collection_file.txt" ]] ; then
	echo "test3: passed file created"
else
	echo "error: test3 failed" >> error_logs.txt && exit 1
fi 

exit 0 

