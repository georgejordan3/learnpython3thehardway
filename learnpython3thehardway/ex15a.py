#from sys import argv

#script, filename = argv

filename = input("Type filename here: ")
txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())
