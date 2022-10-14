import random

def rndom(k):
    return [random.randint(0, 100) for i in range(k + 1)]

def get_string(k, polynomial):
    string = ""
    for i in range(k, -1, -1):
        if i == 0:
            string += str(polynomial[i])
        elif i == 1:
            string += str(polynomial[i]) + "*x + "
        else:
            string += str(polynomial[i]) + "*x^" + str(i) + " + "
    string += " = 0"
    return string

def polynom():
    k = int(input("Введите натуральную степень k = "))
    polynomial = rndom(k)
    string = get_string(k, polynomial)
    print(string)
    with open('Polynomial.txt', 'w') as file:
        file.write(string)    

polynom()

