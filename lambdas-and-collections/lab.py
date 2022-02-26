names = ["Juana", "Maria", "Pepita", "Lucia", "Josue"]
print(sorted(names, key=lambda s:s.lower()))

names_age = [{"name": "Juana", "age":12},{"name": "Maria", "age":15}, {"name": "Pepita", "age":10}, {"name": "Lucia", "age":25}, {"name": "Josue", "age":18}]
print(list(map(lambda p: f'{p.get("name")} is {p.get("age")} years old', names_age)))

print(list(sorted(filter(lambda p: p.get("age") < 70, names_age), key=lambda d: d['age'])))