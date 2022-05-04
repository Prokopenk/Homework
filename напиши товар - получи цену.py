tovar1 = (input('Введите название товара1:'))
tovar2 = (input('Введите название товара2:'))
kol1 = (input('Введите количество товара1:'))
kol2 = (input('Введите количество товара2:'))
Cena1 = 10
Cena2 = 14
Product = {'tovar1': [kol1, 10],'tovar2': [kol2, 14]}
print("tovar1",'-',Product['tovar1'][0],"-",Product['tovar1'][1],
      'rublei','-','tovar2','-',Product['tovar2'][0],"-"
      ,Product['tovar2'][1],'rublei')
print('Цена всех товаров',Cena1+Cena2)
print('Количество товаров', len(Product))
