rows, columns = input().split()

palindrome_matrix = []

for r in range(97, 97 + int(rows)):
    current_row = []
    for c in range(97, 97 + int(columns)):
        current_row.append(f"{chr(r)}{chr(r+c-97)}{chr(r)}")

    palindrome_matrix.append(current_row)

[print(*el) for el in palindrome_matrix]