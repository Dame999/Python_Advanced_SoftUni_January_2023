n, m = input().split()

first_set = {int(input()) for num in range(int(n))}
second_set = {int(input()) for num in range(int(m))}

result = first_set.intersection(second_set)
print(*result, sep="\n")