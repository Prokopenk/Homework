#Посчитать, сколько пар (стоят рядом) верхнего и нижнего регистра находится в
#веденном с клавиатуры слове. (Пример HjkLM- 1 пара нижнего, 1 пара верхнего), а
#также сколько всего букв в слове, сколько гласных и согласных.

text = 'HjkzLM'
pair_lower = 0
pair_upper = 0
for i in range(1, len(text)):
    print(text[i - 1], text[i])
    if text[i - 1].islower() and text[i].islower():
        pair_lower += 1
    if text[i - 1].isupper() and text[i].isupper():
        pair_upper += 1
print('сколько пар (стоят рядом) верхнего регистра:', pair_upper)
print('сколько пар (стоят рядом) нижнего регистра:', pair_lower)
