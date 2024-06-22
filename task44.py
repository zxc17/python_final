"""
    Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
    Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?
"""
import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# TEST
print(pd.get_dummies(data['whoAmI']))
print()

# Вариант 1.
# data.loc[data['whoAmI'] == 'human', 'human'] = True
# data.loc[data['whoAmI'] != 'human', 'human'] = False
# data.loc[data['whoAmI'] == 'robot', 'robot'] = True
# data.loc[data['whoAmI'] != 'robot', 'robot'] = False
# data = data[['human', 'robot']]
# print(data)


# Вариант 2.
one_hot = pd.DataFrame({'human': data['whoAmI'] == 'human',
                        'robot': data['whoAmI'] == 'robot'})
print(one_hot)
