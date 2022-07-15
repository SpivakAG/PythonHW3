# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
import re
list = ['fvfvfdv', 'fdnbtrwwq', 'v7ryvf', 'fdv6fdh']

for i in range(len(list)):
    num = re.findall(r'\d+', list[i])
    if num !=[]:
        print(num)