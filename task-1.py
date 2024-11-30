from datetime import datetime

def get_days_from_today(date):
    date_time = datetime.strptime(date, "%Y-%m-%d")
    date_now = datetime.today()
    days = (date_time - date_now).days
    return days


get_days_from_today("2021-10-09")

