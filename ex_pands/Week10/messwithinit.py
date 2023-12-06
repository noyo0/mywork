# mess with init
# author: Norbert Antal

class Person:
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last
        #self.middlename = middle
    def fullName(self):
        if hasattr(self, 'middlename'):
            return self.firstname +' '+self.middlename+' '+self.lastname
    def __str__(self):
        return(self.fullName())
    def addmiddlename(self, middlename):
        self.middlename = middlename

person1 = Person('Andrew','Beatty')
person1.addmiddlename('middleJoe')
print(person1.firstname)
print(person1.fullName())
print(person1) # for this you need __str___ fuinction