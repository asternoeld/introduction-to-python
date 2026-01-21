class Jar:
    def __init__(self, capacity=12):
        # capacity must be a non-negative integer
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer")

        self._capacity = capacity
        self._size = 0  # starts empty

    def __str__(self):
        # return cookies as 🍪 repeated "size" times
        return "🍪" * self._size

    def deposit(self, n):
        # n must be a positive integer
        if not isinstance(n, int) or n < 0:
            raise ValueError("Deposit amount must be a non-negative integer")

        if self._size + n > self._capacity:
            raise ValueError("Too many cookies")

        self._size += n

    def withdraw(self, n):
        # n must be a positive integer
        if not isinstance(n, int) or n < 0:
            raise ValueError("Withdraw amount must be a non-negative integer")

        if n > self._size:
            raise ValueError("Not enough cookies")

        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size