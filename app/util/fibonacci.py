import threading


class Fibonacci:
    """
    This class is an iterator object that generate fibonacci sequence on the fly,
    it also contains caching mechanism that will share with all Fibonacci
    instance of this class make older instance run more efficient than predecessor.

    Attributes:
        fib_position (int): The position of fib you want this class handle.

    Returns:
        iterator: Return an iterable object that is a sequence of fib.

    """
    CACHE = {0: 0, 1: 1}

    # Prevent race condition when multiple instance try to edit our cache
    LOCK = threading.Lock()

    def __init__(self, fib_position):
        self.fib_position = fib_position
        self.current_position = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_position >= self.fib_position:
            raise StopIteration
        if self.current_position in self.CACHE:
            result = self.CACHE[self.current_position]
        else:
            with self.LOCK:
                result = self.CACHE[self.current_position] = self.CACHE[self.current_position - 1] + \
                                                             self.CACHE[self.current_position - 2]
        self.current_position += 1
        return result
