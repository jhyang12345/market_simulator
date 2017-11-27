import random, os
from collections import Counter

rows = 7
cols = 6

def makegrid(rows=7, cols=6):
    ret = []
    for x in range(rows):
        row = []
        for y in range(cols):
            row.append(0)
        ret.append(row)
    return ret

def write_to_file(text, filename="simulation_output.txt"):
    append_write= ""
    if os.path.exists(filename):
        append_write = 'a'
    else:
        append_write = 'w'
    with open(filename, append_write) as record_file:
        record_file.write(text)

def print_grid(grid):
    for row in grid:
        ret = ""
        for person in row:
            if person != 0:
                ret += str(person.number).rjust(4)
                ret += " "
            else:
                ret += str(0).rjust(4)
                ret += " "
        print(ret)

def print_group(grid):
    for row in grid:
        ret = ""
        for person in row:
            if person != 0:
                ret += str(person.group.id).rjust(4)
                ret += " "
            else:
                ret += str(0).rjust(4)
                ret += " "
        print(ret)

def print_group_with_id(grid, index):
    gap = " "
    padding = "      "
    empty_seats = 0
    for row in grid:
        ret = ""
        for person in row:
            if person != 0:
                ret += str(person.group.id).rjust(4)
                ret += " "
            else:
                ret += str(0).rjust(4)
                empty_seats += 1
                ret += " "
        ret += padding
        for person in row:
            if person != 0:
                ret += str(person.number).rjust(4)
                ret += gap
            else:
                ret += str(0).rjust(4)
                ret += gap
        ret += padding
        for person in row:
            if person != 0:
                ret += str(person.hours).rjust(4)
                ret += gap
            else:
                ret += str(0).rjust(4)
                ret += gap
        ret += padding
        for person in row:
            if person != 0:
                ret += str(person.happiness[index]).rjust(4)
                ret += gap
            else:
                ret += str(0).rjust(4)
                ret += gap


        print(ret)
        write_to_file(ret + '\n')
    print("Empty Seats: %d\n" % (empty_seats))
    write_to_file("Empty Seats: %d\n\n" % (empty_seats))



def choose_hours(low =1, high = 4): # inclusive
    return random.randint(low, high)

def choose_grid(grids, group):
    choice = random.randint(0, len(grids) - 1)
    if(not group.ishappy(choice)):
        return
    group.set_hour(choose_hours())
    result = fit_grid(grids[choice], group)
    if(result):
        pass
    else:
        group.unhappy(choice)


def fit_grid(grid, group):
    num = len(group.members)
    spots = []
    for x in range(len(grid)):
        for y in range(len(grid[0]) - num + 1):
            empty = True
            for i in range(num):
                if(grid[x][y + i] != 0):
                    empty = False
            if(empty):
                spots.append([x, y])
    if not spots:
        return False
    spots_index = random.randint(0, len(spots) - 1)
    spot = spots[spots_index]
    spot_x = spot[0]
    spot_y = spot[1]
    group.occupied = grid
    for y in range(spot_y, spot_y + num):
        grid[spot_x][y] = group.members[y - spot_y]
    return True

def print_population_happiness(population, index):
    ret = []
    for person in population:
        ret.append(person.happiness[index])
    c = Counter(ret)
    keys = sorted(list(c.keys()))
    for key in keys:
        print(str(key) + ": " + str(c[key]))
    print()
