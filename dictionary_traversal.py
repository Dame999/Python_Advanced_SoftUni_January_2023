import os


def save_extensions(dir_name, first_level=False):
    for filename in os.listdir(dir_name):
        file = os.path.join(dir_name, filename)

        if os.path.isfile(file):
            extension = filename.split(".")[-1]

            if extension not in extensions:
                extensions[extension] = []

            extensions[extension].append(filename)

        elif os.path.isdir(file) and not first_level:
            save_extensions(file, first_level=True)


directory = input()

extensions = {}
result = []

save_extensions(directory)

extensions = sorted(extensions.items(), key=lambda x: x[0])

for extension, filename in extensions:
    result.append(f".{extension}")

    for name in filename:
        result.append(f"- - - {name}")

with open("report.txt", "w") as file:
    file.write('\n'.join(result))
