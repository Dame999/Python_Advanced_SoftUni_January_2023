rows, columns = input().split()

matrix = [input().split() for r in range(int(rows))]

while True:
    command_data = input().split()

    if command_data[0] == 'END':
        break

    if command_data[0] == 'swap' and len(command_data) == 5:
        row_one, col_one, row_two, col_two = int(command_data[1]), int(command_data[2]),\
                                             int(command_data[3]), int(command_data[4])
        if 0 <= row_one < int(rows) and 0 <= col_one < int(columns) and \
                0 <= row_two < int(rows) and 0 <= col_two < int(columns):
            matrix[row_one][col_one], matrix[row_two][col_two] = matrix[row_two][col_two], matrix[row_one][col_one]
            [print(*el) for el in matrix]
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")