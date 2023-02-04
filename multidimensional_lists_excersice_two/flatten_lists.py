
lists = input().split("|")

for el in lists[::-1]:
    for i in el.split():
        print(i, end=" ")