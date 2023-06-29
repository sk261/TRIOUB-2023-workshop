# We have a bunch of fruit gummies.
# We want everyone in the room to be given an equal amount of fruit gummy.
list_of_names = [
    "Phillip",
    "Mercedes",
    "Christian",
    "CJ",
    "Melissa",
    "Mason",
    "Shay"
]

# Prints out list of names
for name in list_of_names:
    print(name)

list_of_fruit_gummies = [
    0,
    0,
    0,
    0,
    0,
    0,
    30
]

total_gummies = 0

# Get the sum of all fruit gummies
for gummies in list_of_fruit_gummies:
    total_gummies = total_gummies + gummies

# Set the person at the end (Shay)'s fruit gummy count to 0
list_of_fruit_gummies[-1] = 0

# print the total number of fruit gummies
print(total_gummies)
print("List of gummies")

# print the number of fruit gummies that each individual person has
for gummies in list_of_fruit_gummies:
    print(gummies)

person_index = 0

while total_gummies > 0:
    name = list_of_names[person_index]
    print("Giving a gummy to: " + name)
    list_of_fruit_gummies[person_index] += 1
    total_gummies -= 1
    person_index += 1
    if person_index > len(list_of_fruit_gummies):
        person_index = 0

