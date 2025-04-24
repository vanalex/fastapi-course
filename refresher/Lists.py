class Person:
    def __init__(self, first_name, last_name, age, occupation):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.occupation = occupation

    def __repr__(self):
        return f"{self.first_name} {self.last_name} {self.age} {self.occupation}"

people = [
    Person("Alice", "Johnson", 28, "Software Engineer"),
    Person("Bob", "Smith", 35, "Doctor"),
    Person("Charlie", "Davis", 22, "Student"),
    Person("Diana", "Martinez", 41, "Professor"),
    Person("Ethan", "Wilson", 33, "Graphic Designer")
]

[print(person) for person in people]

george = Person("George", "Taylor", 45, "Architect")

people.append(george)

[print(person) for person in people]

fiona = Person("Fiona", "Garcia", 29, "Marketing Specialist")

people.insert(2, fiona)

[print(person) for person in people]

people.remove(george)

[print(person) for person in people]

popped_person = people.pop(0)

print(f" popped_person : {popped_person}")
print()

[print(person) for person in people]
print()
people.sort(key=lambda person: person.last_name)
[print(person) for person in people]

print()
people.sort(key=lambda person: person.age)
[print(person) for person in people]




