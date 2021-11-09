# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 13:55:59 2021

@author: Dell
"""
#Merge multiple .dat files to one

# Creating a list of filenames
filenames = ['1.dat', '2.dat','3.dat']
  
# Open file3 in write mode
with open('123.dat', 'wb') as outfile:
  
    # Iterate through list
    for names in filenames:
  
        # Open each file in read mode
        with open(names,'rb') as infile:
  
            # read the data from file1 and
            # file2 and write it in file3
            outfile.write(infile.read())