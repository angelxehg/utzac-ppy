class Fibonacci:
    def __init__(self, limit):
        self.limit = limit
    def __iter__(self):
        self.fibs = []
        return self
    def __next__(self):
        if len(self.fibs) == self.limit:
            raise StopIteration
        if len(self.fibs) == 0:
            self.fibs.append(0)
        elif len(self.fibs) < 3:
            self.fibs.append(1)
        else:
            self.fibs.append(self.fibs[-1] + self.fibs[-2])
        return self.fibs[-1]


for i in Fibonacci(10):
    print(i)
# Imprime [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
