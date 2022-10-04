#  Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

n = int(input('Введите целое положительное число: '))

def fibon(n):
    fibon_series = []
    a, b = 1, 1
    for i in range(n):
        fibon_series.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (n+1):
        fibon_series.insert(0, a)
        a, b = b, a - b
    return fibon_series

fibon_series = fibon(n)
print(fibon(n))