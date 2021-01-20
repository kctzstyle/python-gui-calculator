
class Calculator:

    def __init__(self):
        self.__values = []

    @property
    def values(self):
        print(self.__values)
        length = len(self.__values)
        if length > 3:
            x, op1, y, op2 = self.__values
            result = self.calculate[op1](float(x), float(y))
            self.reset()
            if result.is_integer():
                result = int(result)
            self.values = result
            self.values = op2
        elif length == 3:
            x, op, y = self.__values
            result = self.calculate[op](float(x), float(y))
            self.reset()
            if result.is_integer():
                result = int(result)
            self.values = result
        return self.__values[0]

    @values.setter
    def values(self, v):
        self.__values.append(v)

    @property
    def calculate(self):
        return {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
            '%': lambda x, y: x % y
        }

    def reset(self):
        self.__values.clear()

    def __add__(self, other):
        self.values = other

    def __str__(self):
        return str(self.values)
