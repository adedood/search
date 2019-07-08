# search

To search for files containing keywords of interest

# Usage

python search.py [ directory ] [ keyword ]

optional arguments:
directory          specify directory to search 
keyword            specify keyword to search

An input prompt will appear for easy input 
Where no additional arguments are given, script will search for the working directory with "TODO" as keyword

# Word Search
A mix of Breadth First Search and Depth First Search is used. 
BFS is used to locate the files in immediate directory, followed by a recursive DFS to search subsequent directories. 

# Test Cases
Execute test cases in test.sh script
Script with basic test cases of files to search for

