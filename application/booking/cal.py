
import calendar
from datetime import datetime, date

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
