# задача 2 . Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
def new_list(n):
    new_lst = []
    for i in n:
        if i not in new_lst:
            new_lst.append(i)
    return new_lst 


first_list = list(map(int, input("Введите числа через пробел:\n").split()))
print(f"Исходный список: {first_list}")
n_list= new_list(first_list)
print(f"Список из неповторяющихся элементов: {n_list}")