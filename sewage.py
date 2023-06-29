# input -> redirect water or don't redirect
# redirecting water = "water"
# not redirecting = "sewage"

print("Are we redirecting the water?")
command = input()

if command == "yes":
    print("water")
else:
    print("sewage")