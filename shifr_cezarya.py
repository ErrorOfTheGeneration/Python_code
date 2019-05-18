# ci = (pi + k) % 33
#shifr[i] = (your_text[i] + k) % 33
import re #подключение библиотеки для поиска совпадений
your_text = input('введите ваш текст: ')
k = int(input('введите ключ: '))
shifr = ''
str= 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
for i in range(len(your_text)): #len - функция которая считает кол-во символов в моем тексте
    if re.search(your_text[i], str) and your_text[i] != '.': #если это буква
        for j in range(len(str)):
            if str[j] == your_text[i]:
                break
        index = (j + k) % 33 #index - переменная, которая показывает порядковый номер буквы алфавита
        shifr = shifr + str[index]
    else:
        shifr = shifr + your_text[i]
print(shifr)