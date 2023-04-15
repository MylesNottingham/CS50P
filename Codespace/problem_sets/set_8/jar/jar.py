# Cookie Jar



# Establishes Jar class
class Jar:
# Initializes a cookie jar with the given capacity
# Capacity represents the maximum number of cookies that can fit in the cookie jar
# Raises ValueError if capacity is not a non-negative int
    def __init__(self, capacity=12):
        if not capacity > 0:
            raise ValueError("Capacity must be a positive integer")
        self.capacity = capacity
        self.size = 0

# Returns the number of cookies in the cookie jar, each represented by a "🍪"
    def __str__(self):
        return self.size * "🍪"

# Adds cookies to the cookie jar and raises ValueError if beyond capacity
    def deposit(self, n):
        self.size += n
        if self.size > self.capacity:
            raise ValueError("Too many cookies")
        return self

# Removes cookies from the cookie jar and raises ValueError if there aren’t enough cookies
    def withdraw(self, n):
        self.size -= n
        if self.size < 0:
            raise ValueError("Not enough cookies")
        return self

# Returns the cookie jar’s capacity
    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

# Returns the number of cookies actually in the cookie jar
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size