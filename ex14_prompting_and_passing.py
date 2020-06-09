from sys import argv

script, user_name = argv
item = '> '

print(f"Hi {user_name}, I'm the {script} script")
print("I'd like to ask you a few questions")
print(f"Do you like me {user_name}?")
likes = input(item)


print(f"Where do you live {user_name}")
lives = input(item)


print("What type of computer do you have?")
computer = input(item)



print(f"""
Alright, so you said you like {likes} about liking me.
You said you live in  the {lives} and that you have a {computer}.
Nice""")



