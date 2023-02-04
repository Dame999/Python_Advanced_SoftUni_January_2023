n = int(input())

matrix = [[int(el) for el in input().split()] for r in range(n)]

primary_diagonal = [matrix[r][r] for r in range(n)]
secondary_diagonal = [matrix[r][n-r-1] for r in range(n)]

difference = abs(sum(primary_diagonal) - sum(secondary_diagonal))
print(difference)