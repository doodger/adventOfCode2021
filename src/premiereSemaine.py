def list_from_text(name_of_file):
    output = []
    with open("day1input.txt") as f:
        for line in f:
            output.extend([int(x) for x in line.split()])
    return output


def sliding_comparer(list_like):
    return sum(
        [1 for previous, current in zip(list_like, list_like[1:]) if current > previous]
    )


def main():
    # puzzles of the first day: finding how many entries in a list are bigger than the previous one,
    # as well as finding how many group of three entries are bigger than the previous one.

    firstDay = list_from_text("day1input.txt")
    print(firstDay)

    count = sliding_comparer(firstDay)
    print(count)

    sliding_window = [
        sum([a, b, c]) for a, b, c in zip(firstDay, firstDay[1:], firstDay[2:])
    ]
    new_count = sliding_comparer(sliding_window)
    print(new_count)


if __name__ == "__main__":
    main()
