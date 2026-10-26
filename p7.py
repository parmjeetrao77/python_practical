def remove_negative(matrix):
    return [
        list(filter(lambda x: x >= 0, row))
        for row in matrix
    ]


def sort_matrix(matrix):
    return [
        sorted(row)
        for row in matrix
    ]


def square_matrix(matrix):
    return [
        list(map(lambda x: x ** 2, row))
        for row in matrix
    ]


rows = int(input("Enter number of rows: "))
matrix = []

for i in range(rows):
    row = list(map(
        int,
        input(f"Enter row {i + 1} values separated by spaces: ").split()
    ))
    matrix.append(row)

print("Original matrix:", matrix)
print("Without negative values:", remove_negative(matrix))
print("Sorted matrix:", sort_matrix(matrix))
print("Squared matrix:", square_matrix(matrix))