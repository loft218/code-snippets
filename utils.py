#-*-coding:utf-8-*-

import calendar
import datetime
import time


def add_months(dt, months):
    month = dt.month - 1 + months
    year = int(dt.year + month / 12)
    month = month % 12 + 1
    day = min(dt.day, calendar.monthrange(year, month)[1])
    return dt.replace(year=year, month=month, day=day)


def date2utc(date):
    return datetime.datetime.utcfromtimestamp(time.mktime(date.timetuple()))
    
def date2uts(date):
    return time.mktime(date.timetuple())

def date_month_range(start_date, end_date):
    for n in range(month_differ(start_date, end_date)):
        yield add_months(start_date, n)

def month_differ(date1, date2):
    return abs((date1.year - date2.year) * 12 +
               (date1.month - date2.month) * 1)
               
def unix_now():
    '''
      当前unix时间
    '''
    return int(time.time())

def timestamp_from_objectid(objectid):
    result = 0
    try:
        result = int(time.mktime(objectid.generation_time.timetuple())) + 28800 #+8小时
    except:
        pass
    return result


if __name__ == '__main__':
    _date = add_months(datetime.date(2017, 8, 31), 1)
    print(_date)
