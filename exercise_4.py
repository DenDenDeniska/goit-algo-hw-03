from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.03.09"},
    {"name": "Jane Smith", "birthday": "1990.03.04"}
]

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    # Инициализация пустых списков
    next_year_congratulation_list = []
    congratulation_list = []
    for user in users: # Выбираем из списка определенного пользователя
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date() # Приводим строку даты рождения к типу datetime
        birthday = birthday.replace(year=today.year) # Заменяем год рождения на текущий год
        if 0 <= birthday.toordinal() - today.toordinal() <= 7: # Если день рождения будет в течении недели продолжаем выполнение программы
            day = birthday
            if birthday.isoweekday() == 6: # Если день рождение припадает на субботу то приплюсовываем 2, что бы поздравить в понедельник
                day = birthday + timedelta(days=2)
            if birthday.isoweekday() == 7: # Если день рождение припадает на воскресенье то приплюсовываем 1, что бы поздравить в понедельник
                day = birthday + timedelta(days=1)
            congratulation_list.append({"name": {user["name"]}, "congratulation": day.strftime("%Y.%m.%d")}) # Добавляем в список поздравления пользователя
        elif birthday.toordinal() - today.toordinal() < 0: # Если день рождения уже прошел
            next_year_congratulation_list.append({"name": user["name"], "birthday": birthday.strftime("%Y.%m.%d")}) # То добавляем поздравление пользователя в список на след год
    return congratulation_list

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список поздравлений на этой неделе:", upcoming_birthdays, end="\n")