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
    def ishappy(self, index):
        return self.members[0].happiness[index] > 0
    def unhappy(self, index, magnitude=0.3):
        for person in self.members:
            person.happiness[index] -= magnitude
            person.happiness[index] = round(person.happiness[index], 1)
    def happy(self, index, magnitude=0.1):
        for person in self.members:
            person.happiness[index] += magnitude
            person.happiness[index] = round(person.happiness[index], 1)
# functions:
# length
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
    def __init__(self, hours, group, number, grid_types=4):
        self.hours = hours
        self.group = group
        self.number = number
        self.happiness = []
        for i in range(grid_types):
            self.happiness.append(1.0)

    def played(self):
        self.hours -= 1

    def _print(self):
        print("Person: " + str(self.number) + ", hours: " + str(self.hours))
