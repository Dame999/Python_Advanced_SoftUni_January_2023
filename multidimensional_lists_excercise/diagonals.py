n = int(input())
matrix = [[int(el) for el in input().split(", ")] for row in range(n)]

primary_diagonal = [matrix[row][row] for row in range(len(matrix))]
secondary_diagonal = [matrix[row][n - row - 1] for row in range(len(matrix))]

sum_primary = sum(primary_diagonal)
sum_secondary = sum(secondary_diagonal)

print(f"Primary diagonal: {', '.join([str(el) for el in primary_diagonal])}. Sum: {sum_primary}")
print(f"Secondary diagonal: {', '.join([str(el) for el in secondary_diagonal])}. Sum: {sum_secondary}")