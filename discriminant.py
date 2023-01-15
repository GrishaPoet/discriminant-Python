a = int(input('Введите число: (a) '))
b = int(input('Введите число: (b) '))
c = int(input('Введите число: (c) '))

def discriminant(): 
    D = int((b)**2 - 4*a*c)
    print(D)

discriminant()
