empty_stack = []
n = int(input())

for i in range(n):
    command = input()
    if "1" in command:
        current_command, number = command.split()
        empty_stack.append(int(number))
    elif command == "2":
        if len(empty_stack) > 0:
            empty_stack.pop()
    elif command == "3":
        if len(empty_stack) > 0:
            print(max(empty_stack))
    elif command == "4":
        if len(empty_stack) > 0:
            print(min(empty_stack))

stack = []
for i in range(len(empty_stack)):
    stack.append(empty_stack.pop())

print(*stack, sep=", ")