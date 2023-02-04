matrix_size = int(input())
matrix = []

path_directions = {
    "up": (-1, 0),
    "right": (0, 1),
    "down": (1, 0),
    "left": (0, -1),
}

best_path = None
bunny_position = []
collected_eggs = 0
best_path_indexes = []

for r in range(matrix_size):
    matrix.append(input().split())

    if "B" in matrix[r]:
        bunny_position = [r, matrix[r].index("B")]

for direction, indexes in path_directions.items():

    current_bunny_path = []
    current_collected_eggs = 0
    row, col = bunny_position[0] + indexes[0], bunny_position[1] + indexes[1]

    while 0 <= row < matrix_size and 0 <= col < matrix_size:
        if matrix[row][col] == "X":
            break

        current_collected_eggs += int(matrix[row][col])
        current_bunny_path.append([row, col])
        row += indexes[0]
        col += indexes[1]

    if current_collected_eggs >= collected_eggs:
        collected_eggs = current_collected_eggs
        best_path = direction
        best_path_indexes = current_bunny_path


print(best_path)
print(*best_path_indexes, sep="\n")
print(collected_eggs)
