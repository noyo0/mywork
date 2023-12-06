'''Write a function that prints out a menu of commands we can perform, ie add,
view and quit. The function should return what the user chose.
Test the function. We don’t need to worry about error handling yet'''

# error handling with "while" ref: https://programming-21.mooc.fi/part-6/3-errors
# return keyword ref: https://www.w3schools.com/python/ref_keyword_return.asp
# execute function stored as string ref: https://www.geeksforgeeks.org/exec-in-python/
# get list index numbers ref: https://towardsdatascience.com/looping-in-python-5289a99a116e#:~:text=Using%20the%20enumerate()%20Function&text=The%20enumerate()%20function%20takes,(the%20default%20is%200).&text=And%20that's%20it!
# update dictionary ref: https://thispointer.com/python-how-to-add-append-key-value-pairs-in-dictionary-using-dict-update/
# dictionary from list (zip) ref: https://stackoverflow.com/questions/209840/how-can-i-make-a-dictionary-dict-from-separate-lists-of-keys-and-values

students = []

def readModules():
    modules=[]
    moduleName = input("\t Enter the first Module name (blank to quit):").strip()
    while moduleName is not "":
        module = {}
        module["name"] = moduleName
        module["grade"]=int(input("\t\tEnter grade:"))
        modules.append(module)
        moduleName = input("\tEnter the next module name (blank to quit):").strip()                     
    return(modules)

def doAdd():
    print("function+++++++ doAdd\n")
    currentStudent = {}
    currentStudent["name"] = input("enter name: ")
    currentStudent["modules"] = readModules()
    students.append(currentStudent)
    doView()


def dispModules(modules):
    print ("\tName \tGrade")
    for m in modules:
        print(m["name"],"\t",m["grade"])

def doView():
    print("function....... doView\n")   
    for currentStudent in students:
        print("student: \n",currentStudent["name"])
        dispModules(currentStudent["modules"])


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
