from datetime import datetime, timedelta

users = [
    {"name": "Roman", "birthday": "26 July 2002"},
    {"name": "Karina", "birthday": "10 May 1994"},
    {"name": "Liliya", "birthday": "29 May 1974"},
    {"name": "Alexander", "birthday": "3 February 1990"},
]


def get_birthdays_per_week(users):
    start = datetime.now().date()
    end = start + timedelta(days=7)
    for i in users:
        birthday = datetime.strptime(i["birthday"], "%d %B %Y")
        date_b = datetime(start.year, birthday.month, birthday.day)
        if start <= date_b.date() <= end:
            day = date_b.weekday()
            if day == 0:
                print("Monday: " + i["name"])
            if day == 1:
                print("Tuesday: ", +i["name"])
            if day == 2:
                print("Wednesday: " + i["name"])
            if day == 3:
                print("Thursday: " + i["name"])
            if day == 4:
                print("Friday: " + i["name"])
            if day in (5, 6):
                print('Next Monday: ' + i['name'])
            if day not in (0, 1, 2, 3, 4, 5, 6):
                print("No birthday in this week")


get_birthdays_per_week(users)