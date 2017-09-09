class node:
    def __init__(self, k, v):
        self.key = k
        self.value = v
    def __str__(self):
        return "[" + str(self.key) + "] => " + str(self.value)
