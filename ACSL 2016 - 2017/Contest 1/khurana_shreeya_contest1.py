"""
Shreeya Khurana
Intermediate Division
Contest 1
"""
print("""Please input the values with a comma and a space after each card. 
""")

input1 = input("1. ")
input2 = input("2. ")
input3 = input("3. ")
input4 = input("4. ")
input5 = input("5. ")

def AGRAM(input1):
    input1 = input1.split(", ")
    leadcard = input1[0]
    leadlist = list(leadcard)
    if leadlist[0] == "T":
        leadlist[0] = "10"
    if leadlist[0] == "J":
        leadlist[0] = "11"
    if leadlist[0] == "Q":
        leadlist[0] = "12"
    if leadlist[0] == "K":
        leadlist[0] = "13"
    if leadlist[0] == "A":
        leadlist[0] = "1"
    leadnum = int(leadlist[0])
    leadsuit = leadlist[1]

    card1 = list(input1[1])
    card2 = list(input1[2])
    card3 = list(input1[3])
    card4 = list(input1[4])
    card5 = list(input1[5])

    card1num = card1[0]
    card2num = card2[0]
    card3num = card3[0]  
    card4num = card4[0]  
    card5num = card5[0]

    if card1num == "T":
        card1num = "10"
    if card1num == "J":
        card1num = "11"
    if card1num == "Q":
        card1num = "12"
    if card1num == "K":
        card1num = "13"
    if card1num == "A":
        card1num = "1"
        
    if card2num == "T":
        card2num = "10"
    if card2num == "J":
        card2num = "11"
    if card2num == "Q":
        card2num = "12"
    if card2num == "K":
        card2num = "13"
    if card2num == "A":
        card2num = "1"

    if card3num == "T":
        card3num = "10"
    if card3num == "J":
        card3num = "11"
    if card3num == "Q":
        card3num = "12"
    if card3num == "K":
        card3num = "13"
    if card3num == "A":
        card3num = "1"

    if card4num == "T":
        card4num = "10"
    if card4num == "J":
        card4num = "11"
    if card4num == "Q":
        card4num = "12"
    if card4num == "K":
        card4num = "13"
    if card4num == "A":
        card4num = "1"

    if card5num == "T":
        card5num = "10"
    if card5num == "J":
        card5num = "11"
    if card5num == "Q":
        card5num = "12"
    if card5num == "K":
        card5num = "13"
    if card5num == "A":
        card5num = "1"

    numlist = [int(card1num), int(card2num), int(card3num), int(card4num), int(card5num)]
    suitlist = [card1[1], card2[1], card3[1], card4[1], card5[1]]

    commonsuits = []
    if suitlist[0] == leadsuit:
        commonsuits.append(numlist[0])
    if suitlist[1] == leadsuit:
        commonsuits.append(numlist[1])
    if suitlist[2] == leadsuit:
        commonsuits.append(numlist[2])
    if suitlist[3] == leadsuit:
        commonsuits.append(numlist[3])
    if suitlist[4] == leadsuit:
        commonsuits.append(numlist[4])

    if len(commonsuits) == 0:
        cardnumid = numlist.index(min(numlist))
        numlist[cardnumid] = str(numlist[cardnumid])
        if numlist[cardnumid] == "10":
            numlist[cardnumid] = "T"
        if numlist[cardnumid] == "11":
            numlist[cardnumid] = "J"
        if numlist[cardnumid] == "12":
            numlist[cardnumid] = "Q"
        if numlist[cardnumid] == "13":
            numlist[cardnumid] = "K"
        if numlist[cardnumid] == "1":
            numlist[cardnumid] = "A"
        outputcard = numlist[cardnumid]+ suitlist[cardnumid]
        
    else:
        maxnum = max(commonsuits)
        if maxnum > leadnum:    
            cardnumid = commonsuits.index(min(x for x in commonsuits if x > leadnum))
            commonsuits[cardnumid] = str(commonsuits[cardnumid])
            if commonsuits[cardnumid] == "10":
                commonsuits[cardnumid] = "T"
            if commonsuits[cardnumid] == "11":
                commonsuits[cardnumid] = "J"
            if commonsuits[cardnumid] == "12":
                commonsuits[cardnumid] = "Q"
            if commonsuits[cardnumid] == "13":
                commonsuits[cardnumid] = "K"
            if commonsuits[cardnumid] == "1":
                commonsuits[cardnumid] = "A"
            outputcard = commonsuits[cardnumid] + leadsuit
        else:
            cardnumid = commonsuits.index(min(commonsuits))
            commonsuits[cardnumid] = str(commonsuits[cardnumid])
            if commonsuits[cardnumid] == "10":
                commonsuits[cardnumid] = "T"
            if commonsuits[cardnumid] == "11":
                commonsuits[cardnumid] = "J"
            if commonsuits[cardnumid] == "12":
                commonsuits[cardnumid] = "Q"
            if commonsuits[cardnumid] == "13":
                commonsuits[cardnumid] = "K"
            if commonsuits[cardnumid] == "1":
                commonsuits[cardnumid] = "A"
            outputcard = commonsuits[cardnumid] + leadsuit
    
    print(outputcard)

print()
print()
print("1. ")
AGRAM(input1)
print()
print("2. ")
AGRAM(input2)
print()
print("3. ")
AGRAM(input3)
print()
print("4. ")
AGRAM(input4)
print()
print("5. ")
AGRAM(input5)



    

    

    
