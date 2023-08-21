# 📌Создайте класс Матрица.
# Добавьте методы для:
# ○вывода на печать,
# ○сравнения,
# ○сложения,
# ○*умножения матриц

class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

    def __eq__(self, other):
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise ValueError(f"Ошибка! Переданы матрицы {len(self.data)}х{len(self.data[0])} и {len(other.data)}х{len(other.data[0])} \
для сравнения матрицы должны быть одного размера")
        logic_result = True
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                logic_result = logic_result and (self.data[i][j] == other.data[i][j])

        return logic_result

    def __add__(self, other):
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise ValueError(f"Ошибка! Переданы матрицы {len(self.data)}х{len(self.data[0])} и {len(other.data)}х{len(other.data[0])} \
для сложения матрицы должны быть одного размера")

        result_data = []
        for i in range(len(self.data)):
            row = [self.data[i][j] + other.data[i][j] for j in range(len(self.data[0]))]
            result_data.append(row)

        return Matrix(result_data)

    def __mul__(self, other):
        if len(self.data[0]) != len(other.data):
            raise ValueError(f"Ошибка! Переданы матрицы {len(self.data)}х{len(self.data[0])} и {len(other.data)}х{len(other.data[0])} \
для умножения Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы")


        result_data = []
        for i in range(len(self.data)):
            row = []
            for j in range(len(other.data[0])):
                element = sum(self.data[i][k] * other.data[k][j] for k in range(len(self.data[0])))
                row.append(element)
            result_data.append(row)

        return Matrix(result_data)


# Создаем матрицы
matrix1 = Matrix([[1, 2, 3], [3, 4, 3]])
matrix2 = Matrix([[1, 2, 3], [3, 4, 3]])
matrix3 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix4 = Matrix([[1, 2], [3, 4], [5, 7]])

#сложение матриц
result_add = matrix1 + matrix2
print("Сложение матриц:")
print(result_add)

#умножение матриц
result_mul = matrix1 * matrix3
print("Умножение матриц:")
print(result_mul)

#сравнение матриц
print(matrix1 == matrix2)
print(matrix3 == matrix4)

# #сложение матриц
# result_add = matrix1 + matrix3
# print("Сложение матриц:")
# print(result_add)

#умножение матриц
result_mul = matrix1 * matrix2
print("Умножение матриц:")
print(result_mul)


