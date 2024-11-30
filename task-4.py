from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    greetings_users = []
    today = datetime.today().date()
    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year = today.year)

        if (birthday_this_year < today):
            birthday_this_year = birthday_this_year.replace(year = today.year + 1)

        days_before_birthday = (birthday_this_year - today).days

        if days_before_birthday <= 6:
            congratulation_date = birthday_this_year

            if congratulation_date.weekday() > 4:
                congratulation_date += timedelta(days=(7 - congratulation_date.weekday()))
             
            greetings_users.append({
                    "name": user["name"],
                    "congratulation_date": congratulation_date.strftime('%Y.%m.%d'),
                })    
    return greetings_users

users = [
    {"name": "Corben Dallas", "birthday": "1985.12.1"},
    {"name": "John Doe", "birthday": "1985.11.30"},
    {"name": "Jane Smith", "birthday": "1990.12.03"},
    {"name": "Harry Potter", "birthday": "1990.12.02"},
    {"name": "Luce Skywalker", "birthday": "1990.12.08"},
    {"name": "Jack Richard", "birthday": "1990.07.14"}
]

print(get_upcoming_birthdays(users))