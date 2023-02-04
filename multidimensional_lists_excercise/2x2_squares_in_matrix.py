rows, columns = input().split()

matrix = [input().split() for row in range(int(rows))]

two_by_two_matrix = 0
for row in range(int(rows) - 1):
    for col in range(int(columns) - 1):
        if matrix[row][col] == matrix[row+1][col] and matrix[row][col] == matrix[row+1][col+1] \
                and matrix[row][col] == matrix[row][col+1]:
            two_by_two_matrix += 1


print(two_by_two_matrix)
