# Inheritance
class Quadrillateral():
    
    def __init__(self):
        self.n=4

    def area(self):
        pass

    def sides(self):
        return self.n

class Square(Quadrillateral):
    
    def __init__(self,a):
        super().__init__()
        self.side=a

    # Override
    def area(self):
        return self.side**2

class Rectangle(Quadrillateral):
    
    def __init__(self,l,b):
        super().__init__()
        self.length=l
        self.breadth=b

    # Override
    def area(self):
        return self.length*self.breadth

if __name__=="__main__":
    s=Square(4)
    r=Rectangle(3,5)
    print(s.sides(),s.area())
    print(r.sides(),r.area())

# 4 16
# 4 15