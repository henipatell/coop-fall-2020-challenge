class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0
        self.totalSteps = 0
        self.history = [self.value]
        self.redoOps = []

    def add(self, num: int):
        self.value = self.value + num
        self.history.append(self.value)

    def subtract(self, num: int):
        self.value = self.value - num
        self.history.append(self.value)

    def undo(self):
        if len(self.history)>1:
            self.value = self.history[-2]
        else:
            print("Nothing to undo")

    def redo(self):
        if len(self.history)>0:
            self.value = self.history[-1]
        else:
            print("Nothing to redo")

    def bulk_undo(self, steps: int):
        if (steps == len(self.history)):
                self.value = 0
        if (len(self.history) > steps):
            self.value = self.history[-2 - (steps) + 1]


    def bulk_redo(self, steps: int):
        if(len(self.history)>steps):
            self.value = self.history[-1]

