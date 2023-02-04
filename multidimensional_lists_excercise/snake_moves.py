rows, columns = [int(i) for i in input().split()]
snake = input()

matrix = []
index = 0

for r in range(rows):
    matrix.append([])

    for c in range(columns):
        matrix[r].append(snake[index % len(snake)])
        index += 1

    if r % 2 != 0:
        matrix[r].reverse()
    print(''.join(matrix[r]))

