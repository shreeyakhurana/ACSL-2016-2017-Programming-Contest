"""
Shreeya Khurana
Int 3
"""
def LightsOut(input1):
    inputlist = input1.split(" ")
    w, h = 8, 8
    board = [[0 for x in range(w)] for y in range(h)]
    r = 1
    while(r <= int(inputlist[0])):
        if len(inputlist[r]) > 2:
            i = 0 
            row = 8 - int(inputlist[r][i])
            columnsstr = inputlist[r][1:len(inputlist[r])]
            columnsint = int(inputlist[r][1:len(inputlist[r])])
            while(i < len(columnsstr)):
                board[row][int(columnsstr[i]) - 1] = 1
                i = i + 1
        else:
            row = 8 - int(inputlist[r][0])
            column = int(inputlist[r][1])
            board[row][column - 1] = 1
        r = r + 1
    numberpressed = int(inputlist[1 + int(inputlist[0])])
    n = 0
    def switch(row, column):
            if board[row][column] == 1:
                board[row][column] = 0
            else:
                board[row][column] = 1 
    while (n < numberpressed):
        rowp = 8 - int(inputlist[2 + int(inputlist[0])][0])
        columnp = int(inputlist[2 + int(inputlist[0])][1]) - 1
        switch(rowp, columnp)
        ######corners#######
        if rowp == 0 and columnp == 0:
            switch(rowp + 1, columnp)
            switch(rowp, columnp + 1)
            switch(rowp + 2,columnp)
            switch(rowp + 1,columnp + 1)
            switch(rowp,columnp)
        elif rowp == 0 and columnp == 7:
            switch(rowp + 1, columnp)
            switch(rowp, columnp)
            switch(rowp + 2, columnp)
            switch(rowp + 1, columnp - 1)
            switch(rowp, columnp - 2)
        elif rowp == 7 and columnp == 7:
            switch(rowp - 1, columnp)
            switch(rowp, columnp - 1)
            switch(rowp - 2, columnp)
            switch(rowp - 1, columnp - 1)
            switch(rowp, columnp - 2)
        elif rowp == 7 and columnp == 0:
            switch(rowp - 1, columnp)
            switch(rowp, columnp + 1)
            switch(rowp - 2, columnp)
            switch(rowp - 1, columnp + 1)
            switch(rowp, columnp + 2)
        ######side edges######
        elif columnp == 0 and rowp == 2:
            switch(rowp - 1, columnp)
            switch(rowp, columnp + 1)
            switch(rowp + 1, columnp)
            switch(rowp + 2, columnp)
            switch(rowp + 1, columnp + 1)
            switch(rowp, columnp + 2)
            switch(rowp - 1, columnp + 1)
        elif columnp == 0 and rowp == 7:
            switch(rowp - 1, columnp)
            switch(rowp, columnp + 1)
            switch(rowp + 1, columnp)
            switch(rowp + 1, columnp + 1)
            switch(rowp, columnp + 2)
            switch(rowp - 1, columnp + 1)
            switch(rowp - 2, columnp)
        elif columnp == 0 and (rowp == 3 or rowp == 4 or rowp == 5 or rowp == 6):
            switch(rowp - 1, columnp)
            switch(rowp, columnp + 1)
            switch(rowp + 1, columnp)
            switch(rowp + 2, columnp)
            switch(rowp + 1, columnp + 1)
            switch(rowp, columnp + 2)
            switch(rowp - 1, columnp + 1)
            switch(rowp - 2, columnp)
            
        elif columnp == 7 and rowp == 2:
            switch(rowp - 1, columnp)
            switch(rowp, columnp - 1)
            switch(rowp + 1, columnp)
            switch(rowp + 2, columnp)
            switch(rowp + 1, columnp - 1)
            switch(rowp, columnp - 2)
            switch(rowp - 1, columnp - 1)
        elif columnp == 7 and rowp == 7:
            switch(rowp - 1, columnp)
            switch(rowp, columnp - 1)
            switch(rowp + 1, columnp)
            switch(rowp + 1, columnp - 1)
            switch(rowp, columnp - 2)
            switch(rowp - 1, columnp - 1)
            switch(rowp - 2, columnp)
        elif columnp == 7 and (rowp == 3 or rowp == 4 or rowp == 5 or rowp == 6):
            switch(rowp - 1, columnp)
            switch(rowp, columnp - 1)
            switch(rowp + 1, columnp)
            switch(rowp + 2, columnp)
            switch(rowp + 1, columnp - 1)
            switch(rowp, columnp - 2)
            switch(rowp - 1, columnp - 1)
            switch(rowp - 2, columnp)
        #####upper edges#####
        elif rowp == 0 and columnp == 1:
            switch(rowp, columnp - 1)
            switch(rowp, columnp + 1)
            switch(rowp - 1, columnp)
            switch(rowp - 2, columnp)
            switch(rowp - 1, columnp - 1)
            switch(rowp, columnp + 2)
            switch(rowp - 1, columnp + 1)
        elif rowp == 0 and columnp == 6:
            switch(rowp, columnp - 1)
            switch(rowp, columnp + 1)
            switch(rowp - 1, columnp)
            switch(rowp - 2, columnp)
            switch(rowp - 1, columnp - 1)
            switch(rowp, columnp - 2)
            switch(rowp - 1, columnp + 1)
        elif rowp == 0 and (columnp == 2 or columnp == 3 or columnp == 4 or columnp == 5):
            switch(rowp, columnp - 1)
            switch(rowp, columnp + 1)
            switch(rowp - 1, columnp)
            switch(rowp - 2, columnp)
            switch(rowp - 1, columnp - 1)
            switch(rowp, columnp - 2)
            switch(rowp - 1, columnp + 1)
            switch(rowp, columnp + 2)
            
        elif rowp == 7 and columnp == 1:
            switch(rowp, columnp - 1)
            switch(rowp, columnp + 1)
            switch(rowp + 1, columnp)
            switch(rowp + 2, columnp)
            switch(rowp + 1, columnp - 1)
            switch(rowp, columnp + 2)
            switch(rowp + 1, columnp + 1)
        elif rowp == 7 and column == 6:
            switch(rowp, columnp - 1)
            switch(rowp, columnp + 1)
            switch(rowp + 1, columnp)
            switch(rowp + 2, columnp)
            switch(rowp + 1, columnp - 1)
            switch(rowp, columnp - 2)
            switch(rowp + 1, columnp + 1)
        elif rowp == 7 and (columnp == 2 or columnp == 3 or columnp == 4 or columnp == 5):
            switch(rowp, columnp - 1)
            switch(rowp, columnp + 1)
            switch(rowp + 1, columnp)
            switch(rowp + 2, columnp)
            switch(rowp + 1, columnp - 1)
            switch(rowp, columnp - 2)
            switch(rowp + 1, columnp + 1)
            switch(rowp, columnp + 2)
        #####other problems####
        elif rowp == 7 and columnp == 1:
            switch(rowp, columnp + 1)
            switch(rowp, columnp - 1)
            switch(rowp, columnp + 2)
            switch(rowp + 1, columnp)
            switch(rowp + 1, columnp - 1)
            switch(rowp + 1, columnp + 1)
            switch(rowp - 1, columnp + 1)
            switch(rowp - 1, columnp - 1)
            switch(rowp - 1, columnp)
            switch(rowp - 2, columnp)
        elif rowp == 7 and column == 6:
            switch(rowp, columnp + 1)
            switch(rowp, columnp - 1)
            switch(rowp, columnp - 2)
            switch(rowp + 1, columnp)
            switch(rowp + 1, columnp - 1)
            switch(rowp + 1, columnp + 1)
            switch(rowp - 1, columnp + 1)
            switch(rowp - 1, columnp - 1)
            switch(rowp - 1, columnp)
            switch(rowp - 2, columnp)
        elif rowp == 2 and column == 6:
            switch(rowp, columnp + 1)
            switch(rowp, columnp - 1)
            switch(rowp, columnp - 2)
            switch(rowp + 1, columnp)
            switch(rowp + 1, columnp - 1)
            switch(rowp + 1, columnp + 1)
            switch(rowp - 1, columnp + 1)
            switch(rowp - 1, columnp - 1)
            switch(rowp - 1, columnp)
            switch(rowp + 2, columnp)
        elif rowp == 2 and column == 1:
            switch(rowp, columnp + 1)
            switch(rowp, columnp - 1)
            switch(rowp, columnp + 2)
            switch(rowp + 1, columnp)
            switch(rowp + 1, columnp - 1)
            switch(rowp + 1, columnp + 1)
            switch(rowp - 1, columnp + 1)
            switch(rowp - 1, columnp - 1)
            switch(rowp - 1, columnp)
            switch(rowp + 2, columnp)

        elif rowp == 7 and (columnp == 2 or columnp == 3 or columnp == 4 or columnp == 5):
            switch(rowp, columnp + 1)
            switch(rowp, columnp - 1)
            switch(rowp, columnp + 2)
            switch(rowp, columnp - 2)
            switch(rowp + 1, columnp)
            switch(rowp + 1, columnp - 1)
            switch(rowp + 1, columnp + 1)
            switch(rowp - 1, columnp + 1)
            switch(rowp - 1, columnp - 1)
            switch(rowp - 1, columnp)
            switch(rowp - 2, columnp)
        elif rowp == 2 and (columnp == 2 or columnp == 3 or columnp == 4 or columnp == 5):
            switch(rowp, columnp + 1)
            switch(rowp, columnp - 1)
            switch(rowp, columnp + 2)
            switch(rowp, columnp - 2)
            switch(rowp + 1, columnp)
            switch(rowp + 1, columnp - 1)
            switch(rowp + 1, columnp + 1)
            switch(rowp - 1, columnp + 1)
            switch(rowp - 1, columnp - 1)
            switch(rowp - 1, columnp)
            switch(rowp + 2, columnp)

        elif columnp == 1 and (rowp == 3 or rowp == 4 or rowp == 5 or rowp == 6):
            switch(rowp, columnp + 1)
            switch(rowp, columnp - 1)
            switch(rowp, columnp + 2)
            switch(rowp + 1, columnp)
            switch(rowp + 1, columnp - 1)
            switch(rowp + 1, columnp + 1)
            switch(rowp - 1, columnp + 1)
            switch(rowp - 1, columnp - 1)
            switch(rowp - 1, columnp)
            switch(rowp + 2, columnp)
            switch(rowp - 2, columnp)
        elif columnp == 6 and (rowp == 3 or rowp == 4 or rowp == 5 or rowp == 6):
            switch(rowp, columnp + 1)
            switch(rowp, columnp - 1)
            switch(rowp, columnp - 2)
            switch(rowp + 1, columnp)
            switch(rowp + 1, columnp - 1)
            switch(rowp + 1, columnp + 1)
            switch(rowp - 1, columnp + 1)
            switch(rowp - 1, columnp - 1)
            switch(rowp - 1, columnp)
            switch(rowp + 2, columnp)
            switch(rowp - 2, columnp)
        #####middle####
        else:
            switch(rowp, columnp + 1)
            switch(rowp + 1, columnp)
            switch(rowp, columnp - 1)
            switch(rowp - 1, columnp)
            switch(rowp - 1, columnp + 1)
            switch(rowp, columnp + 2)
            switch(rowp + 1, columnp + 1)
            switch(rowp + 2, columnp)
            switch(rowp + 1, columnp - 1)
            switch(rowp, columnp - 2)
            switch(rowp - 1, columnp - 1)
            switch(rowp - 2, columnp)
        inputlist.pop(2 + int(inputlist[0]))
        n = n + 1
    output = sum(x.count(1) for x in board)
    print(output)

input1 = input("1. ")
print("Output 1: ")
LightsOut(input1)
print()
input2 = input("2. ")
print("Output 2: ")
LightsOut(input2)
print()
input3 = input("3. ")
print("Output 3: ")
LightsOut(input3)
print()
input4 = input("4. ")
print("Output 4: ")
LightsOut(input4)
print()
input5 = input("5. ")
print("Output 5: ")
LightsOut(input5)
