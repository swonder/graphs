class myQueue:
    def __init__(self):
        self.q = []
    def push(self, elem):
        self.q.append(elem)
    def pop(self):
        elem = self.q[0]
        self.q = self.q[1:]
        return elem
    def size(self):
        return len(self.q)
    def empty(self):
        if len(self.q) == 0:
            return True
        return False
    def __str__(self):
        dsp = "Elements in queue: \n"
        for elem in self.q:
            dsp += str(elem) + ", "
        dsp = dsp.rstrip(", ")
        return dsp
