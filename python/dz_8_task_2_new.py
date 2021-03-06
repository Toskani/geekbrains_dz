"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в
качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class Division:
    def __init__(self, a, b):
        self.a = a
        self.b = b


def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return f"Нельзя делить на 0"


my_div = Division(0, 0)
#  Тут хотел уточнить, не до конца понимаю где можно пусто указать,
# а где нужно хотя бы какие-либо значения. Имею ввиду вот так ().
print(div(10, 0))
print(div(10, 1))
