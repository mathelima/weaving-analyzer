class MovingAverage:
    def __init__(self, window_size):
        self._window_size = window_size
        self._values = []

    def update(self, value):
        """
        Update the moving average with a new value and return the current average.
        """
        self._values.append(value)
        if len(self._values) > self._window_size:
            self._values.pop(0)
        return sum(self._values) / len(self._values)
