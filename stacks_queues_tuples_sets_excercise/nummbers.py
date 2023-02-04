first_sequence = set(int(item) for item in input().split())
second_sequence = set(int(item) for item in input().split())

functions = {
    "Add First": lambda x: [first_sequence.add(el) for el in numbers],
    "Add Second": lambda x: [second_sequence.add(el) for el in numbers],
    "Remove First": lambda x: [first_sequence.discard(el) for el in numbers],
    "Remove Second": lambda x: [second_sequence.discard(el) for el in numbers],
    "Check Subset": lambda: print(True) if first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence) else print(False)
}

for i in range(int(input())):
    command_first_part, *data = input().split()
    current_command = command_first_part + " " + data.pop(0)
    if data:
        numbers = [int(i) for i in data]
        functions[current_command](numbers)
    else:
        functions[current_command]()

print(*sorted(first_sequence), sep=', ')
print(*sorted(second_sequence), sep=', ')


