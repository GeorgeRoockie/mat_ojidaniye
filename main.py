from scipy.integrate import quad
import math

class Calculate:
    @staticmethod
    def calculate_expected_value(values, probabilities): #мат ожидание
        if len(values) != len(probabilities):
            raise ValueError('Количество значений и вероятностей должно быть одинаковым')

        expected_value = sum(i * j for i, j in zip(values, probabilities))
        return expected_value

    @staticmethod
    def pdf_function(x): #плотность вероятности
        return 2 * x

    @staticmethod
    def continuous_expected_value(pdf_function, lower_limit, upper_limit): #для непрерывной случайной величины
        result, _ = quad(lambda x: pdf_function * Calculate.pdf_function(x), lower_limit, upper_limit)
        return result

    @staticmethod
    def calculate_variance(values): #дисперсия
        n = len(values)
        mean = sum(values) / n
        variance = sum((x - mean) ** 2 for x in values) / (n - 1)
        return variance

    @staticmethod
    def calculate_standard_deviation(values): #ср квадр откл
        n = len(values)
        mean = sum(values) / n
        variance = sum((x - mean) ** 2 for x in values) / (n - 1)
        standard_deviation = math.sqrt(variance)
        return standard_deviation


user = Calculate()
while True:
    ans = input('Введите номер того, что хотите найти:\n1 - Математическое ожидание\n2 - Непрерывная СВ\n3 - Дисперсия\n4 - Среднее квадратическое отклонение\n')
    if ans == '1':
        print('Введите список значений через пробел:\n')
        values = (int(i) for i in input().split())
        print('Введите список вероятностей этих значений через пробел:\n')
        probabilities = (int(i) for i in input().split())
        print('Математическое ожидание = ', user.calculate_expected_value(values, probabilities))
        continue
    if ans == '2':
        print('Введите нижний и верхний пределы:\n')
        lower_limit, upper_limit = int(input('Нижний: ')), int(input('Верхний: '))
        print('Введите плотность вероятности:\n')
        x = int(input())
        print('Непрерывная СВ = ', user.continuous_expected_value(x, lower_limit, upper_limit))
        continue
    if ans == '3':
        print('Введите список значений через пробел:\n')
        values = (int(i) for i in input().split())
        print('Дисперсия = ', user.calculate_variance(values))
        continue
    if ans == '4':
        print('Введите список значений через пробел:\n')
        values = (int(i) for i in input().split())
        print('Среднее квадратическое отклонение = ', user.calculate_standard_deviation(values))
