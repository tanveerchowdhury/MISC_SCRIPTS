#!/usr/bin/python

"""
script Name: fileexists.py
Description:
Script to check if a file exists in a specified directory
Created by: tanveerchowdhury 
Date: Sept 16, 2017
"""

# import libraries and modules
import sys
from datetime import datetime
import os
import re 

""" 
Function to get current timestamp
"""
def getDateTime():

    i = datetime.now()
    return str(i)

"""
 Fucntion to get Directory Listing 
 to search for the file
"""

def checkFile():

    fileList = os.listdir('/home/tanveer/Scripts/') # Grab the directory List

    # Iterate through all the files and directories and search for spefied file 
    for filename in fileList:
        fsearch = re.search( r'_a_test', filename,re.M|re.I)   
     
        if fsearch:
            print (getDateTime() + " File Found "+ fsearch.group())
        else:
	    print (getDateTime() + " File Not Found ")


def main():
   
    print ( getDateTime() + " Script Execution Started")
    checkFile()

if __name__ == "__main__":
    main()


