class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []
        self.index = 0

    def append(self, item):
        # If there is empty spot in the ring
        if len(self.buffer) < self.capacity:
            self.buffer.append(item)
        # If there is no spot in the ring
        else:
            if len(self.buffer) == self.capacity:
               self.index



    def get(self):
        pass