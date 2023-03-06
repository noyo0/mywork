'''Write a function that prints out a menu of commands we can perform, ie add,
view and quit. The function should return what the user chose.
Test the function. We don’t need to worry about error handling yet'''

# error handling with "while" ref: https://programming-21.mooc.fi/part-6/3-errors

def doAdd():
    print("+++++++ doAdd")
    students=[]
    addStud=str(input("Enter student's name: ")
    students.append(addStud)

    

def doView():
    print("....... doView")

def doQuit():
    print("Thank you! ------- doQuit")
    #exit()def UserMenu():
        
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