#!/usr/bin/env bash
#this file is for testing project 0


ex_path=~/matthew-project0-production
test_path=~/project-data


source "$ex_path/venv/bin/activate"

if [[ -d $test_path ]] ; then
	         
		echo "error: test failed dir present" > error_logs.txt && exit 1
	else
		echo "test 1: pass "
	
fi

$ex_path/venv/bin/python3 $ex_path/main.py collection.txt 0

if [[ -d $test_path ]] ; then
	echo "Test 2 pass dir created"
else
	echo "error test 2 fail" > error_logs.txt && exit 1
fi

