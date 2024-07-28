from random import randint


def create_matrix(x: int, y: int) -> list:
    return [[randint(-99, 99) for _ in range(x)] for _ in range(y)]


def matrix_addition(m1: list, m2: list) -> list:
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        # result: list = []
        # for i in range(len(m1)):
        #     result.append([])
        #     for k in range(len(m1[0])):
        #         result[i].append(m1[i][k] + m2[i][k])
        # return result
        return [
            [m1[i][k] + m2[i][k] for k in range(len(m1[0]))] for i in range(len(m1))
        ]
    return "Нельзя сложить матрицы разной длины"


m1 = create_matrix(2, 5)
m2 = create_matrix(2, 5)

print(m1, m2, sep="\n\n", end="\n\n")

print(matrix_addition(m1, m2))
