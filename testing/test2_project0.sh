#!/usr/bin/env bash
ex_path=~/matthew-project0-production
test_path=~/project-data


$ex_path/venv/bin/python3 $ex_path/main.py collection.txt 0

#test2 create /project-data/
if [[ -d $test_path ]] ; then
         echo "Test 2 pass dir created"
else
         echo "error test 2 fail" >> error_logs.txt && exit 1
fi

exit 0
