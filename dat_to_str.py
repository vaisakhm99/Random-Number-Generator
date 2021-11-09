# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 11:09:06 2021

@author: VAISAKH M
"""
#converts a .dat file to .txt file

file="quantis"

outfile = open(file+".txt", "w")#opens output .txt file

for n in open(file+".dat", "rb").read():#opens input .dat file
    outfile.write(f"{n:08b}")
outfile.close()