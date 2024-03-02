import random

min_number, max_number, quantity_number = 0, 0, 0

while True:
    try:

        if  min_number and min_number > 0:
            pass
        else:
            min_number = int(input("Введите минимальное число больше 0: "))
            continue
        if max_number and min_number < max_number < 1001:
            pass
        else:    
            max_number = int(input("Введите максимальное число не больше 1000: "))
            continue
        if quantity_number and min_number <= quantity_number <= max_number :
            pass
        else:    
            quantity_number = int(input("Введите количество выпадающих чисел: "))
            continue
        break
    except ValueError:
        print("Ввелите коректные данные")
        continue
number_list = []
def get_numbers_ticket(min_number, max_number, quantity_number):
    while quantity_number > 0:
        random_number = random.randint(min_number, max_number)
        if random_number in number_list:
            continue
        else:
            number_list.append(random_number)
            quantity_number -= 1

get_numbers_ticket(min_number, max_number, quantity_number)
print(sorted(number_list))

    