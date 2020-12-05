# Establishes a value for people
people = 30
# Establishes a value for cars
cars = 40
# Establishes a value for trucks
trucks = 15

# Produces conditional
if cars > people:
    # Prints the string given the satisfaction of the conditional
    print("We should take the cars.")
# Secondary conditional
elif cars < people:
    # Prints the string given the satisfaction of the conditional
    print("We should not take the cars.")
# Fallback condition
else:
    # Prints the string given the satisfaction of the conditional
    print("We can't decide.")

# Produces conditional
if trucks > cars:
    # Prints the string given the satisfaction of the conditional
    print("That's too many trucks.")
# Secondary conditional
elif trucks < cars:
    # Prints the string given the satisfaction of the conditional
    print("Maybe we could take the trucks.")
# Fallback condition
else:
    # Prints the string given the satisfaction of the conditional
    print("We still can't decide.")

# Produces conditional
if people > trucks:
    # Prints the string given the satisfaction of the conditional
    print("Alright, let's just take the trucks.")
# Fallback condition
else:
    # Prints the string given the satisfaction of the conditional
    print("Fine, let's stay home then.")