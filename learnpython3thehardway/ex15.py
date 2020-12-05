# Imports the command argv from the sys library
from sys import argv

# The script filename is defined by the user entry
script, filename = argv

# Defines the variable txt as the opened filename
txt = open(filename)

# Formates the function to print the name of the file chosen by user input
print(f"Here's your file {filename}:")
# Prints the text from the text file chosen by user input
print(txt.read())

# Prints the prompt for the user to type the filename again
print("Type the filename again:")
# Defines the variable as the input with the printed "> " before the user input
file_again = input("> ")

# Opens the file again
txt_again = open(file_again)

# Prints the same user selected file
print(txt_again.read())
