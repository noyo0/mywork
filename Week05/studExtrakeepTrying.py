# studentEXTRA.py
# Author: Norbert Antal
#Write a program that will read in the data for the data structure above, ie
#reads in a student’s name, then keeps reading in their modules and grades
# (until the user enters a blank module name),
#This program prompts user to enter a module name from a pregeneraed list and filters students who are enrolled in selected module

students = { #create student database
    "Mary" : { 
        "modules" : [
            {
                "module" : "Programming",
                "grade": 99
        },
            {
                "module" : "Poetry",
                "grade" : 3
        }
        ]
        },
    "John" : { 
        "modules" : [
            {
                "module" : "Pottery",
                "grade": 20
        },
            {
                "module" : "Architecture",
                "grade" : 5
        }
        ]
        },
    "Bill" : { 
        "modules" : [
            {
                "module" : "Poetry",
                "grade": 90
        },
            {
                "module" : "Athletics",
                "grade" : 5
        }
        ]
        },
    "Pam" : { 
        "modules" : [
            {
                "module" : "Poetry",
                "grade": 20
        },
            {
                "module" : "Architecture",
                "grade" : 55
        }
        ]
        },
    "Jack" : { 
        "modules" : [
            {
                "module" : "Cooking",
                "grade": 92
        },
            {
                "module" : "Programming",
                "grade" : 50
        }
        ]
        }
    }
#create module selection list
lst = []
selStud = {"stud":"","mod":"","grd":""} #dictionary container for filter list
filtStud = []
for stud, data in students.items():
    for i in data["modules"]:
        addtolist = i["module"]
        if addtolist not in lst: # check for duplicates
            lst.append(i["module"]) # append list with unique list items only
for l in lst:
    print(l) #print module selection
# user must enter a valid module name from the list to continue
userinput = input("Enter a modulename from above list (Case sensitive): ")
if userinput not in lst:
    print("That is not on the list. \n \t ...Program closed")
else: # if item correctly entered Program lists sutdent names, modules and grades
    for stud, data in students.items():
        print(stud)
        for i in data["modules"]:
           print("\t{}\t\t\t: {}".format(i["module"],i["grade"]))
#for s in selStud: #print all dictionary items
    #print(selStud["stud"]+" - "+selStud["mod"]+" - "+selStud["grd"])
# lets try with lists
print("\n -> LIST students with the selected module:")
for stud, data in students.items():
# turns out there was no need for a separate list
    for d in data["modules"]:
       if userinput == d["module"]:
            print(stud,"-",d["module"],"-",d["grade"])

# this is the tricky bit; I want to compile a filterd list of students,modules and grades
# by appending a dictionary. However, the dictionary overwrites instead of appending (I got the append bit from stackoverflow)            
# for stud, data in students.items():
#    for d in data["modules"]:
#       if userinput == d["module"]:
#          selStud['stud'] = str(stud)
#          selStud['mod'] = str(d["module"])
#          selStud['grd'] = str(d["grade"])
#print("\n -> DICT students with the selected module:")