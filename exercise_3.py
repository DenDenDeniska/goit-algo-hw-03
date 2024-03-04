import re

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def normalize_phone(num):
    pattern = r"\+?\d+" # Патерн для нахождения номеров, есть или нету "+" плюс лобое кол-во чисел
    result = re.findall(pattern, num)
    new_result = "".join(result) # Склеиваем из списка найденные числа
    if re.fullmatch(r"\+38\d+", new_result): # Если номер начинается с "+38" ничего делать не нужно, номер уже нормализирован
        pass
    elif re.fullmatch(r"38\d+", new_result): # ЕСли номер начинается с "38" нужно добавить "+" перед номером
        new_result = "+" + new_result
    else: # Во всех остальных случаях к номеру прибавляем "+38"
        new_result = "+38" + new_result
    return new_result

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)