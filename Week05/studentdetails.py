student = {
    "details" : {"Firstname" : "Mary", "Lastname" : ""},
    "modules" : {"Programming" : 45, "History" : 99}
}
print("Student: "+student["details"]["Firstname"])
print(*['\t:'+str(k) + '\t:' + str(v) for k,v in student["modules"].items()], sep='\n') #ref: https://blog.finxter.com/how-to-print-a-dictionary-without-brackets-in-python/#:~:text=To%20print%20a%20comma%2Dseparated,elements%20with%20a%20newline%20character.
