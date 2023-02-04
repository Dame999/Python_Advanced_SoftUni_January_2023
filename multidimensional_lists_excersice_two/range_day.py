def is_direction_valid(matrix_data, move_direction, moving_steps, current_position):
    row_direction = directions[move_direction][0] * moving_steps + current_position[0]
    column_direction = directions[move_direction][1] * moving_steps + current_position[1]

    if 0 <= row_direction < len(matrix_data) and 0 <= column_direction < len(matrix_data) \
            and matrix_data[row_direction][column_direction] == ".":
        return True
    return False


def move_func(matrix_data, move_direction, moving_steps, current_position):
    if is_direction_valid(matrix_data, move_direction, moving_steps, current_position):

        matrix_data[current_position[0]][current_position[1]] = "."

        row_direction = directions[move_direction][0] * moving_steps + current_position[0]
        column_direction = directions[move_direction][1] * moving_steps + current_position[1]

        current_position = [row_direction, column_direction]
        matrix_data[row_direction][column_direction] = "A"

    return matrix_data, current_position


def shoot_func(matrix_data, shoot_direction, current_position, targets, hit_targets_position):
    row, column = current_position[0], current_position[1]

    while True:
        row += directions[shoot_direction][0]
        column += directions[shoot_direction][1]

        if 0 <= row < len(matrix_data) and 0 <= column < len(matrix_data):
            if matrix_data[row][column] == "x":
                hit_targets_position.append([row, column])
                targets -= 1
                matrix_data[row][column] = "."
                break
        else:
            break
    return matrix_data, targets, hit_targets_position


size = 5

my_position = []
matrix = []
total_targets = 0
hit_targets = []
for r in range(size):
    matrix.append(input().split())

    if "A" in matrix[r]:
        my_position = [r, matrix[r].index("A")]
    if "x" in matrix[r]:
        total_targets += matrix[r].count("x")

directions = {
    "up": (-1, 0),
    "right": (0, 1),
    "down": (1, 0),
    "left": (0, -1),
}

number_of_commands = int(input())

for i in range(number_of_commands):

    command_data = input().split()

    if "move" in command_data:
        direction, steps = command_data[1], int(command_data[2])
        matrix, my_position = move_func(matrix, direction, steps, my_position)

    elif "shoot" in command_data:
        direction = command_data[1]
        matrix, total_targets, hit_targets = shoot_func(matrix, direction, my_position, total_targets, hit_targets)


if total_targets > 0:
    print(f"Training not completed! {total_targets} targets left.")
else:
    print(f"Training completed! All {len(hit_targets)} targets hit.")

[print(el, end="\n") for el in hit_targets]