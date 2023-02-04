matrix_size = int(input())
matrix = [[int(c) for c in input().split()] for r in range(matrix_size)]
bombs_cells = [el for el in input().split()]

alive_cells = []
sum_of_alive_cells = 0

bombing_directions = {
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1),
}

for i in range(len(bombs_cells)):
    current_bomb_pos = int(bombs_cells[i][0]), int(bombs_cells[i][2])

    for direction in bombing_directions:
        row_index, column_index = current_bomb_pos[0] + direction[0], current_bomb_pos[1] + direction[1]

        if 0 <= row_index < matrix_size and 0 <= column_index < matrix_size and matrix[row_index][column_index] > 0:
            matrix[row_index][column_index] -= matrix[current_bomb_pos[0]][current_bomb_pos[1]]
    matrix[current_bomb_pos[0]][current_bomb_pos[1]] = 0

alive_cells += [el for row in matrix for el in row if el > 0]

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")
[print(*row) for row in matrix]
