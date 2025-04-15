class Numbers:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def display(self):
        print(f"Числа: {self.a}, {self.b}")

    def change_numbers(self, new_a, new_b):
        self.a = new_a
        self.b = new_b

    def sum(self):
        return self.a + self.b

    def max(self):
        return max(self.a, self.b)


nums = Numbers(3, 5)
nums.display()  # Числа: 3, 5
print("Сумма:", nums.sum())  # 8
print("Максимум:", nums.max())  # 5
nums.change_numbers(10, 20)
nums.display()  # Числа: 10, 20