from group import Person, Group
from util import *

space = list(range(210)) # 42 * 5

total = 200


ones = int(total * 2 / 25)
twos = int(total * 3 / 25)
threes = int(total * 3 / 25)
fours = int(total * 2 / 25)
num_sum = ones * 1 + twos * 2 + threes * 3 + fours * 4

people = [Person(0, [], i) for i in range(1, total + 1)]

groupings = []

group_index = 1

def popgroup(people, num):
    ret = []
    group = Group([])
    global group_index
    for x in range(num):
        index = random.randint(0, len(people) - 1)
        person = people.pop(index)
        person.group = group
        group.add_person(person)
    group.id = group_index

    group_index += 1
    return group

for x in range(ones):
    group = []
    group = popgroup(people, 1)
    groupings.append(group)

for x in range(twos):
    group = popgroup(people, 2)
    groupings.append(group)

for x in range(threes):
    group = popgroup(people, 3)
    groupings.append(group)

for x in range(fours):
    group = popgroup(people, 4)
    groupings.append(group)

# making pc cafes
grids = [makegrid(rows, cols) for x in range(4)]

def iteration(groups, grids):
    random.shuffle(groups)
    count = 0
    for group in groups:
        if group.occupied:
            count += 1
        if(not group.occupied):
            choose_grid(grids, group)
    for grid in grids:
        print_group_with_id(grid)
    print("1 hour has passed\n")

    ret = 0
    seen_list = []

    for grid_index in range(len(grids)):
        grid = grids[grid_index]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                person = grid[i][j]
                if(person != 0 and person in seen_list):
                    print(i, j)
                    continue
                seen_list.append(person)
                if(type(person) is Person):
                    person.played()
                    if person.hours == 0:
                        person.group.occupied = None
                        grid[i][j] = 0
                else:
                    pass
#    for grid in grids:
#        print_group_with_id(grid)

for hours in range(4):
    iteration(groupings, grids)
