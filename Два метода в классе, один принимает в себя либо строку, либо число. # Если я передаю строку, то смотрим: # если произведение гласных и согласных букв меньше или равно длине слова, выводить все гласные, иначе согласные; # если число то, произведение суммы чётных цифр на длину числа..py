# -------------------------------------------------------Суббота-----------------------------------
# Два метода в классе, один принимает в себя либо строку, либо число.
# Если я передаю строку, то смотрим:
# если произведение гласных и согласных букв меньше или равно длине слова, выводить все гласные, иначе согласные;
# если число то, произведение суммы чётных цифр на длину числа.
# Длину строки и числа искать во втором методе.
# import string
#
#
# class StrOrInt:
#     def __init__(self, obj: (int, str)) -> (int, str):
#         self.obj = obj
#         self.dlina = len(str(obj))
#
#     def rezult(self):
#         if isinstance(self.obj, int):
#             cumma = 0
#             for i in str(self.obj):
#                 if int(i) % 2 == 0:
#                     cumma += int(i)
#             print(self.dlina * cumma)
#         elif isinstance(self.obj, str):
#             gl = 0
#             sogl = 0
#             gl_letters = ''
#             sogl_letters = ''
#             for i in self.obj.lower():
#                 if i in 'eyuoia':
#                     gl += 1
#                     gl_letters += i
#                 elif i in string.ascii_lowercase:
#                     sogl += 1
#                     sogl_letters += i
#             if sogl * gl <= self.dlina:
#                 print(' '.join(gl_letters))
#             else:
#                 print(' '.join(sogl_letters))
#         else:
#             print(f'{self.obj} не является строкой или числом.')
#
#
# # Tests:
# str_1 = StrOrInt('wqertyqreuritqpuipausd')
# str_1.rezult()
# int_1 = StrOrInt(1234)
# int_1.rezult()
# list_1 = StrOrInt([1, 2, 3])
# list_1.rezult()

# --------------------------------------Воскресенье---------------------
# Класс Tomato:
# Создайте класс Tomato
# Создайте статическое свойство states, которое будет содержать все стадии созревания помидора
# Создайте метод __init__(), внутри которого будут определены два динамических protected свойства:
# 1) _index - передается параметром и 2) _state - принимает первое значение из словаря states
# Создайте метод grow(), который будет переводить томат на следующую стадию созревания
# Создайте метод is_ripe(), который будет проверять, что томат созрел (достиг последней стадии созревания)
# Класс TomatoBush
# Создайте класс TomatoBush
# Определите метод __init__(), который будет принимать в качестве параметра количество
# томатов и на его основе будет создавать список объектов класса Tomato. Данный список
# будет храниться внутри динамического свойства tomatoes.
# Создайте метод grow_all(), который будет переводить все объекты из списка томатов на следующий этап созревания
# Создайте метод all_are_ripe(), который будет возвращать True, если все томаты из списка стали спелыми
# Создайте метод give_away_all(), который будет чистить список томатов после сбора урожая
# Класс Gardener
# Создайте класс Gardener
# Создайте метод __init__(), внутри которого будут определены два динамических свойства:
# 1) name - передается параметром, является публичным и 2) _plant - принимает объект класса Tomato, является protected
# Создайте метод work(), который заставляет садовника работать, что позволяет растению становиться более зрелым
# Создайте метод harvest(), который проверяет, все ли плоды созрели.
# Если все - садовник собирает урожай. Если нет - метод печатает предупреждение.
# Создайте статический метод knowledge_base(), который выведет в консоль справку по садоводству.

# Тесты:
# Вызовите справку по садоводству
# Создайте объекты классов TomatoBush и Gardener
# Используя объект класса Gardener, поухаживайте за кустом с помидорами
# Попробуйте собрать урожай
# Если томаты еще не дозрели, продолжайте ухаживать за ними
# Соберите урожай

# class Tomato:
#     states = ['0%', '33%', '66%', '100%']
#
#     def __init__(self, index):
#         self._index = index
#         self._state = self.states[0]
#
#     def grow(self):
#         self._state = self.states[self.states.index(self._state) + 1]
#
#     def is_ripe(self):
#         if self._state == '100%':
#             return True
#         return False
#
#
# class TomatoBush:
#     def __init__(self, amount):
#         self.tomatoes = [Tomato(i) for i in range(amount)]
#
#     def grow_all(self):
#         return [tomat.grow() for tomat in self.tomatoes]
#
#     def all_are_ripe(self):
#         return all([tomat.is_ripe() for tomat in self.tomatoes])
#
#     def give_away_all(self):
#         self.tomatoes.clear()
#
#
# class Gardener:
#     def __init__(self, name, plant):
#         self.name = name
#         self._plant = plant
#
#     def work(self):
#         print('Садовник начал работу')
#         self._plant.grow_all()
#         print('Садовник закончил работу')
#
#     def harvest(self):
#         if self._plant.all_are_ripe():
#             print('Все помидоры созрели')
#             self._plant.give_away_all()
#         else:
#             print('Урожай еще не созрел')
#
#     @staticmethod
#     def knowledge_base():
#         print('Садовник, который умеет работать')
#
#
# Gardener.knowledge_base()
# tomato_bush = TomatoBush(13)
# gardener = Gardener('Paul', tomato_bush)
# gardener.work()
# gardener.work()
# gardener.harvest()
# gardener.work()
# gardener.harvest()
