#!/bin/bash

#Test case 1: check current directory for files containing keyword TODO
mkdir testcase1
touch ./testcase1/emptyfile.txt
echo "TODO" >> ./testcase1/test1.txt 

python search.py

# ./testcase1/test1.txt to be returned

#Test case 2: search.py must be able to check sub directory and return files from the end of directory tree
mkdir -p testcase2/folder2
touch ./testcase2/folder2/emptyfile.txt
echo "TODO" >> ./testcase2/folder2/test2.txt

python search.py

# ./testcase2/folder2/test2.txt to be returned, compare with grep command (grep TODO testcase2/*) 


#Test case 3: search.py to be able to search in other directories for other keywords
#To execute 
# python search.py <directory> <keyword> 
# when prompted, input full directory path and keyword to search. 

