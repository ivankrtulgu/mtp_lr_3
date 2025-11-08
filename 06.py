class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            return "Ошибка: деление на ноль"
        return a / b

first_num = 4
second_num = 2
print("Сложение: ", MathUtils.add(first_num, second_num))
print("Вычитание: ", MathUtils.subtract(first_num, second_num))
print("Умножение: ", MathUtils.multiply(first_num, second_num))
print("Деление: ", MathUtils.divide(first_num, second_num))
