i = 0

while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
    if i == 4:
        break
else:
    print("i is now larger or equal to 5")

# Implementation for the assignment
my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# Initialize counter for while loop
counter = 0

# While loop to run 3 times
while counter < 3:
    # For loop to iterate through my_list
    for day in my_list:
        # Skip Monday
        if day == "Monday":
            continue
        # Print the current day
        print(day)

    # Increment counter after each complete iteration of the for loop
    counter += 1
