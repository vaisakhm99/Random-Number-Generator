# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 11:09:06 2021

@author: VAISAKH M
"""
file=quantis
outfile = open(file+".txt", "w")
for n in open(file+"quantis1.dat", "rb").read():
    outfile.write(f"{n:08b}")
outfile.close()