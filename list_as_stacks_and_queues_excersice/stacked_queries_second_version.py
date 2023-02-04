from collections import deque

numbers = deque()

map_functions = {
    1: lambda x: numbers.append(x[1]),
    2: lambda x: numbers.pop() if numbers else None,
    3: lambda x: print(max(numbers)) if numbers else None,
    4: lambda x: print(min(numbers)) if numbers else None,
}

for i in range(int(input())):
    current_number = [int(x) for x in input().split()]
    map_functions[current_number[0]](current_number)

numbers.reverse()

print(*numbers,sep=", ")
