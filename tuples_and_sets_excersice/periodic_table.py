count_of_input = int(input())
periodic_elements = set()
for i in range(count_of_input):
    [periodic_elements.add(el) for el in input().split()]

print(*periodic_elements, sep="\n")