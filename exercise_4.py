from datetime import datetime

today = datetime.today().date()
print(today)

congratulation_list = []
users = [
    {"name": "John Doe", "birthday": "1985.01.25"},
    {"name": "Jane Smith", "birthday": "1990.01.26"}
]

for user in users:
    birthday_this_year = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
    if birthday_this_year.month <= today.month:
        if birthday_this_year.month == today.month and birthday_this_year.day <= today.day:
            pass
        else:
            next_congratulation = birthday_this_year.replace(year=today.year + 1)
            if next_congratulation.isoweekday() == 6 or next_congratulation.isoweekday() == 7:
                if next_congratulation.isoweekday() == 6:
                    print("6")
                    next_congratulation = next_congratulation.replace(day=next_congratulation.day + 2)
                else:
                    print("7")
                    next_congratulation = next_congratulation.replace(day=next_congratulation.day + 1)
    print(next_congratulation.isoweekday())
    congratulation_list.append(next_congratulation)
    print(congratulation_list)


