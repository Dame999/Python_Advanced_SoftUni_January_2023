import os

while True:

    command, *data = input().split("-")

    if command == "Create":
        with open(f"{data[0]}", "w") as file:
            pass

    elif command == "Add":
        with open(f"{data[0]}", "a") as file:
            file.write(f"{data[1]}\n")

    elif command == "Replace":

        try:
            with open(f"{data[0]}", "r") as file:
                text = file.read()

            text = text.replace(data[1], data[2])

            with open(f"{data[0]}", "w") as file:
                file.write(text)

        except FileNotFoundError:
            print("An error occurred")

    elif command == "Remove":

        try:
            os.remove(f"{data[0]}")
        except FileNotFoundError:
            print("An error occurred")

