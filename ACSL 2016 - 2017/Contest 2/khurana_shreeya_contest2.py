"""
Shreeya Khurana
Block C
"""
print("""For inputs 1 through 5, decimals or integer values are acceptable..
For formats 5 to 8, c is a non-negative integer.
The solution values in the output are decimal values rounded to the tenths place. 
""")
input1 = input("1. ")
input2 = input("2. ")
input3 = input("3. ")
input4 = input("4. ")
input5 = input("5. ")

def program(input1):
    a = ""
    b = ""
    c = ""
    op = ""
    x = 0
    x1 = 0
    x2 = 0
    line = ""
    input1list = input1.split(",")
    a = float(input1list[0])
    b = float(input1list[1])
    c = float(input1list[2])
    op = float(input1list[3])
    #Greater Than
    if op == 1:
        x = (c-b)/a
        x = round(x,1)
        if a > 0:
            line = "o----->"
        else:
            line = "<-----o"
        print(x,"and",line)
    #Less Than
    elif op == 2:
        x = (c-b)/a
        x = round(x,1)
        if a > 0:
            line = "<-----o"
        else:
            line = "o----->"
        print(x,"and",line)
    #Greater Than or Equal to
    elif op == 3:
        x = (c-b)/a
        x = round(x,1)
        if a > 0:
            line = "*----->"
        else:
            line = "<-----*"
        print(x,"and",line)
    #Less Than or Equal to
    elif op == 4:
        x = (c-b)/a
        x = round(x,1)
        if a > 0:
            line = "<-----*"
        else:
            line = "*----->"
        print(x,"and",line)
        
    ###ABSOLUTE VALUE###
    #Greater Than
    elif op == 5:
        x1 = (c-b)/a
        x2 = ((0-c) - b)/a
        x1 = round(x1,1)
        x2 = round(x2,1)
        line = "<-----o.....o----->"
        if x1 < x2:
            print(x1, " and ", x2, " and ", line)
        else:
            print(x2, " and ", x1, " and ", line)
    #Less Than
    elif op == 6:
        x1 = (c-b)/a
        x2 = ((0-c) - b)/a
        x1 = round(x1,1)
        x2 = round(x2,1)
        line = "o-----o"
        if x1 < x2:
            print(x1, " and ", x2, " and ", line)
        else:
            print(x2, " and ", x1, " and ", line)
    #Greater Than or Equal to
    elif op == 7:
        x1 = (c-b)/a
        x2 = ((0-c) - b)/a
        x1 = round(x1,1)
        x2 = round(x2,1)
        line = "<-----*.....*----->"
        if x1 < x2:
            print(x1, " and ", x2, " and ", line)
        else:
            print(x2, " and ", x1, " and ", line)
    #Less Than or Equal to
    elif op == 8:
        x1 = (c-b)/a
        x2 = ((0-c) - b)/a
        x1 = round(x1,1)
        x2 = round(x2,1)
        line = "*-----*"
        if x1 < x2:
            print(x1, " and ", x2, " and ", line)
        else:
            print(x2, " and ", x1, " and ", line)
print("OUTPUT #1: ")            
program(input1)
print()
print("OUTPUT #2: ")            
program(input2)
print()
print("OUTPUT #3: ")            
program(input3)
print()
print("OUTPUT #4: ")           
program(input4)
print()
print("OUTPUT #5: ")            
program(input5)
print()

