def index_validation(size_of_the_matrix, row_index, col_index):
    if 0 <= row_index < size_of_the_matrix and 0 <= col_index < size_of_the_matrix:
        return True
    return False


def add_func(matrix_numbers, row_index, col_index, value_to_add):
    matrix_numbers[row_index][col_index] += value_to_add
    return matrix_numbers


def subtract_func(matrix_numbers, row_index, col_index, value_to_subtract):
    matrix_numbers[row_index][col_index] -= value_to_subtract
    return matrix_numbers


matrix_size = int(input())

matrix = [[int(c) for c in input().split()] for r in range(matrix_size)]

while True:

    command = input().split()

    if 'END' in command:
        [print(*row) for row in matrix]
        break

    cur_command, row, column, value = command[0], int(command[1]), int(command[2]), int(command[3])

    if index_validation(matrix_size, row, column):
        if cur_command == 'Add':
            matrix = add_func(matrix, row, column, value)
        elif cur_command == 'Subtract':
            matrix = subtract_func(matrix, row, column, value)
    else:
        print("Invalid coordinates")

