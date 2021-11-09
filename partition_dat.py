# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 12:40:23 2021

@author: VAISAKH M
"""
#partitions a .dat file to multiple .dat files of equal size

file='quantis'

CHUNK_SIZE = 5000000 #size of each file

file_number = 1

with open(file+'.dat','rb') as f:#opens main file
    chunk = f.read(CHUNK_SIZE)
    while chunk:
        with open(file+ str(file_number)+'.dat','wb') as chunk_file: #opens the output files
            chunk_file.write(chunk)
        file_number += 1
        chunk = f.read(CHUNK_SIZE)