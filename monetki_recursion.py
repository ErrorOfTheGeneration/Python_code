print ("Введите сдачу: ")
x = int(input()) # х - сдача
y = 0 # y - кол-во монет, данное на сдачу

def cd(x, y):
    if x == 0:
        return print(y)
    if x >= 50:
        x = x - 50
        y = y + 1
        cd (x, y)
    else:
        if x >= 10:
            x = x - 10
            y = y + 1
            cd (x, y)
        else:
            if x >= 5:
               x = x - 5
               y = y + 1
               cd(x, y)
            else:
                x >= 1
                x = x - 1
                y = y +1
                cd(x,y)


print("кол-во монет: ")
cd (x, y)