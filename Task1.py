# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
import re
list = ['fvfvfdv', 'fdnbtrwwq', 'v7ryvf', 'fdv6fdh']

def FindNumber(array):
    for i in range(len(array)):
        num = re.findall(r'\d+', array[i])
        if num !=[]:
            return num

print(FindNumber(list))