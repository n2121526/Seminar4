# задача 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
def spisok_pr(n):
   i = 2
   res = []
   while i * i <= n:
       while n % i == 0:
           res.append(i)
           n = n // i
       i = i + 1
   if n > 1:
       res.append(n)
   return res

n = int(input("Задайте натуральное число N: "))
print(spisok_pr(n))