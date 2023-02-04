count_system = {}
input_data = input()

for el in input_data:
    if el not in count_system.keys():
        count_system[el] = 0
    count_system[el] += 1

for character, value in sorted(count_system.items()):
    print(f"{character}: {value} time/s")
