import os
import glob
import re


for filename in os.listdir('D:/Users/Chris/Desktop/PA/PA_Uyghur_raw_files/Uyghur_raw_cleaned/PA_Uyghur_Split/'):
     with open(filename, 'r', encoding="utf-8") as openfile:
        if not filename.endswith('.py'):
            firstline = openfile.readline()
     os.rename(filename, firstline.strip()+'_Stanford.txt')