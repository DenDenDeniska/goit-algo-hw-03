import random

min_number, max_number, quantity_number = 0, 0, 0 #Инициализация переменных

while True: # Цикл с обопботкой ошибок что бы вводились правильные значения
    try:

        if  min_number and min_number > 0: # Проверяем существует ли минимальное число
            pass
        else:
            min_number = int(input("Введите минимальное число больше 0: "))
            continue
        if max_number and max_number < 1001: # Проверяем существует ли максисальное число и меньше ли оно 1001 по условию
            pass
        else:    
            max_number = int(input("Введите максимальное число не больше 1000: "))
            continue
        if quantity_number: # Существует ли кол-во выбираемых чисел
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
    if min_number >= max_number or max_number - min_number < quantity_number: # Если данные не соответствуют условию задачи то возвращаем пустой список
        return number_list
    
    while quantity_number > 0: # Пока кол-во выпадающих значенмй не 0 выполняем цикл
        random_number = random.randint(min_number, max_number) # Получаем случайное число
        if random_number in number_list: # Если случайное число есть в списке идем к след. итерации
            continue
        else:
            number_list.append(random_number) # Если числа в списке нет, то мы его добавляем в список
            quantity_number -= 1
    return sorted(number_list) # Функцией sorted сортируем список

print(get_numbers_ticket(min_number, max_number, quantity_number))