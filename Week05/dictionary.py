names = ["JOhn", "Susan", "Béla", "János"]
ages = [12,52,33,57]
active = [True, True, False, True]
members ={"name":names,"age":ages, "act" : active}
inx = 1
print(members.get("name","not there"))
