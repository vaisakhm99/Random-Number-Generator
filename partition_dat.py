# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 12:40:23 2021

@author: VAISAKH M
"""
file='quantis'
CHUNK_SIZE = 5000000
file_number = 1
with open(file+'.dat','rb') as f:
    chunk = f.read(CHUNK_SIZE)
    while chunk:
        with open(file+ str(file_number)+'.dat','wb') as chunk_file:
            chunk_file.write(chunk)
        file_number += 1
        chunk = f.read(CHUNK_SIZE)