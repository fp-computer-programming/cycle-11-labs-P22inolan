# Author: IBN (AMDG)

my_file = open("cycle-11-labs-P22inolan/alma_mater.txt")
contents = my_file.readlines()
contents.reverse()
new_txt = "".join(contents)
print(new_txt)
my_file.close()