class myStack:
    def __init__(self):
        self.s = []
    def push(self, elem):
        self.s.append(elem)
    def pop(self):
        return self.s.pop()
    def size(self):
        return len(self.s)
    def empty(self):
        if len(self.s) == 0:
            return True
        return False
    def __str__(self):
        dsp = "Elements in stack: \n"
        for elem in self.s:
            dsp += str(elem) + ", "
        dsp = dsp.rstrip(", ")
        return dsp
