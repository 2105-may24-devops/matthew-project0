#!/usr/bin/env bash
#this file is for testing project 0
pwd

ex_path=~/matthew-project0-production
test_path=~/project-data


source "$ex_path/venv/bin/activate"

if [[ -d $test_path ]] ; then
	        echo "error dir already exist" > error_logs.txt 
		[[ -d $test_path ]] 2> error_logs.txt && exit 1
	else
		        echo "test passed "
fi

