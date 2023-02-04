num_of_names = int(input())
unique_usernames = set(input() for i in range(num_of_names))
print(*unique_usernames, sep="\n")