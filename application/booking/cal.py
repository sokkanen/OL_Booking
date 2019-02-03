
import calendar
from datetime import datetime, date
from calendar import monthrange

class Month_And_Year:
    def __init__(self):
        self.year = datetime.now().year
        self.month = datetime.now().month

    def previous_month(self):
        if self.month == 1:
            self.year -=1
            self.month = 12
        else:
            self.month -=1

    def next_month(self):
        if self.month == 12:
            self.year +=1
            self.month = 1
        else:
            self.month +=1

    def get_month(self):
        return self.month

    def get_year(self):
        return self.year

    def now(self):
        self.month = datetime.now().month
        self.year = datetime.now().year

class First_And_Last:
    def __init__(self, year, month):
        self.my = Month_And_Year()
        self.first = datetime.today().replace(year=year).replace(month=month).replace(day=1).replace(hour=00).replace(minute=00).replace(second=00)
        self.last = datetime.today().replace(year=year).replace(month=month).replace(day=monthrange(self.my.get_year(), self.my.get_month())[1]).replace(hour=23).replace(minute=59)

    def plus_one(self):
        self.first.month + 1

    def minus_one(self):
        self.first.month + 1

    def get_first(self):
        return self.first

    def get_last(self):
        return self.last
