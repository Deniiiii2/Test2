ru = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЭЮЯ'*1000000
eu = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'*10000000
message=input('Введите текст ЗАГЛАВНЫМИ буквами Русского или Английского алфавита: ')
lang=input('Введите язык RU или EU: ')
number=int(input('Введите шаг сдвига (не более 10000) '))
d = ''
if lang == 'RU':
    for i in message:
        place=ru.find(i)
        new=place+number
        if i in ru:
            d+=ru[new]
        else:
            d+=i
else:
    for i in message:
        place=eu.find(i)
        new=place+number
        if i in eu:
            d+=eu[new]
        else:
            d+=i
print(d)
