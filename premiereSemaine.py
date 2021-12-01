

def main():
    firstDay = []
    with open('day1input.txt') as f:
        for line in f:
            firstDay.extend([int(x) for x in line.split()])

    print(firstDay)

    count = sum([1 for previous, current in zip(firstDay, firstDay[1:]) if current>previous])
    print(count)

if __name__=="__main__":
    main()