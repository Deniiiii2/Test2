# Создаем алфавит
ru = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЭЮЯ'*1000000
eu = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'*10000000
message=input('Введите текст ЗАГЛАВНЫМИ буквами Русского или Английского алфавита: ')
lang=input('Введите язык RU или EU: ')
number=int(input('Введите шаг сдвига (не более 1000000) ')) #Создаем переменную с шагом шифровки
d = '' #создаем переменную для вывода итогового сообщения
if lang == 'RU':
    for i in message:
        place=ru.find(i) #Вычисляем места символов в списке
        new=place+number #Сдвигаем символы на указанный в переменной smeshenie шаг
        if i in ru:
            d+=ru[new] # Задаем значения в итог
               else:
            d+=i
else: #аналогично для другого языка
    for i in message:
        place=eu.find(i)
        new=place+number
        if i in eu:
            d+=eu[new]
        else:
            d+=i
print(d)  #Строка вывода
