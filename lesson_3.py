# Упражнение 3: Написать класс собственного исключения и использовать его в примере кода:
#
# Задание: Создать класс NegativeNumberError, который будет генерироваться, если переданное число отрицательное.
# Использовать это исключение в функции check_positive_number.
#
# Пошаговая инструкция:
# Создайте класс NegativeNumberError, наследующий от Exception.
# Переопределите конструктор, чтобы принимать значение числа и сообщение об ошибке.
# Переопределите метод __str__, чтобы возвращать информативное сообщение.
# Создайте функцию check_positive_number, которая проверяет, является ли число положительным.
# Если число отрицательное, функция должна вызывать исключение NegativeNumberError.
#
# Проверка:
# Протестируйте функцию с отрицательным числом.
# Протестируйте функцию с положительным числом.
# Убедитесь, что исключение NegativeNumberError правильно обрабатывается и выводит информативное сообщение.

class NegativeNumberError(Exception):

    def __init__(self, number):
        self.number = number
        super().__init__()

    def __str__(self):
        return f"NegativeNumberError: Число не должно быть отрицательным! (получено: {self.number})"


def check_positive_number(number):
    if number < 0: raise NegativeNumberError(number)
    print(f"Число {number} прошло проверку на положительность")


check_positive_number(10)
check_positive_number(-10)
