# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c —
# стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой
# двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника
# с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним,
# равнобедренным или равносторонним.

class DataException(Exception):
    def __init__(self, a, b, c):
        self.side_a = a
        self.side_b = b
        self.side_c = c

    def __str__(self):
        return f'треугольник со сторонами {self.side_a}, {self.side_b}, {self.side_c} не может существовать'


class DataTypeError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'введен параметр неверного типа : {type(self.value)}'


class Triangle:
    def __init__(self, a, b, c):
        if not isinstance(a, (int, float)) or a < 0:
            raise DataTypeError(a)
        if not isinstance(b, (int, float)) or b < 0:
            raise DataTypeError(b)
        if not isinstance(c, (int, float)) or c < 0:
            raise DataTypeError(c)

        if a >= b + c or b >= a + c or c >= b + a:
            raise DataException(a, b, c)
        else:
            self.side_a = a
            self.side_b = b
            self.side_c = c

    def type_check(self):
        result = f"треугольник со сторонами {self.side_a}, {self.side_b}, {self.side_c} существует"
        if self.side_a == self.side_b == self.side_c:
            result += f'и является равносторонним'
        elif self.side_a == self.side_b or self.side_a == self.side_c or self.side_c == self.side_b:
            result += f' и является равнобедренным'

        return result


print("введите стороны треугольника а, b, c")

side_a = 1
side_b = 5
side_c = "s"

tri = Triangle(side_a, side_b, side_c)
print(tri.type_check())
