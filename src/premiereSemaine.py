def int_list_from_text(name_of_file):
    output = []
    with open(name_of_file) as f:
        for line in f:
            output.extend([int(x) for x in line.split()])
    return output


def sliding_comparer(list_like):
    return sum(
        [1 for previous, current in zip(list_like, list_like[1:]) if current > previous]
    )

def tuple_list_from_text(name_of_file):
    output = []
    with open(name_of_file) as f:
        for line in f:
            inter = [x for x in line.split() ]
            inter[1] = int(inter[1])
            output.append(tuple(inter))
    return output

def generate_direction_part_one(direction_tuple):
    direction = direction_tuple[0]
    strength = direction_tuple[1]

    if direction=="forward":
        output = (strength,0)
    elif direction=="up":
        output = (0,-strength)
    elif direction == "down":
        output = (0, strength)
    else:
        output = (0,0)
    return output

def generate_direction_part_two(direction_tuple,current_aim):
    direction = direction_tuple[0]
    strength = direction_tuple[1]

    if direction=="forward":
        output = (strength,current_aim*strength,current_aim)
    elif direction=="up":
        output = (0,0,current_aim-strength)
    elif direction == "down":
        output = (0, 0,current_aim+strength)
    else:
        output = (0,0,current_aim)
    return output


def firstDay():
    # puzzles of the first day: finding how many entries in a list are bigger than the previous one,
    # as well as finding how many group of three entries are bigger than the previous one.
    firstDay = int_list_from_text("day2input.txt")
    print(firstDay)

    count = sliding_comparer(firstDay)
    print(count)

    sliding_window = [
        sum([a, b, c]) for a, b, c in zip(firstDay, firstDay[1:], firstDay[2:])
    ]
    new_count = sliding_comparer(sliding_window)
    print(new_count)

def secondDay():
    travel = [0,0]
    input = tuple_list_from_text("src/day2input.txt")
    for tup in input:
        dir = generate_direction_part_one(tup)
        travel[0] += dir[0]
        travel[1] += dir[1]

    travel = [0,0,0]
    for tup in input:
        dir = generate_direction_part_two(tup,travel[2])
        travel[0] += dir[0]
        travel[1] += dir[1]
        travel[2] = dir[2]
    print(travel[0]*travel[1])


def main():
    print("oh oh oh!")
if __name__ == "__main__":
    main()
