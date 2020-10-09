class A:

    def __init__(self,a):
        self.a=a

    def display(self):
        print(self.a)

class B:

    def __init__(self,b):
        self.b=b

    def display(self):
        print(self.b)

class C(A,B):

    def __init__(self,a,b,c):
        A.__init__(self,a)      # Calling base class contructors to pass parameters
        B.__init__(self,b)
        self.c=c

    def disp(self):
        A.display(self)         # Calling base class functions
        B.display(self)
        print("C")

if __name__=="__main__":
    c=C("A","B","C")
    c.disp()

# A
# B
# C

# Sadly, in pyth, we can access data members of only first base class in multiple inheritance. This can be
# done using super(). In this case, super().a will work but super().b won't work because there is no such 
# member in A class. 