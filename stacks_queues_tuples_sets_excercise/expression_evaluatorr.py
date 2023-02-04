from functools import reduce

string_expression = input().split()

index = 0

functions = {
    "*": lambda i: reduce(lambda a, b: int(a) * int(b), string_expression[:i]),
    "/": lambda i: reduce(lambda a, b: int(a) / int(b), string_expression[:i]),
    "+": lambda i: reduce(lambda a, b: int(a) + int(b), string_expression[:i]),
    "-": lambda i: reduce(lambda a, b: int(a) - int(b), string_expression[:i]),
}

while index < len(string_expression):

    if string_expression[index] in "+-*/":
        result = functions[string_expression[index]](index)
        [string_expression.pop(1) for i in range(index)]
        string_expression[0] = result
        index = 0
    index += 1

print(int(string_expression[0]))
