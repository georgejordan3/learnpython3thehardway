name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
height_m = (height * float(2.54)) # centimeters
weight = 180 # lbs
weight_m = (weight * float(.453592)) # kilograms
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

print(f"He's {height_m} centimers tall.")
print(f"He's {weight_m} kilograms heavy.")
