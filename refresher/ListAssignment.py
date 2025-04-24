zoo = ["Lion", "Elephant", "Giraffe", "Zebra", "Tiger"]

# Delete the animal at the 3rd index (index 2)
zoo.pop(2)
print("After deleting the animal at the 3rd index:")
print(zoo)

# Append a new animal at the end of the list
zoo.append("Monkey")
print("After appending a new animal:")
print(zoo)

# Delete the animal at the beginning of the list
zoo.pop(0)
print("After deleting the animal at the beginning:")
print(zoo)

# Print all the animals
print("All animals in the zoo:")
for animal in zoo:
    print(animal)

# Print only the first 3 animals
print("First 3 animals in the zoo:")
print(zoo[:3])
