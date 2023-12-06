student= {
    "name" : "Mary",
    "modules" : [
        { 
        "Module" : "History", 
        "Teacher" : "Prof. John",
        "Grade" : 99
        },
        {
        "Module" : "Programming",  
        "Teacher" : "Dr. Akimbo",
        "Grade" : 45
        }
    ]
}
print(student["name"])
for i in student["modules"]:
    print("\t {} \t: {}" "\t -- {}".format(i["Module"], i["Grade"], i["Teacher"]))
#print(student["modules"]["mod1"]["Teacher"], student["modules"]["mod1"]["Grade"])
# iterate if list, call if dictionary!+!!!!!!!!!
print(len(student["modules"])

               