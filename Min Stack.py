class MinStack:
    # @param x, an integer
    def __init__(self):
        self.s=[]
        self.m=[]
    def push(self, x):
        if len(self.m)==0 or x<self.m[-1]:
            self.m.append(x)
        self.s.append(x)
    # @return nothing
    def pop(self):
        if len(self.s)==0:
            return
        if self.s[-1]==self.m[-1]:
            self.m.pop()
        self.s.pop()
    # @return an integer
    def top(self):
        if len(self.s)==0:
            return -1
        return self.s[-1]
    # @return an integer
    def getMin(self):
        if len(self.m)==0:
            return -1
        return self.m[-1]    
==>TC=O(n) with 2 stacks of O(n)
class MinStack:
    # @param x, an integer
    def __init__(self):
        self.s=[]
        self.mins=float('-inf')
    def push(self, x):
        if len(self.s)==0:
            self.s.append(x)
            self.mins=x
        if x<self.mins:
            self.s.append(2*x-self.mins)
            self.mins=x
        else:
            self.s.append(x)
    # @return nothing
    def pop(self):
        if len(self.s)==0:
            return 
        if self.mins>self.s[-1]:
            prevmin=2*self.mins-self.s[-1]
            self.mins=prevmin
            self.s.pop()
        else:
            self.s.pop()
    # @return an integer
    def top(self):
        if len(self.s)==0:
            return -1
        if self.s[-1]<self.mins:
            return self.mins
        return self.s[-1]
    # @return an integer
    def getMin(self):
        if len(self.s)<=0:
            return -1
        return self.mins

==TC=O(n) and only one stack with mins variable
