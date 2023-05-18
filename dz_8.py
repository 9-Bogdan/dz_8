from datetime import datetime, timedelta
"""
Потрібно дивитись чи збігається теперішні місяць і дата з вказаними значеннями словника
Якщо так то виводимо привітання
Також якщо дата народження входить в межі +тиждень теж виводимо
Тиждень починається з понеділка

"""


def get_birthdays_per_week(users):
    greet_dict = {}
    time_now = datetime.now()
    for i in users:
        birthday_date = i['birthday']
        one_weeks_interval = timedelta(weeks=1)
        time_plus_one_week = time_now + one_weeks_interval
        if (time_plus_one_week.day - birthday_date.day in range(1, 8)) and (time_plus_one_week.month - birthday_date.month == 0):
            name = i['name']
            this_year_bd = datetime(
                year=time_now.year, month=birthday_date.month, day=birthday_date.day)
            if this_year_bd.weekday() == 5:
                two_days_plus = timedelta(days=2)
                greet_day = this_year_bd + two_days_plus
                format_greet_day = datetime.strftime(greet_day, "%A")
                if not format_greet_day in greet_dict:
                    greet_dict[format_greet_day] = name
                else:
                    greet_dict[format_greet_day] += f", {name}"
            elif this_year_bd.weekday() == 6:
                one_day_plus = timedelta(days=1)
                greet_day = this_year_bd + one_day_plus
                format_greet_day = datetime.strftime(greet_day, "%A")
                if not format_greet_day in greet_dict:
                    greet_dict[format_greet_day] = {name}
                else:
                    greet_dict[format_greet_day] += f", {name}"
            else:
                greet_day = datetime.strftime(this_year_bd, "%A")
                if not greet_day in greet_dict:
                    greet_dict[greet_day] = name
                else:
                    greet_dict[greet_day] += f", {name}"
    for k, v in greet_dict.items():
        print(f"{k}: {v}")


users = [
    {'name': "Noname_1", 'birthday': datetime(year=2002, month=2, day=21)},
    {'name': "Noname_2", 'birthday': datetime(year=1999, month=9, day=15)},
    {'name': "Noname_3", 'birthday': datetime(year=1998, month=3, day=18)},
    {'name': "Noname_4", 'birthday': datetime(year=1969, month=9, day=15)},
    {'name': "Noname_5", 'birthday': datetime(year=1969, month=3, day=16)},
    {'name': "Noname_6", 'birthday': datetime(year=2002, month=6, day=2)},
    {'name': "Noname_7", 'birthday': datetime(year=2002, month=5, day=23)},
    {'name': "Noname_8", 'birthday': datetime(year=2002, month=5, day=20)},
    {'name': "Noname_9", 'birthday': datetime(year=2002, month=5, day=20)},
    {'name': "Noname_10", 'birthday': datetime(year=2002, month=5, day=21)},
    {'name': "Noname_11", 'birthday': datetime(year=2002, month=5, day=24)},
]
get_birthdays_per_week(users)
