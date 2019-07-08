#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re
import sys

#option to choose a directory by providing the full path, otherwise, current working directory will be used
if len(sys.argv) > 2: 
    directory = input("Full path or subdirectory you would like to search: ")
    keyword = input("Keyword you like to search: ")
else: 
    directory = os.getcwd()
    keyword = '"TODO"'

#function to search for files and subdirectories, breadth first search
def FullList(dir_name):
    #get files in the immediate directory
    filelist = os.listdir(dir_name)
    allFiles = list()
    #identify directories within immediate directory
    for record in filelist:
        #get absolute path by joining immediate directory and files within
        absolutepath = os.path.join(dir_name, record)
        #get files in sub directories
        if os.path.isdir(absolutepath):
            allFiles = allFiles + FullList(absolutepath)
        else:
            allFiles.append(absolutepath)
    return allFiles


#Search through each file for keyword (eg: "TODO") and print every file containing "TODO"
def SearchFile(files_list):
    keywordFiles = list()
    for eachfile in filespath:
        toread = open(eachfile, "r")
        try: 
            for line in toread:
                if re.search(keyword, line):
                    keywordFiles.append(eachfile)
                else:
                    continue
        except UnicodeDecodeError:    #to skip files which are non-text
            pass
    return list(set(keywordFiles))



#To get list of files to search through
filespath = FullList(directory)

#Return all files containing keyword "TODO"
uniquelist = SearchFile(filespath)
for row in uniquelist: 
    print(row)
