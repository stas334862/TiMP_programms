print('Ноль в качестве знака операции завершит работу программы')
while True:
    s = input("Знак (&,|,^,~): ")
    if s == '0': break
    if s in ('&','|','^','~'):
        x = int(input("Введите двоичное число x= "), 2)
        y = int(input("Введите двоичное число y= "), 2)
        if s == '&':
           print(bin(x & y))
        elif s == '|':
           print(bin(x | y))
        elif s == '^':
            print(bin(x ^ y))
        elif s == '~':
            print("Инверсия числа х:", bin(~x))
            print("Инверсия числа y:", bin(~y))
    else:
       print("Неверный знак операции!")