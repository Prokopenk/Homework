# С клавиатуры вводится 7 значное число. Если четных цифр в нем больше, чем
# нечетных, то найти сумму всех его цифр, если нечетных больше, то найти
# произведение 1 3 и 6 цифры.
a = int(input('Введите семизначное число:'))

count_nechet = 0
count_chet = 0
cumma = 0
    for i in a:
         if i % 2 == 0:
          count_chet += 1
          cumma += i
      else:
          count_nechet += 1
         cumma += i

    if count_chet>count_nechet:
        print(f'Сумма всех цифр списка равна: {cumma}')
    elif count_nechet>count_chet:
        print(f'Произведение 1 3 и 6 элементов: {list_3[0]*list_3[2]*list_3[5]}')