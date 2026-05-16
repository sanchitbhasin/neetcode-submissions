# Alternate soln - using one stack only

class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = float('inf')

    def push(self, val: int) -> None:
        if not self.stack:
            self.mini = val
            self.stack.append(0)
        else:
            self.stack.append(val - self.mini)
            if val < self.mini:
                self.mini = val

    def pop(self) -> None:
        if not self.stack:
            return
            
        top = self.stack.pop()

        if top < 0:
            self.mini = self.mini - top

    def top(self) -> int:
        top = self.stack[-1]
        if top > 0:
            return self.stack[-1] + self.mini
        return self.mini
    

    def getMin(self) -> int:
        return self.mini
        
