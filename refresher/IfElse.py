
# Example 1: Greeting based on hour
hour = 21

if hour >= 6 and hour < 12:
    print("Good morning")
elif hour >= 12 and hour < 18:
    print("Good afternoon")
elif hour >= 18 and hour < 24:
    print("Good evening")
else:
    print("Good night")

# Example 2: Grade calculation
# Create a variable grade holding an integer between 0 - 100
grade = 85

# Print the letter grade based on the number grade
if grade >= 90 and grade <= 100:
    print("Your grade is: A")
elif grade >= 80 and grade <= 89:
    print("Your grade is: B")
elif grade >= 70 and grade <= 79:
    print("Your grade is: C")
elif grade >= 60 and grade <= 69:
    print("Your grade is: D")
elif grade >= 0 and grade <= 59:
    print("Your grade is: F")
else:
    print("Invalid grade")
