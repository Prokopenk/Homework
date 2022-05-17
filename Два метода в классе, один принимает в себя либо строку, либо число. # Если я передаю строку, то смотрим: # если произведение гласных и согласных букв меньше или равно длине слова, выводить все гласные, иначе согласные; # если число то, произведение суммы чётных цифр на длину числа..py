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

