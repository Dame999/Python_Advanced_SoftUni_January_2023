rows, columns = input().split()

matrix = [[int(el) for el in input().split()] for row in range(int(rows))]

max_sum = 0
matrix_with_max_sum = []

for r in range(int(rows) - 2):
    for c in range(int(columns) - 2):
        current_sum = 0
        current_matrix = [[matrix[row][column] for column in range(c, c + 3)] for row in range(r, r + 3)]

        for row in current_matrix:
            current_sum += sum(row)

        if matrix_with_max_sum:
            if current_sum > max_sum:
                max_sum = current_sum
                matrix_with_max_sum = current_matrix
        else:
            max_sum = current_sum
            matrix_with_max_sum = current_matrix

print(f"Sum = {max_sum}")
[print(*row) for row in matrix_with_max_sum]
