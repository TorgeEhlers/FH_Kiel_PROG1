# Schrittzähler

class StepCounter:

    def __init__(self):
        self.steps = 0

    def addStep(self):
        self.steps += 1
    
    def reset(self):
        self.steps = 0

    def showSteps(self):
        print(f"Sie sind {self.steps} Schritte gegangen!")


torge = StepCounter()
for i in range(0, 20):
    torge.addStep()
torge.showSteps()
torge.addStep()
torge.reset()
torge.showSteps()

