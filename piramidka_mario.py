print("height:")
x = int(input())
while x > 1 and x < 23:
    for i in range(x):
        print(' ' * (x - i - 1), '#' * (i + 2))
    break