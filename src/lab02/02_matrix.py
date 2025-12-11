def transpose(mat: list[list[float | int]]) -> list[list]:
    if not mat:
        return []
    if not all(len(row) == len(mat[0]) for row in mat):
        raise ValueError
    num_rows = len(mat)
    num_cols = len(mat[0])
    return [[mat[r][c] for r in range(num_rows)] for c in range(num_cols)]


# print(transpose([[1, 2, 3]]))
# print(transpose([[1], [2], [3]]))
# print(transpose([[1, 2], [3, 4]]))
# print(transpose([]))
# try:
#     print(transpose([[1, 2], [3]]))
# except ValueError:
#     print("ValueError")
# print()


def row_sums(mat: list[list[float | int]]) -> list[float]:
    if not all(len(row) == len(mat[0]) for row in mat if mat):
        raise ValueError
    return [sum(row) for row in mat]


# print(row_sums([[1, 2, 3], [4, 5, 6]]))
# print(row_sums([[-1, 1], [10, -10]]))
# print(row_sums([[0, 0], [0, 0]]))
# try:
#     print(row_sums([[1, 2], [3]]))
# except ValueError:
#     print("ValueError")
# print()


def col_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat or not all(len(row) == len(mat[0]) for row in mat):
        raise ValueError
    num_cols = len(mat[0])
    return [sum(mat[r][c] for r in range(len(mat))) for c in range(num_cols)]


# print(col_sums([[1, 2, 3], [4, 5, 6]]))
# print(col_sums([[-1, 1], [10, -10]]))
# print(col_sums([[0, 0], [0, 0]]))
# try:
#     print(col_sums([[1, 2], [3]]))
# except ValueError:
#     print("ValueError")
