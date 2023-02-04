matrix_size = int(input())
matrix = []

for r in range(matrix_size):
    matrix.append([el for el in input()])

knight_moves = {
    (-1, -2),
    (-2, -1),
    (-2, 1),
    (-1, 2),
    (1, 2),
    (2,1),
    (2, -1),
    (1, -2),
}

removed_knights = 0


while True:
    max_attacks = 0
    knight_with_most_attacks_position = (0, 0)
    for row in range(matrix_size):
    
        for col in range(matrix_size):

            if matrix[row][col] == "K":
                current_attacks = 0
                for move in knight_moves:
                    cur_row, cur_col = row + move[0], col + move[1]
                    if 0 <= cur_row < matrix_size and 0 <= cur_col < matrix_size:

                        if matrix[cur_row][cur_col] == "K":
                            current_attacks += 1
                if current_attacks > max_attacks:
                    max_attacks = current_attacks
                    knight_with_most_attacks_position = (row, col)
    if max_attacks == 0:
        break

    matrix[knight_with_most_attacks_position[0]][knight_with_most_attacks_position[1]] = 'O'
    removed_knights += 1


print(removed_knights)



