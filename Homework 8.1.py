class Data:
    def __init__(self, date):
        self.date = date

    @classmethod
    def extract_digit(cls, date):
        row = list(map(int, date.split("-")))
        return row[0], row[1], row[2]


    @staticmethod
    def valid(date):
        row = list(map(int, date.split("-")))
        try:
            if not (row[0] > 0 and row[0] <= 31):
                raise ValueError
        except ValueError:
            print('выберите дату от  1 до 31')
        else:
            print('корректный формат даты')
        try:
            if not (row[1] > 0 and row[1] <= 12):
                raise ValueError
        except ValueError:
            print('выберите месяц от  1 до 12')
        else:
            print("корректный формат месяца")

        try:
            if not (row[2] >= 1950 and row[2] <= 2100):
                raise ValueError
        except ValueError:
            print('выберите год от  1950 до 2100')
        else:
            print("Корректный формат года")
        return f'процесс валидации завершен'






print(Data.extract_digit("09-08-2020"))
print(Data.valid("37-15-2020"))
