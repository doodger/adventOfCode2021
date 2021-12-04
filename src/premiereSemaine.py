def int_list_from_text(name_of_file):
    output = []
    with open(name_of_file) as f:
        for line in f:
            output.extend([int(x) for x in line.split()])
    return output


def sliding_comparer(list_like):
    return len( # Idée d'un collègue; plus rapide
        [None for previous, current in zip(list_like, list_like[1:]) if current > previous]
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

def accumulate_binary(array_of_array):
    ratio = len(array_of_array)//2
    return list(map(lambda x: 1 if x>ratio else 0 ,list(map(sum,zip(*array_of_array)))))

def gamma_to_epsilon(list_of_bits):
    test = list(map( lambda x: 1 if x==0 else 0 , list_of_bits))
    return test

def list_of_bit_to_int(list_of_bits):
    out = 0
    for bit in list_of_bits:
        out = (out << 1) | bit
    return out

def day_3_io(path):
    arr = []
    with open(path) as f:
        for line in f:
            if line[-1] == '\n':
                line = line[:-1]
            arr.append([int(i) for i in list(line)])
    return(arr)

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


def third_day():
    gamma = accumulate_binary( day_3_io("src/day3input.txt") )
    epsilon = gamma_to_epsilon(gamma)
    print(list_of_bit_to_int(gamma)*list_of_bit_to_int(epsilon))

def main():
    print("oh oh oh!")
    third_day()
if __name__ == "__main__":
    main()
