# задача 4. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))  

def nok(a,b):
    if a > b:
        num = a
    else:
        num = b 
    while(True):
        if (( num % a == 0 and num % b == 0)):
            c = num
            break
        num += 1
    return c
  
print("НОК чисел", a, "и", b, "является число:", nok(a,b))     