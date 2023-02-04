from collections import deque

working_bees = deque((int(i) for i in input().split()))
nectar = deque((int(i) for i in input().split()))
symbols = deque(input().split())

total_honey_made = 0

functions = {
    "+": lambda: bee + current_nectar,
    "-": lambda: bee - current_nectar,
    "*": lambda: bee * current_nectar,
    "/": lambda: bee / current_nectar,
}

while nectar and working_bees:

    bee = working_bees.popleft()
    current_nectar = nectar.pop()

    while current_nectar < bee and nectar:
        current_nectar = nectar.pop()

    if symbols:
        symbol = symbols.popleft()

        result = functions[symbol]()
        total_honey_made += abs(result)
    else:
        break

print(f"Total honey made: {total_honey_made}")

if working_bees:
    print(f"Bees left: {', '.join((str(b) for b in working_bees))}")

elif nectar:
    print(f"Nectar left: {', '.join((str(n) for n in nectar))}")