class Counter:
    def __init__(self, value=0):
        self._value = value

    def increment(self):
        self._value += 1

    def decrement(self):
        self._value -= 1

    @property
    def value(self):
        return self._value


#пример использования
counter = Counter(5)
counter.increment()
print("Текущее значение:", counter.value)  # 6
counter.decrement()
print("Текущее значение:", counter.value)  # 5