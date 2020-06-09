
## imports the argv ability
from sys import argv
## The inputs to argv are the filename of the python file we are running as well as the txt file that we are going to read
script, filename = argv
## This opens the filename 
txt = open(filename)

## justs prints the the filename input and then reads the file
print(f"here's your file {filename}:")
print(txt.read())

## this time it takes the filename in as an input mid way through the code rather than at the start.
print("Type the filename again:")
file_again = input("Type it here mate:")


## this then opens the file again and reads it
txt_again = open(file_again)

print(txt_again.read())
