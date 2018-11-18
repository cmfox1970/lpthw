name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
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

cm_per_inch = 2.54
kg_per_pound = 1 / 2.20

height_in_cm = height * cm_per_inch
weight_in_kg = weight * kg_per_pound

print(f"His weight in kilograms is {round(weight_in_kg)} kilos.")
print(f"His height in centimeters is {height_in_cm} cm.")
