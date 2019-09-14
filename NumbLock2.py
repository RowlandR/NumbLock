global Break1
Break1 = 0
Count1 = 0
Hold1 = 0
Port1 = 0
def seektrack(target):
    M.seek(0)
    Count1 = 0
    Port1 = 0
    Hold1 = ''
    global List1
    List1 = []
    for i in M.read():
        if Port1 == 2:
            if i == '^':
                List1.append(Hold1)
                break
            elif i == ' ':
                List1.append(Hold1)
                Hold1 = ''
            else:
                Hold1 = str(Hold1) + str(i)
        elif Port1 == 1:
            if i == '^':
                Port1 = 2
            elif i != target[Count1]:
                Port1 = 0
                Count1 = 0
            Count1 += 1
        elif i == '&':
            break
        elif i == '*':
            Port1 = 1
            
def checklist(input):
    global Break1
    for i in List1:
        if i == input:
            Break1 = 0
def seekplace(target):
    global Count1
    Count1 = 0
    M.seek(0)
    for i in M.read():
        if i == target:
            break
        Count1 += 1


with open('Memory-NL.txt', 'r+') as M:
    while True:
        Hold1 = input("Welcome to NumbLock, do you have an existing account?\nPlease enter Yes, No, or Skip\n")
        if Hold1 == "Yes" or Hold1 == "YES" or Hold1 == "yes":
            Hold1 = input("Please enter your Username\n\nUSER: ")
        elif Hold1 == "No" or Hold1 == "NO" or Hold1 == "no":
            Hold1 = input("\nPlease enter your new Username\n\nIt may not include any spaces, $, &, ^, *, must be longer than 3 characters,\nand cannot be already taken\n\nUSER: ")
            while True:
                Break1 = 1
                Count1 = 0
                for i in Hold1:
                    Count1 += 1
                    if i == ' ' or i == '*' or i == '&' or i == '^' or i == '$':
                        Break1 = 0
                if Count1 < 4:
                    Break1 = 0
                else:
                    seektrack('Users')
                    checklist(Hold1)
                if Break1 == 1:
                    NewUser = Hold1
                    break
                else:
                    Hold1 = input("\nSorry, but your Username has not been accepted,\nplease review the guidelines above\n\nUSER: ")
            Hold1 = input("Please enter your new Password, it may not include any spaces, $, &, ^, *,\nandmust be longer than 3 characters\nif you do not want a password, please type in %NULL\n\nUSER: " + NewUser + "\nPASS: ")
            while True:
                Break1 = 1
                Count1 = 0
                for i in Hold1:
                    Count1 += 1
                    if i == ' ' or i == '*' or i == '&' or i == '^' or i == '$':
                        Break1 = 0
                if Count1 < 4:
                    Break1 = 0
                if Break1 == 1:
                    NewPass = Hold1
                    break
                else:
                    Hold1 = input("\nSorry, but your Password has not been accepted,\nplease review the guidelines above\n\nUSER: " + NewUser + "\nPASS: ")
            seekplace('$')
            M.seek(Count1 - 1)
            
            M.write("*!" + NewUser + "^" + NewPass + " LV1^\n$")

            
                
                

