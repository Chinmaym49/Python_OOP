class Dog:

    # class variable
    animal="dog"

    # constructor
    def __init__(self,name,breed,age):
        # instance variables
        self.name=name
        self.breed=breed
        self.age=age

    def change_animal(self,str):
        Dog.animal=str

if __name__=="__main__":
    d1=Dog("tuffy","poodle",3)
    print(d1.name,d1.breed,d1.age,d1.animal)
    d2=Dog("bruno","pitbull",4)
    print(d2.name,d2.breed,d2.age,d2.animal)
    print(Dog.animal)
    d1.change_animal("Doggy")
    print(d1.animal,d2.animal)