class Jar:
    def __init__(self, capacity=12):
        if(capacity<0):
            raise ValueError
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪"*self.size

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError
        self.size += n

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError
        self.size -= n

    @property
    def capacity(cls):
        return cls._capacity

    @capacity.setter
    def capacity(cls, n ):
        cls._capacity = n

    @property
    def size(cls):
        return cls._size

    @size.setter
    def size(cls, n ):
        cls._size = n

