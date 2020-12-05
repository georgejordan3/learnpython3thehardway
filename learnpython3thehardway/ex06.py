# Providing a value = 10 for variable {types_of_people}
types_of_people = 10
# Formatting the value within the string
x = f"There are {types_of_people} types of people."

# Providing a value string for variable {binary}
binary = "binary"
# Providing a value string for variable {do_not}
do_not = "don't"
# Formatting the values with the string
y = f"Those who know {binary} and those who {do_not}."

# Prints variable {x}
print(x)
# Prints variable {y}
print(y)

# Prints variable {x} within the reiterative string
print(f"I said: {x}")
# Prints variable {y} within the reiterative string
print(f"I also said: '{y}'")

# Boolean truth value for variable {hilarious}
hilarious = False
# Provides string for variable
joke_evaluation = "Isn't that joke so funny?! {}"

# Prints formatted truth value for the variable string
print(joke_evaluation.format(hilarious))

# Provides string value for variable {w}
w = "This is the left side of..."
# Provides string value for variable {e}
e = "a string with a right side."

# Prints both variables as a string
print(w + e)
