class Calculation:
    def __init__(self):
        self.__calculationLine = ""
    def SetCalculationLine(self, value):
        self.__calculationLine = value

    def SetLastSymbolCalculationLine(self, symbol):
        self.__calculationLine += symbol

    def GetCalculationLine(self):
        return self.__calculationLine

    def GetLastSymbol(self):
        return self.__calculationLine[-1] if self.__calculationLine else ""

    def DeleteLastSymbol(self):
        if self.__calculationLine:
            self.__calculationLine = self.__calculationLine[:-1]

# Пример использования:
calc = Calculation()
calc.SetCalculationLine("123")
print(calc.GetCalculationLine())  # Вывод: 123

calc.SetLastSymbolCalculationLine("4")
print(calc.GetCalculationLine())  # Вывод: 1234

print(calc.GetLastSymbol())       # Вывод: 4

calc.DeleteLastSymbol()
print(calc.GetCalculationLine())  # Вывод: 123