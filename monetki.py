print ("введите сдачу: ")
x = int(input()) #х - сдача
y = 0 #y - количество выданных монет
while x >= 50:
    x = x - 50
    y = y + 1
while x >= 10:
    x = x - 10
    y = y + 1
while x >= 5:
    x = x - 5
    y = y + 1
while x >= 1:
    x = x - 1
    y = y + 1
print("кол-во монет: ")
print (y)


