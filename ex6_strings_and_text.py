types_of_people = 10

x = f"There are {types_of_people} in this world"

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who do not"


print(x)
print(y)


print(f"I said {x}")
print(f"I also said {y}")

hilarious = False

joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of ....."
e = "a string with 2 sides"

print(w + e)