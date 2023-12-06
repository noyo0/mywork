# messing with objects
# Author: Norbert Antal

class Naemofclass:
    name = ""
    last = ""

    def getfullname(self):
        return(self.name + ' ' + self.last)

    pass


inst = Naemofclass()
inst2 = Naemofclass()

inst.name = 'andrew'
inst.last = 'da man'
inst2.last = 'beatty'
person = inst

print(person.getfullname())