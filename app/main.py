class Person:
    people = {}
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    new_list = []
    for pers in people:
        new = Person(pers["name"], pers["age"])
        new_list.append(new)
    for pers in people:
        if pers.get("husband", None):
                Person.people[pers["name"]].husband = Person.people[pers["husband"]]
        elif pers.get("wife", None):
            Person.people[pers["name"]].wife = Person.people[pers["wife"]]
    return new_list
