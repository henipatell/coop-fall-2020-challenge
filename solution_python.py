class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0
        self.totalSteps = 0
        self.history = [self.value]
        self.redoOps = []

    def add(self, num: int):
        self.value = self.value + num
        self.totalSteps += 1;
        self.history.append(self.value)

    def subtract(self, num: int):
        self.value = self.value - num
        self.totalSteps += 1;
        self.history.append(self.value)

    def undo(self):
        if self.totalSteps > 0:
            self.totalSteps -= 1
            temp = self.history.pop()
            self.value = self.history[-1]
            self.redoOps.append(temp)
        else:
            print("Nothing to undo")
        self.totalSteps += 1;

    def redo(self):
        if len(self.redoOps) > 0:
            self.totalSteps -= 1
            temp = self.redoOps.pop()
            self.history.append(temp)
            self.value = self.history[-1]
        else:
            print("Nothing to undo")
        self.totalSteps += 1

    def bulk_undo(self, steps: int):
        while steps>0:
            self.undo()
            steps = steps - 1
        self.totalSteps += 1

    def bulk_redo(self, steps: int):
        while steps>0:
            self.redo()
            steps = steps - 1
        self.totalSteps += 1
