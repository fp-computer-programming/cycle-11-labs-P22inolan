# Author: IBN (ADMG) 2/8/2022

file = open("cycle-11-labs-P22inolan/alma_mater.txt", "r")
while True:
     line = file.readline()
     if len(line) == 0:
           break
     print (line, end="\n")
file.close()