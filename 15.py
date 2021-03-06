while True:
    try:
        n = int(input("Задайте размер поля (введите 3 или 4): "))
        if n == 3 or n == 4:
            break
        else:
            print ("Ошибка.")
    except (TypeError, ValueError):
        print("Введи целое число.")

massiv = []
def init ():
    if n == 4:
        v = 15 #v - числа в пятнашках
    else:
        v = 8
    for i in range(n): #i строчки
        massiv.append([])
        for j in range (n): #j столбцы
            massiv [i].append (v)
            v = v - 1
    if n == 4:
        massiv[3][1], massiv[3][2] = massiv[3][2],massiv[3][1]

def draw():
    for i in range (n):
        for j in range(n):
            if massiv[i][j] == 0:
                print('_ ', " ", end = '')
            elif massiv[i][j] >= 1 and massiv[i][j] <= 9:
                print(massiv[i][j], '  ', end = '')
            else:
                print(massiv[i][j], ' ', end = '')
        print('\n')
init()
draw()

def move():
    step = input('нажмите клавишу для перемещения: ')
    for i in range(n):
        for j in range(n):
            if massiv[i][j] == 0:
                break
        if massiv[i][j] == 0:
            break
    if step == 's':
        if i > 0:
            massiv[i][j],massiv[i-1][j] = massiv[i-1][j],massiv[i][j]
    elif step == 'w':
        if i < n - 1:
            massiv[i][j], massiv[i + 1][j] = massiv[i + 1][j], massiv[i][j]
    elif step == 'a':
        if j < n - 1:
            massiv[i][j], massiv[i][j + 1] = massiv[i][j + 1], massiv[i][j]
    elif step == 'd':
        if j > 0:
            massiv[i][j], massiv[i][j - 1] = massiv[i][j - 1], massiv[i][j]

def won():
    f = 1
    v = 0
    for i in range(n):
        for j in range(n):
            v = v + 1
            if i == n - 1 and j == n - 1:
                v = 0
            if massiv[i][j] != v:
                f = 0
    if f == 1:
        print('Вы выиграли.')
    return f

while True:
    move()
    draw()
    if won() == 1:
        break
