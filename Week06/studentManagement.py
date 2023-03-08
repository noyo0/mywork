'''Write a function that prints out a menu of commands we can perform, ie add,
view and quit. The function should return what the user chose.
Test the function. We don’t need to worry about error handling yet'''

# error handling with "while" ref: https://programming-21.mooc.fi/part-6/3-errors
# return keyword ref: https://www.w3schools.com/python/ref_keyword_return.asp
# execute function stored as string ref: https://www.geeksforgeeks.org/exec-in-python/
# get list index numbers ref: https://towardsdatascience.com/looping-in-python-5289a99a116e#:~:text=Using%20the%20enumerate()%20Function&text=The%20enumerate()%20function%20takes,(the%20default%20is%200).&text=And%20that's%20it!
# update dictionary ref: https://thispointer.com/python-how-to-add-append-key-value-pairs-in-dictionary-using-dict-update/
# dictionary from list (zip) ref: https://stackoverflow.com/questions/209840/how-can-i-make-a-dictionary-dict-from-separate-lists-of-keys-and-values

def doModul():
    print("function+++++++doModul\n Student selected: ",gID, gStu)
    Module={}
    modname=[]
    modgrade=[]
    addMod=""
    while addMod != "F" or addMod != "f":
        addMod=input("add module or F for finish:")
        if addMod == "F" or addMod == "f":
            break
        else:
            addGrad=input(f"what is the {gStu}'s grade for {addMod}: ")
            modname.append(addMod)
            modgrade.append(addGrad) #Folytköv!!---------------------->
    Module=dict(zip(modname,modgrade))
    print(Module)
    gStudents[gID].append(Module)
    print(gStudents)


def doAdd():
    print("function+++++++ doAdd\n")
    students=[]
    global gStudents
    gStudents = students
    addStud = ""
    while addStud != "F" or addStud != "f":
        addStud = str(input("Enter student's name or F to finish adding: "))
        if addStud != addStud != "F" or addStud != "f":
            students.append(addStud)
        else:
            break
        print("students added:", students)
    print("Finished adding. \n")
    cont=input("view list? Y for yes:")
    if cont=="y" or cont=="Y":
        print("Full list of students:\n")
        doView()
        return(students)
    else:
        return(students)       


def doView():
    studID=""
    print("function....... doView\n")
    for g in range(len(gStudents)):
        print(f"Student number:{g} - Student: {gStudents[g]}")
    studID=int(input("Add module(s) to Student? Select student number"))
    print(gStudents[studID])
    global gID
    gID = studID
    global gStu
    gStu=gStudents[studID]
    doModul()

    

def doQuit():
    print("Thank you! ------- doQuit\n")
    exit()
        
#-----------------   
def UserMenu():
    while UserMenu != "None":
        menu=[
            {"menuTxt":"(a) Add new student", "menuVal":"a", "function": "doAdd()"},
            {"menuTxt":"(v) View students" , "menuVal": "v", "function": "doView()"},
            {"menuTxt":"(q) Quit" , "menuVal": "q", "function": "doQuit()"}
            ]   
        print("\n What would you like to do?\n")
        for m in menu:
            print(m["menuTxt"])       
        UserSelect=input("\n Type one letter (a/v/q):")
        for m in menu:
            if UserSelect==m["menuVal"]:      
                print("\nYou selected",m["menuTxt"])
                return(m["function"])

#------------------

exec(UserMenu())