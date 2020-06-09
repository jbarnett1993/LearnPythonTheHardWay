from sys import argv

script, filename = argv

print(f"Going to erase {filename}")
print("can cancel here by pressing, hit ctrl-c")
print("if you do want that, press Return")


input("?")

print("Opening the file ..... ")

target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("now asking for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these 3 lines")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()



