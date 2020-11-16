"""
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на
наличие только чисел. Проверить работу исключения на реальном примере. Необходимо запрашивать
у пользователя данные и заполнять список. Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не
остановит работу скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный
список выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. При вводе
пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число) и
отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.
"""


class List:
    def __init__(self):
        self.my_list = []

    def my_input(self):

        while True:
            try:
                val = int(input('Введите число: '))
                self.my_list.append(val)
            except ValueError:
                stopper = input(f'Ошибка! Введите число или stop для завершения: ')

                if stopper.lower() == 'stop':
                    return f'Вы вышли. Итоговый спискок: {self.my_list}'


for_work = List()
print(for_work.my_input())
