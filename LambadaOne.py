# Given a list of dictionaries, each representing a person with name and age
# keys use lambda functions to filter out people under 18 and then map the
# remaining people's names to a new list.
people = [
    {"name": "Ajay", "age": 25},
    {"name": "Vijay", "age": 16},
    {"name": "Vineetha", "age": 19},
    {"name": "Athvik", "age": 15}
]

#  Filter people aged 18 and above
Ageundereighteen = filter(lambda person: person["age"] <= 18, people)

# Map only their names into a new list
Namesofperson = list(map(lambda person: person["name"], Ageundereighteen))

print(Namesofperson)

