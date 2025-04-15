class DemoClass:
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b
        print(f"Создан объект с параметрами: {a}, {b}")

    def __del__(self):
        print(f"Объект с параметрами {self.a}, {self.b} удален")



obj1 = DemoClass()
obj2 = DemoClass(10, 20)
del obj1
del obj2