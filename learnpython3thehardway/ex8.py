# Establishes a formatter to be applied in future arguments
formatter = "{} {} {} {}"

# Prints a series of numbers using the formatter
print(formatter.format(1, 2, 3, 4))
# Prints a series of strings using the formatter
print(formatter.format("one", "two", "three", "four"))
# Prints Boolean truth values using the formatter
print(formatter.format(True, False, False, True))
# Prints a series of symbols from the formatter
print(formatter.format(formatter, formatter, formatter, formatter))
# Prints the four strings in place of the formatter
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
