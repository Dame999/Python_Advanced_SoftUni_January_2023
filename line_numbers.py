from string import punctuation

with open("line_text.txt", "r") as line_text_file:
    text = line_text_file.readlines()

with open("output.txt", "w") as output_file:

    for item_index in range(len(text)):

        current_row = text[item_index]

        letters = 0
        punctuations = 0

        for symbol in current_row:

            if symbol.isalpha():
                letters += 1
            elif symbol in punctuation:
                punctuations += 1

        output_file.write(f"Line {item_index + 1}: {''.join(current_row)[:-1]} ({letters})({punctuations})\n")
