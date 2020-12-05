# Import a script from sys
from sys import argv

# Defines the input_file as the filename entered
script, input_file = argv

# Defines the print_all function to read the file
def print_all(f):
# Prints the function to read the file
    print(f.read())

# Defines the function to rewind the file
def rewind(f):
# Places the seek function back at the start
    f.seek(0)

# Defines the function to list a line count within a file
def print_a_line(line_count, f):
# Counts the line and reads that line
    print(line_count, f.readline())

# Defines the variable as the opened input file
current_file = open(input_file)

# Prints the script
print("First let's print the whole file:\n")

# Prints the file, reads it to the end.
print_all(current_file)

# Prints the script
print("Now let's rewind, kind of like a tape.")

# Brings the reading back to beginning of the file
rewind(current_file)

# Prints the script
print("Let's print three lines:")

# Defines the current line in the function for the file
current_line = 1
# Runs the print_a_line function on the current location of the file
    ## def print_a_line(line_count = 1, f):
    ## print(line_count, f.readline())
print_a_line(current_line, current_file)

# Defines the line one lower than the previous function
current_line = current_line + 1
# Runs the print_a_line function on that next line
    ## def print_a_line(line_count = 2, f):
    ## print(line_count, f.readline())
print_a_line(current_line, current_file)

# Defines the next line in the function
current_line = current_line + 1
# Runs the function
    ## def print_a_line(line_count = 3, f):
    ## print(line_count, f.readline())
print_a_line(current_line, current_file)
