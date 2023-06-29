print("Welcome adventurer, what's your name?")
name = input("Insert name here: ")

print("Hello " + name)

# Let's make a game:
# You're traveling through a dungeon
# You can choose to go left or right
# Behind a "random" door, there is a dragon
# Behind a different door, there is a treasure

print("In front of you, there are 2 doors. Do you take the one on the left or right?")
choice = input("left or right: ")
if (choice == "left"):
    # We chose the left door.
    print("Now, there are 2 coloured doors. Do you take the red one or the blue one?")
    choice = input("red or blue: ")
    if (choice == "red"):
        # We chose the red door inside the left door
        print("You found the dragon! You lose.")
    else:
        # We chose the blue door inside the left door
        print("You found nothing.")
else:
    # we chose the right door.
    print("Now, there are 2 coloured doors. Do you take the red one or the blue one?")
    choice = input("red or blue: ")
    if (choice == "red"):
        # We chose the red door inside the left door
        print("You found nothing.")
    else:
        # We chose the blue door inside the left door
        print("You found the treasure, you win!")
    