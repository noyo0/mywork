import os
FILENAME="count.txt"

def fn_readnumber():
    try:
        with open(FILENAME) as f:
            num=int(f.read())
            fn_writenumber(num+1)
            return(num)
    except IOError:
        return(0) 

def fn_writenumber(number):
    with open(FILENAME, "wt") as f:
        f.write(str(number))

if not os.path.isfile(FILENAME):
    print("file doesn\'t exist")
    fn_writenumber(0)
    
num=fn_readnumber()
print(f"we have ran this program {num} times")
        