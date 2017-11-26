class Group(object):
    members = []
    id = 1
    occupied = None
    def __init__(self, members):
        self.members = members

    def length(self):
        return len(self.members)

    def add_person(self, person):
        self.members.append(person)

    def set_hour(self, hour):
        for person in self.members:
            person.hours = hour
    def get_hour(self):
        return self.members[0].hours
    def ishappy(self):
        return self.members[0].happiness > 0
    def unhappy(self, magnitude=0.3):
        for person in self.members:
            person.happiness -= magnitude
            person.happiness = round(person.happiness, 1)
    def happy(self, magnitude=0.1):
        for person in self.members:
            person.happiness += magnitude
            person.happiness = round(person.happiness, 1)
# unctions:
# ength
# add_person
# set_hour
# get_hour
# ishappy
# unhappy
# happy

class Person(object):
    hours = 0
    group = []
    number = 0
    happiness = 1.0
    def __init__(self, hours, group, number):
        self.hours = hours
        self.group = group
        self.number = number
        self.happiness = 1.0

    def played(self):
        self.hours -= 1

    def _print(self):
        print("Person: " + str(self.number) + ", hours: " + str(self.hours))
