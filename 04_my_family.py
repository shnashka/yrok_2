#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ["ама", "папа", "я"]


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    [my_family[0], 110],
    [my_family[1], 120],
    [my_family[2], 130]
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print('Рост отца - {} см'.format(my_family_height[1][1]))
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
Pizdek = my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1]
print('Общий рост моего отчаиния - {} см'.format(Pizdek))
