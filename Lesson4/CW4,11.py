a = input()
b = int(input())
c = float(input())
strenght = b * 1.5
gold_tax = c * 0.9
title = a + '-' + a + '-' + a
print(f'\nИтоговая карточка\nТитул: {title}\nСила: {strenght}\nЗолото после налога: {gold_tax}\nДлина имени: {len(a)}')