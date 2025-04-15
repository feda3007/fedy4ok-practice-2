class Train:
    def __init__(self, destination, number, departure_time):
        self.destination = destination
        self.number = number
        self.departure_time = departure_time

    def get_info(self):
        return (f"Поезд №{self.number}\n"
                f"Пункт назначения: {self.destination}\n"
                f"Время отправления: {self.departure_time}")


trains = [
    Train("Москва", "123A", "12:00"),
    Train("Санкт-Петербург", "456B", "15:30"),
]

input_number = input("Введите номер поезда: ")
found = False
for train in trains:
    if train.number == input_number:
        print(train.get_info())
        found = True
        break
if not found:
    print("Поезд не найден.")