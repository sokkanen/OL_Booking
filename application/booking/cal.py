
import calendar
from datetime import datetime, date
from calendar import monthrange
from application.booking.models import Booking

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

class Days_of_the_Month():
    def __init__(self,year, month):
        self.year = year
        self.month = month
        self.my = First_And_Last(year, month)

    def get_days(self):
        first = self.my.get_first()
        last = self.my.get_last()
        lst = []
        books = Booking.find_bookings_with_workers_and_duration(first, last)
        for week in list(calendar.monthcalendar(self.year, self.month)):
            newweek = []
            for day in week:
                newday = []
                d = str(day)
                if len(d) == 1:
                    d = '0' + d
                newday.append(d)
                for book in books:
                    if str(day) == book[0]:
                        if (book[1] == None):
                            newday.append("Ex-worker: " + book[2])
                        else:
                            newday.append(book[1] + ": "+ book[2])
                newday.append("No reservations")
                newweek.append(newday)
            lst.append(newweek)
        return lst

class Date_From_String():
    def __init__(self, year, month, day):
        self.year = str(year)
        self.month = str(month)
        self.day = str(day)
    def get_daytime_object(self):
        if len(self.day) == 1:
            self.day = '0' + self.day
        if len(self.month) == 1:
            self.month = '0' + self.month
        strtime = self.day + " " + self.month + " " + str(self.year) + ' 00:00'
        timedateobject = datetime.strptime(strtime, "%d %m %Y %H:%M")
        return timedateobject
