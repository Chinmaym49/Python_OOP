class A:

    def __init__(self,x,y,z):
        # public
        self.x=x
        # protected
        self._y=y
        # private
        self.__z=z

if __name__=="__main__":
    ob=A(1,2,3)
    print(ob.x)     # works, its normal

    print(ob._y)    # works! what, why!!! 
                    # Coz there is no such thing as protected in python
                    # The "_" is just a convention so the coder knows that it is protected

    # print(ob.__z) # doesn't work, but wait

    print(dir(ob))  # The output contains all the functions and other crap of the class
                    # But also contains "_A__z". That means, we can actually even access private members!
    
    print(ob._A__z)
    
# 1
# 2
# ['_A__z', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', 
# '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', 
# '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', 
# '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_y', 'x']
# 3