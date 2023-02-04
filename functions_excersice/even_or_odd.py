def even_odd(*args):
    command = args[-1]

    if command == "even":
        args = [el for el in args[:-1] if el % 2 == 0]
    elif command == "odd":
        args = list(filter(lambda x: x % 2 == 1, args[:-1]))

    return args


print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))