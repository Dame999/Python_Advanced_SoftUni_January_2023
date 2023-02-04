def fill_the_box(*args):
    size_of_the_box = args[0] * args[1] * args[2]
    free_space = size_of_the_box
    for i in range(3, len(args)):
        if args[i] == "Finish":
            break
        if args[i] <= free_space:
            free_space -= args[i]
        else:
            leftover = args[i] - free_space
            free_space = 0
            return f"No more free space! You have {sum(args[i+1:len(args) - 1]) + leftover} more cubes."

    return f"There is free space in the box. You could put {free_space} more cubes."



print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))