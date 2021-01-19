
import operator

from functools import reduce
from queue import SimpleQueue


class Calculator:

    def __init__(self):
        self.__q = SimpleQueue()
        self.__op = {
            '+': self.add,
            '-': self.sub,
            '*': self.mul,
            '/': self.div,
            '%': self.mod
        }

    @property
    def values(self):
        return self.__q

    @values.setter
    def values(self, v):
        self.__q.put(v)

    def reset(self):
        self.__q = SimpleQueue()

    def eq(self):
        result = 0
        length = self.values.qsize()
        print(self.values)

        if length >= 3:
            v1 = float(self.values.get())
            op = self.values.get()
            v2 = float(self.values.get())
            print(v1, op, v2)
            cal = self.__op.get(op)
            result = cal((v1, v2))
        elif 0 < length <= 2:
            v = self.values.get()
            op = self.values.get()
            print(v, op)
            self.values = v
            self.values = op
            return v
        else:
            result = 0
        print(result)
        return result

    def add(self, values):
        v = sum(values)
        self.values = v
        return v

    def sub(self, values):
        v = reduce(operator.sub, values)
        self.values = v
        return v

    def mul(self, values):
        v = reduce(operator.mul, values)
        self.values = v
        return v

    def div(self, values):
        v = reduce(operator.truediv, values)
        self.values = v
        return v

    def mod(self, values):
        v = reduce(operator.mod, values)
        self.values = v
        return v

    def __add__(self, other):
        self.values = other

    def __str__(self):
        return str(self.eq())
