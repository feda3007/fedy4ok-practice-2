class Student:
    def __init__(self, surname, birthdate, group, grades):
        self.surname = surname
        self.birthdate = birthdate
        self.group = group
        self.grades = grades

    def set_surname(self, new_surname):
        self.surname = new_surname

    def set_birthdate(self, new_birthdate):
        self.birthdate = new_birthdate

    def set_group(self, new_group):
        self.group = new_group

    def get_info(self):
        return (f"Студент: {self.surname}\n"
                f"Дата рождения: {self.birthdate}\n"
                f"Группа: {self.group}\n"
                f"Успеваемость: {self.grades}")


# Демонстрация
students = [
    Student("Кудрявцев", "12.10.2006", "ГРУППА-643", [4, 5, 3, 4, 5]),
    Student("Иванов", "15.03.2006", "ГРУППА-643", [5, 5, 5, 5, 5]),
]

# Изменение данных
students[0].set_surname("Дудкин")   # изменён Кудрявцев на Дудкин
students[0].set_group("ГРУППА-643")

# Поиск студента
input_surname = input("Введите фамилию: ")
input_birthdate = input("Введите дату рождения: ")
found = False
for student in students:
    if student.surname == input_surname and student.birthdate == input_birthdate:
        print(student.get_info())
        found = True
        break
if not found:
    print("Студент не найден.")