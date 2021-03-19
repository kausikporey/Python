class A:
    def __init__(self):
        self.x = 67
    def __sub__(self,other):
        s = self.x + other.x
        return s    

class B:
    def __init__(self):
        self.x = 90
    def __sub__(self,other):
        s = self.x + other.x
        return s            

a = A()
b = B()
print(b-a)