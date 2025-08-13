class Person:
    def __init__(self, name):
        self.name = name

persons = [
    Person("Alice"),
    Person("Bruno"),
    Person("Carla"),
    Person("Daniela"),
    Person("Eduardo")
]

def exnames(listob):
    return [obj.name for obj in listob]

names = exnames(persons)
print(names)