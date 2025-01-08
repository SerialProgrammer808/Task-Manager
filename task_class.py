from check_date import check_date

class Task():
    def __init__(self, description, date):
        self.description = description
        self.date = date

    def __str__(self):
        return f"{self.description} due {self.date}"

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        if check_date(date):
            self._date = date
        else:
            raise ValueError("Invalid date")

