a = int(input())
b = int(input())
c = int(input())
d = b ** 2 - 4 * a * c
if a != 0:
    if d > 0: #уравнение имеет два корня
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        print(x1, x2)
    elif d == 0: #уравнение имеет один корень
        x = -b / (2 * a)
        print(x)
    else:
        print('Уравнение не имеет корней')
else:
    x = -c / b
    print(x)