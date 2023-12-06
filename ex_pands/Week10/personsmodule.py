# demo of a module
# Author: Norbert Antal
import datetime as dt

def gethealthdata(person):
    print("get health data: ", person['firstname'])

def displayperson(person):
    print(person)

if __name__=='__main__':
    person1 = {
        'firstname' : 'andrew',
        'lastname' : 'beatty',
        'dob' : dt.date(210,1,1),
        'height' : 180,
        'width' : 100
    }

#displayperson(person1)
#gethealthdata(person1)