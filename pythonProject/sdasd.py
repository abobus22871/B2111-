class Counter:
    def __init__(self, max_numbers):
        self.i = 0
        self.max_numbers = max_numbers

    def __iter__(self):
        self.i = 0
        return self.i

    def __next__(self):
        self.i +=1
        if self.i > self.max_numbers:
            raise StopIteration
        return self.i


count = Counter(666)
print(count.__next__())
print(count.__iter__())
print(next(count))
print(next(count))