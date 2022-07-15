#Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
list= ["qwe", "asd", "zxc", "qwe", "ertqwe"]

def SecondEntry(list):
    for i in range(len(list)):
        for a in range(len(list)):
            if list[i] ==list[a] and i != a:
                return a

if SecondEntry(list) == None: #не нашел способ как вывести что второго вхождения нет кроме этого способа :(
    print ('Все строки в списке уникальны')
else:
    print(SecondEntry(list))