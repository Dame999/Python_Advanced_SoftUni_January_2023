data_input = input().split()
my_stack = []

for i in range(len(data_input)):
    my_stack.append(data_input.pop())

print(" ".join(my_stack))