import datetime

def input_function():
    input_date = input('Введите дату формата ГГГГ-ММ-ДД: ')
    return input_date
    
def get_days_from_today(input_date_param):
    try:
        date = datetime.datetime.fromisoformat(input_date_param).date()
    except Exception as error:
        print(error)
        print("Введено неверные данные")
        return

    current_date = datetime.datetime.today().date()
    # Использование метода toordinal для вычетания одной даты от другой
    output_date = current_date.toordinal() - date.toordinal()
    print(f"Между датами прошло {output_date} дня")
    return output_date

input_date = input_function()
print(type(input_date))
get_days_from_today(input_date)