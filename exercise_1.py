import datetime

def input_function():
    while True: # Цикл с обработкой ошибок, для ввода коректныъ данных
        try:
            input_date = datetime.datetime.fromisoformat(input('Введите дату формата ГГГГ-ММ-ДД: '))
            break
        except ValueError:
            print('Пожалуйста введите правильный формат даты')
    return input_date

def get_days_from_today(input_date_param):
    current_date = datetime.datetime.today()
    # Использование метода toordinal для вычетания одной даты от другой
    output_date = current_date.toordinal() - input_date_param.toordinal()
    print(f"Между датами прошло {output_date} дня")
    return output_date

get_days_from_today(input_function()) 