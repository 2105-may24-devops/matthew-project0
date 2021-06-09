#!/usr/bin/env bash
#this file is for testing project 0
pwd

ex_path=~/matthew-project0-production
test_path=~/project-data


source "$ex_path/venv/bin/activate"

if [[ -d $test_path ]] ; then
	         
		[[ -d $test_path ]] 2> error_logs.txt && exit 1
	
fi

