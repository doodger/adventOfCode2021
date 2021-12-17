from collections import Counter
from itertools import starmap
import cProfile


def thermal_line_coordinator(i_string):
    output = Counter({})
    numbers = [int(i) for i in i_string.replace("->", ",").split(",")]
    if numbers[1] == numbers[3]:
        for x in range(numbers[0], numbers[2] + 1):
            output[(x, numbers[1])] = 1
        for x in range(numbers[2], numbers[0] + 1):
            output[(x, numbers[1])] = 1
    if numbers[0] == numbers[2]:
        for y in range(numbers[1], numbers[3] + 1):
            output[(numbers[0], y)] = 1
        for y in range(numbers[3], numbers[1] + 1):
            output[(numbers[0], y)] = 1
    if numbers[2] - numbers[0] == numbers[3] - numbers[1]:  # -45 degree diagonal
        for y in range(numbers[1], numbers[3] + 1):
            output[(y, y)] = 1
        for y in range(numbers[3], numbers[1] + 1):
            output[(y, y)] = 1
    if (numbers[2] == numbers[0]) & (numbers[3] == numbers[1]):  # -45 degree diagonal
        for y in range(numbers[0], numbers[2] - numbers[0] + 1):
            output[(y, numbers[2] - y)] = 1
        for y in range(numbers[2], numbers[0] - numbers[2] + 1):
            output[(y, numbers[0] - y)] = 1
    return output


def thermal_line_horizontal_vertical(i_string):

    output = Counter({})
    numbers = [int(i) for i in i_string.replace("->", ",").split(",")]
    if numbers[1] == numbers[3]:
        for x in range(numbers[0], numbers[2] + 1):
            output[(x, numbers[1])] = 1
        for x in range(numbers[2], numbers[0] + 1):
            output[(x, numbers[1])] = 1
    if numbers[0] == numbers[2]:
        for y in range(numbers[1], numbers[3] + 1):
            output[(numbers[0], y)] = 1
        for y in range(numbers[3], numbers[1] + 1):
            output[(numbers[0], y)] = 1
    return output


def day_four():
    # very slow
    with open("../src/day5input.txt") as f:
        thermal_vents = [thermal_line_horizontal_vertical(line.strip()) for line in f]

    total = sum(thermal_vents, Counter())

    print(sum([1 for i in total.items() if i[1] != 1]))


def fishy(remaining_day):
    if remaining_day == 0:
        output = [6, 8]
    else:
        output = [remaining_day - 1]
    return output


def many_fishy(list_of_fish):
    return [fish for output in list(map(fishy, list_of_fish)) for fish in output]

def counter_fishy(list_of_fish,n):
    fish_school = Counter(list_of_fish)

    for i in range(n):
        print(i)
        updated_fish = Counter()
        updated_fish[6] = fish_school[7]+ fish_school[0]
        updated_fish[5] = fish_school[6]
        updated_fish[4] = fish_school[5]
        updated_fish[3] = fish_school[4]
        updated_fish[2] = fish_school[3]
        updated_fish[1] = fish_school[2]
        updated_fish[0] = fish_school[1]
        updated_fish[7] = fish_school[8]
        updated_fish[8] = fish_school[0]
        fish_school  = updated_fish
    return sum(updated_fish.values())

def day_six():
    fish = [
        1,
        4,
        1,
        1,
        1,
        1,
        5,
        1,
        1,
        5,
        1,
        4,
        2,
        5,
        1,
        2,
        3,
        1,
        1,
        1,
        1,
        5,
        4,
        2,
        1,
        1,
        3,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        2,
        1,
        1,
        1,
        1,
        1,
        5,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        4,
        1,
        1,
        1,
        1,
        5,
        1,
        4,
        1,
        1,
        4,
        1,
        1,
        1,
        1,
        4,
        1,
        1,
        5,
        5,
        1,
        1,
        1,
        4,
        1,
        1,
        1,
        1,
        1,
        3,
        2,
        1,
        1,
        1,
        1,
        1,
        2,
        3,
        1,
        1,
        2,
        1,
        1,
        1,
        3,
        1,
        1,
        1,
        2,
        1,
        2,
        1,
        1,
        2,
        1,
        1,
        3,
        1,
        1,
        1,
        3,
        3,
        5,
        1,
        4,
        1,
        1,
        5,
        1,
        1,
        4,
        1,
        5,
        3,
        3,
        5,
        1,
        1,
        1,
        4,
        1,
        1,
        1,
        1,
        1,
        1,
        5,
        5,
        1,
        1,
        4,
        1,
        2,
        1,
        1,
        1,
        1,
        2,
        2,
        2,
        1,
        1,
        2,
        2,
        4,
        1,
        1,
        1,
        1,
        3,
        1,
        2,
        3,
        4,
        1,
        1,
        1,
        4,
        4,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        4,
        2,
        5,
        2,
        1,
        1,
        4,
        1,
        1,
        5,
        1,
        1,
        5,
        1,
        5,
        5,
        1,
        3,
        5,
        1,
        1,
        5,
        1,
        1,
        2,
        2,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        4,
        3,
        1,
        1,
        4,
        1,
        4,
        1,
        1,
        1,
        1,
        4,
        1,
        4,
        4,
        4,
        3,
        1,
        1,
        3,
        2,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        4,
        1,
        3,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        5,
        2,
        4,
        2,
        1,
        4,
        4,
        1,
        5,
        1,
        1,
        3,
        1,
        3,
        1,
        1,
        1,
        1,
        1,
        4,
        2,
        3,
        2,
        1,
        1,
        2,
        1,
        5,
        2,
        1,
        1,
        4,
        1,
        4,
        1,
        1,
        1,
        4,
        4,
        1,
        1,
        1,
        1,
        1,
        1,
        4,
        1,
        1,
        1,
        2,
        1,
        1,
        2,
    ]
    fish = counter_fishy(fish,256)
    print(fish)

def how_many_unique(i_tuple_pre_after):
    count = 0
    for letters in i_tuple_pre_after:
        length = len(letters)
        if (length==2) or (length==3) or (length==4) or (length==7):
            count +=1

    return count

def decode(i_tuple_pre_after):
    decoded_numbers = {}
    undecoded = {}

    for entry in i_tuple_pre_after[0]:
        temporary = undecoded.get(len(entry))
        if temporary is None:
            temporary = []
        temporary.append(entry)
        undecoded[len(entry)] = temporary

    decoded_numbers[1] = undecoded[2][0]
    decoded_numbers[7] = undecoded[3][0]
    decoded_numbers[4] = undecoded[4][0]
    decoded_numbers[8] = undecoded[7][0]

    # finding up
    up = set(decoded_numbers[7])-set(decoded_numbers[1])

    # finding dl-down
    dl_down = set(decoded_numbers[8])-set(decoded_numbers[4])- up

    # finding 2
    for letter in dl_down:
        present = [ number if letter in number else False for number in undecoded[5]]
        if not all(present):
            decoded_numbers[2] = next((e for e in present if e!=False),None)
            break

    # finding 3
    for number in undecoded[5]:
        flag = False
        for letter in decoded_numbers[1]:
            if letter not in number:
                flag = True
        if not flag:
            decoded_numbers[3] = number
            break

    # finding 5
    for number in undecoded[5]:
        if number!= decoded_numbers[2] and number!=decoded_numbers[3]:
            decoded_numbers[5]=number
            break

    # finding ul and dr
    ul_dr = set(decoded_numbers[8])-set(decoded_numbers[2])
    for letter in ul_dr:
        if letter not in decoded_numbers[7]:
            ul = letter
            dr = set(ul_dr) - set(ul)

    # finding dl and down
    letter = dl_down.pop()
    if letter not in decoded_numbers[5]:
        dl = letter
        down = dl_down.pop()
    else:
        down = letter
        dl = dl_down.pop()

    # finding six
    set_of_six = set(decoded_numbers[5]) | set(dl)
    for number in undecoded[6]:
        if set(number) == set_of_six:
            decoded_numbers[6] = number
            break

    # finding nine
    set_of_nine = set(decoded_numbers[8]) - set(dl)
    for number in undecoded[6]:
        if set(number) == set_of_nine:
            decoded_numbers[9] = number
            break
    # finding zero
    for number in undecoded[6]:
        if (number!= decoded_numbers[9]) and (number!= decoded_numbers[6]):
            decoded_numbers[0] = number
            break


    #print(undecoded)
    decoding_key = { ''.join(sorted(v)): k for k, v in decoded_numbers.items()}

    digits = []
    for number in i_tuple_pre_after[1]:
        digits.append(decoding_key[''.join(sorted(number))])

    return( int(''.join(map(str,digits))) )



def day_eight():
    pre = []
    post = []
    with open("../src/day8input.txt") as f:
        for line in f:
            t_pre, t_post = line.strip().split('| ')
            pre.append(t_pre.split())
            post.append(t_post.split())
    result = sum(map(how_many_unique, post))
    print(result)

    joined = []
    pre = []
    post = []
    with open("../src/day8input.txt") as f:
        for line in f:
            t_pre, t_post = line.strip().split('| ')
            t_pre = (t_pre.split())
            t_post = (t_post.split())
            joined.append( (t_pre,t_post) )

    results = [decode(x) for x in joined ]
    print(sum(results))

def main():
    print("oh oh oh!")
    day_eight()

if __name__ == "__main__":
    main()
