

#This file is for testing project 0 
pwd

py_interpreter_before=$("python --version")

#start venv
source ~/revature/matthew-project0/venv/bin/activate

#verify python interpreter version 
py_interpreter_after=$("python --version")

if [[ $py_interpreter_before -ne $py_interpreter_after ]]; then
	result="$py_interpreter_after : venv is correct"
	echo $result
else
	result="Test 1 : Fail incorrect interpreter"
	echo $result && exit 1
fi

