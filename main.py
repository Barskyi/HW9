from datetime import date, timedelta


def get_birthdays_per_week(users):
    today = date.today()  # Отримуємо поточну дату
    next_week = today + timedelta(days=7)  # Обчислюємо дату через тиждень
    weekdays = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
    }  # Словник з номерацією днів тижня та відповідними назвами днів
    birthday_week = {day: [] for day in weekdays.values()}  # Створюємо словник для зберігання днів народження за днями тижня

    for user in users:
        # Встановлюємо поточний рік для дня народження користувача
        birthday = user["birthday"].replace(year=today.year)
        if birthday < today:  # Якщо день народження вже минув у поточному році
            # Встановлюємо наступний рік
            birthday = birthday.replace(year=today.year + 1)

        # Перевіряємо, чи день народження потрапляє у вікно наступного тижня
        if today <= birthday <= next_week:
            day_name = weekdays[birthday.weekday()]  # Отримуємо назву дня тижня для дня народження
            birthday_week[day_name].append(user["name"])  # Додаємо ім'я користувача до списку імен відповідного дня тижня

    # Враховуємо вихідні дні
    if birthday_week["Saturday"]:
        # Переносимо імена з суботи на понеділок
        birthday_week["Monday"] += birthday_week["Saturday"]
        del birthday_week["Saturday"]
    if birthday_week["Sunday"]:
        # Переносимо імена з неділі на понеділок
        birthday_week["Monday"] += birthday_week["Sunday"]
        del birthday_week["Sunday"]

    return {day: names for day, names in birthday_week.items() if names}


# Приклад списку користувачів із їхніми датами народження
users = [
    {"name": "Taras", "birthday": date(1990, 7, 21)},
    {"name": "Olenka", "birthday": date(1993, 1, 31)},
    {"name": "Artem", "birthday": date(2019, 1, 13)},
    {"name": "Mark", "birthday": date(2022, 9, 29)},
    {"name": "Vasil", "birthday": date(1963, 1, 13)},
    {"name": "Svitlana", "birthday": date(1964, 8, 19)},
]

# Отримання словника з днями народження на наступному тижні
birthdays_per_week = get_birthdays_per_week(users)

# Вивід результатів
print(birthdays_per_week)
