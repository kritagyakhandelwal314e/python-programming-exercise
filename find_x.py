def find_x(matrix, x):
    for li in matrix:
        for element in li:
            if x == element:
                return True
    return False

matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

print(find_x(matrix, 4))
