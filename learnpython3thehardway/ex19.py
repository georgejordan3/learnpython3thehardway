# Uses the function def to define cheese_and_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
# Formats cheese_count to the printed string
    print(f"You have {cheese_count} cheeses!")
# Formats boxes_of_crackers to the printed string
    print(f"You have {boxes_of_crackers} boxes of crackers!")
# Prints a string
    print("Man that's enough for a party!")
# Prints a string and starts a new line
    print("Get a blanket.\n")


# Demonstrates another method in a string
print("We can just give the function numbers directly:")
# Uses the function with the defined values for the variables and then prints
cheese_and_crackers(20, 30)


# Demonstrates another method in a string
print("OR, we can use variables from our script:")
# Provides a value for the variable
amount_of_cheese = 10
# Provides a value for the variable
amount_of_crackers = 50

# Prints the function with the defined values above
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


# Demonstrates another method in a string
print("We can even do math inside too:")
# Prints the function with arithmetic in the values for the variables
cheese_and_crackers(10 + 20, 5 + 6)


# Demonstrates another method in a string
print("And we can combine the two, variables and math:")
# Prints the function with arithmetic and defined values above
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
