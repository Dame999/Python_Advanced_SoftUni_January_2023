matrix_size = int(input())
matrix = []

alice_pos = []

for row in range(matrix_size):
    matrix.append(input().split())

    if "A" in matrix[row]:
        alice_pos = [row, matrix[row].index("A")]

directions = {
    "up": (-1, 0),
    "right": (0, 1),
    "down": (1, 0),
    "left": (0, -1),
}
total_bags_of_tea = 0
while total_bags_of_tea < 10:

    command = input()
    r, c = directions[command]
    matrix[alice_pos[0]][alice_pos[1]] = "*"
    alice_pos[0] += r
    alice_pos[1] += c
    if not (0 <= alice_pos[0] < matrix_size and 0 <= alice_pos[1] < matrix_size):
        print("Alice didn't make it to the tea party.")
        break
    elif matrix[alice_pos[0]][alice_pos[1]] == "R":
        matrix[alice_pos[0]][alice_pos[1]] = "*"
        print("Alice didn't make it to the tea party.")
        break

    if matrix[alice_pos[0]][alice_pos[1]].isdigit():
        total_bags_of_tea += int(matrix[alice_pos[0]][alice_pos[1]])
        matrix[alice_pos[0]][alice_pos[1]] = "*"

else:
    print("She did it! She went to the party.")

[print(*r) for r in matrix]