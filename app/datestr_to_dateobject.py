import time, datetime


def date_string_to_date_object(date_str):
    t = time.strptime(date_str, "%Y-%m-%d")
    y,m,d = t[0:3]
    return datetime.date(y, m, d)
