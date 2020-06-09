from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Printing from {from_file} to {to_file}")

#in_file = open(from_file)
indata = open(from_file).read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the Output file exist? {exists(to_file)}")
print("ready, hit enter to continue or ctrl c to cancel")
input('> ')

out_file = open(to_file,'w').write(indata)

print("Donezo")


