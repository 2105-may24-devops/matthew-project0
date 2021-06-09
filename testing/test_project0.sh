#this file is for testing project 0
pwd

ex_path=~/matthew-project0-production
test_path=~/project-data


source "$ex_path/venv/bin/activate"

if [[ -d $test_path ]] ; then
	        echo "error dir already exist" > error_logs.txt
	else
		        echo "test passed "
fi
#run to see if dir and fies are created
$ex_path/venv/bin/python3 $ex_path/main.py collection_file.txt 0

if [[ -d $test_path ]] ; then
	        echo "test passed dir created in correct location"
	else
		        echo "test failed: dir not created" >> error_logs.txt
fi

if [[ -e "$test_path/collection_file.txt" ]] ; then
	        echo "test passed: default collection created"
	else
		        echo "test failed: default collection not created"
fi

if [[ -e "$test_path/project_0_*" ]] ; then
	        echo "test passed: default aren't pressent"
	else
		        echo "test fail: default are present"
fi

