# use of the person module 
# Author: Norbert Antal

from personsmodule import *

person1 = {
        'firstname' : 'andrew',
        'lastname' : 'beatty',
        'dob' : dt.date(210,1,1),
        'height' : 180,
        'width' : 100
    }

displayperson(person1)
gethealthdata(person1)
