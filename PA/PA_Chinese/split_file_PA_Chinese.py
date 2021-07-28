
#SPLIT A SINGLE FILE IN MULTIPLE FILES USING A SPLIT DELIMITER - <DOC>
#RENAME THE FILES BASED ON THEIR CONTENT

import os
import glob
import re



with open('Stanford_PA_Chinese_all.utf8', 'r', encoding="utf-8") as f:
    buff = []
    i = 0# I should put 1 in general but in this specific case I want to start from 2
    for line in f:
         
         if line.startswith("PA"):
            output = open('PA_Chinese_Split/PA00%d_Stanford.txt' % i,'w', encoding = 'utf-8')
            output.write(''.join(buff))
            output.close()
            i+=1
            buff = [] #buffer reset
            
         #if line.strip():  #skips the empty lines
         buff.append(line)
         
#for filename in os.listdir('D:/Users/Chris/Desktop/PA/PA_Chinese_raw_files/PA_Chinese_Split'):
     #with open(filename, 'r', encoding="utf-8") as openfile:
        #firstline = openfile.readline()
     #os.rename(filename, firstline.strip()+'.txt')

        

           

           

           




       
        
           

            
           
        

           
       
           
           
           
        