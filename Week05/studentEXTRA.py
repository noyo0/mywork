# studentEXTRA.py
# Author: Norbert Antal
#Write a program that will read in the data for the data structure above, ie
#reads in a student’s name, then keeps reading in their modules and grades
# (until the user enters a blank module name),
#This program can just read in one student (and their module details).

student= {
    "name" : "Günther",
    "modules" : [
        { 
        "Module" : "History", 
        "Teacher" : "Prof. John",
        "Grade" : 99
        },
        {
        "Module" : "Pottery",  
        "Teacher" : "Dr. Akimbo",
        "Grade" : 55
        },
        {
        "Module" : "Horse Maintenance",  
        "Teacher" : "Dr. Dolittle",
        "Grade" : 11
        },
        {
        "Module" : "Fractal Geometry",  
        "Teacher" : "Prof. Marvin",
        "Grade" : 33
        },
        {
        "Module" : "",#"Life, The Universe and Everything",  
        "Teacher" : "Prof. Slartibartfast",
        "Grade" : 42
        },
    ]
}
print("\n Student: " +student["name"])
for i in student["modules"]:
    if i["Module"]== "" or i["Teacher"]== "" or i["Grade"] == "" :
        print(f"VERY SERIOUS WARNING! Blank entry at: ({i})")
        break
    else:
        print("\t {} \t\t: {}" " -- {}".format(i["Module"], i["Grade"], i["Teacher"]))