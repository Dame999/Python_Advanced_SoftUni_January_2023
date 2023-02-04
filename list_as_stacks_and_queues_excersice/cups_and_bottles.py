from collections import deque

cups = deque(int(c) for c in input().split())
bottles = deque(int(b) for b in input().split())

wasted_liters = 0

while True:

    if len(cups) == 0:
        print(f"Bottles: {' '.join([str(el) for el in bottles])}")
        print(f"Wasted litters of water: {wasted_liters}")
        break

    elif len(bottles) == 0:
        print(f"Cups: {' '.join([str(el) for el in cups])}")
        print(f"Wasted litters of water: {wasted_liters}")
        break

    cup = cups.popleft()
    bottle = bottles.pop()

    if bottle >= cup:
        wasted_liters += bottle - cup

    else:
        while True:
            cup -= bottle

            if cup <= 0:
                wasted_liters += abs(cup)
                break

            bottle = bottles.pop()



