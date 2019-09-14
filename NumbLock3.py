"""Sample (Mem-NL.txt)

$Users$ #Halsey# #Bruce#^
$User-Halsey$ #Ginger# *1*^
$User-Bruce$ #Norris# *1*^
#&

"""
LineDash = '------------------------------------------------------------------------------\n'
#Usernames are surrounded by two $s, Password are surrounded by two #s, Levels are surrounded by two *s, (NO LONGER -->) the end of file will have a &
def finditem(IndChar, TarChar, IndName, ReCheck, IndCheck):
    #starting/ending ind. char ||| starting/ending tar. char ||| ind. name ||| Checks if their is something else to search for||| (NO LONGER -->) end char ||| end ind. group check
    #This is used to check whether or not something actually exists, the specifications are listed as the finditem() is called
    global Return1
    Return1 = ''
    Count1 = '0'
    Port1 = 'x'
    with open('Mem-NL.txt', 'r+') as M:
        M.seek(0)
        Hold2 = M.read()
        for i in Hold2:
            """
            if i == EndChar:
                Return1 = '%NULL'
                break
            """
            if i == IndCheck:
                Port1 = 'x'
            elif Port1 == 'f':
                if i == TarChar:
                    if Return1 == ReCheck:
                        break
                    elif ReCheck == '%NULL':
                        break
                    else:
                        Port1 = 'z'
                Return1 = str(Return1) + str(i)
                #print(Return1) #--> used to determine why Usernames could be the same when creating a new user and not throw up an error, it should throw an error
                #print(i)#--> same as above, the solution was to rid the calling of the finditem() of the extra User- in the ReCheck, I toyed with the idea before, that's why it was there
            elif Port1 == 'z':
                if i == TarChar:
                    Port1 = 'f'
            elif i == IndChar:
                if Port1 == 'y' and len(IndName) == Count1:
                    Port1 = 'z'
                elif Port1 == 'x': #This down to the 'else:' is used to make sure Hold1 will not be accepted if a username has excess letters (i.e. Halsey would not be accepted as Halseyy)
                    Port1 = 'y'
                    Count1 = 0
                else:
                    Port1 = 'x'
            elif Port1 == 'y':
                #print(str(len(IndName)) + ' : ' + str(Count1)) #--> Used to make sure no errors arose if the count exceded the Hold1 (if i != IndName[Count1]:)
                if len(IndName) > Count1:
                    if i != IndName[Count1]:
                        Count1 = 0
                        Port1 = 'x'
                    else:
                        Count1 += 1
                else:
                    Count1 = 0
                    Port1 = 'x'

def additem(Insert):
    with open('Mem-NL.txt', 'a') as T:
        T.write(Insert)
        #with open('Mem-NL.txt', 'r') as M:
            #T.write(Insert)
        """This was to be used to insert data, it turned out to be too complicated for me, write always destroyed everything in the file
            M.seek(0)
            Count1 = 0
            Brax2 = 0
            Hold3 = M.read()
            for i in Hold3:
                if i == IndChar:
                    Hold4 = Count1
                    Brax2 = 1
                Count1 += 1
            if Brax2 == 1:
                T.seek(Hold4 + Pos)
                print(T.seek(Hold4 + Pos))
                T.write(Insert)
        """
Brax1 = 0
while True: #The Access Loop
    while True:
        if Brax1 == 1:
            Brax1 = 0
            break
        Brax1 = 0
        print(LineDash + "Welcome to Numblock!, Please type in your Username and Password,\nor type %NULL if you don't have one")
        while True:
            if Brax1 == 1 or Brax1 == 2:
                break
            Hold1 = input("\nUSER: ")
            if '%NULL' in Hold1:
                while True: #New User
                    if Brax1 == 1 or Brax1 == 2:
                        break
                    print(LineDash + "Please enter your new Username.\nIt must be longer than 3 characters and may not include @, %, $, #, *, & or ^\nIt will also be rejected if it has already been chosen\nType '%back' to go back")
                    while True: #Username Loop, Used to verify if the Username meets the specifications
                        Brax1 = 3
                        Hold1 = input("\nNEW USER: ")
                        if Hold1 == '%back': #used to go back
                            Brax1 = 2
                        elif len(Hold1) < 3: #char count
                            Brax1 = 0
                        elif '%' in Hold1 or '$' in Hold1 or '#' in Hold1 or '*' in Hold1 or '&' in Hold1 or '^' in Hold1 or '@' in Hold1: #spec. char check
                            Brax1 = 0
                        else: #checks if Username already exists
                            finditem('$', '#', 'Users', Hold1, '^')
                            #print(Return1 + ' : ' + Hold1)
                            if Return1 == Hold1:
                                Brax1 = 0
                        if Brax1 == 0:
                            print(LineDash + 'Your Username has been Rejected Either it is more than 3 characters,\nHas already been taken, or it has a @, %, $, #, *, &, or ^ in it,\nPlease try again\nType \'%back\' to go back')
                        else:
                            break
                    if Brax1 == 2:
                        break
                    while True: #New Password Loop
                        print(LineDash + "Please choose a new Password\nIt must be longer than 3 characters and may not include @, %, $, #, *, & or ^\nType '%back' to go back\n\nNEW USER: " + Hold1)
                        while True: #Used to verify if the Password meets the specifications
                            Hold2 = input('NEW PASSWORD: ')
                            Brax1 = 3
                            if Hold1 == '%back': #used to go back
                                Brax1 = 2
                            elif len(Hold1) < 3: #char count
                                Brax1 = 0
                            elif '%' in Hold1 or '$' in Hold1 or '#' in Hold1 or '*' in Hold1 or '&' in Hold1 or '^' in Hold1 or '@' in Hold1: #spec. char check
                                Brax1 = 0
                            if Brax1 == 0:
                                print(LineDash + 'Your Password has been Rejected, Either it is more than 3 characters,\nor it has a @, %, $, #, *, &, or ^ in it,\nPlease try again\nType \'%back\' to go back\n\nNEW USER: ' + Hold1)
                            else:
                                break
                        if Brax1 == 2:
                            break
                        if Brax1 == 3:
                            Stars = ''
                            for i in Hold2: #Makes the password stars instead of characters
                                Stars = str(Stars) + '*'
                            print(LineDash + 'Please verify your password\nType \'%back\' to go back\n\nNEW USER: ' + Hold1 + '\nNEW PASSWORD: ' + Stars)
                            while True: #Used to verify if the Verified Password meets the specifications
                                Hold3 = input("VERIFIED PASSWORD: ")
                                if Hold3 == '%back':
                                    break
                                elif Hold3 == Hold2:
                                    Brax1 = 1
                                    additem('\n$User-' + Hold1 +'$ #' + Hold2 + '# *1*^\n$Users$ #' + Hold1 + '#^')
                                    print(LineDash + "Your Password has been Accepted, Welcome to NumbLock!")
                                    break
                                else:
                                    print(LineDash + 'Sorry, but your Passwords do not match, Please try Again\nType \'%back\' to go back\n\nNEW USER: ' + Hold1 + '\nNEW PASSWORD: ' + Stars)
                        if Brax1 == 2 or Brax1 == 1:
                            break
            else: #The Sign In Loop
                finditem('$', '#', 'User-' + Hold1, '%NULL', '^')
                if Return1 != '':
                    print(LineDash + 'Please enter your password,\nif you wish to go back, please type \'%back\'')
                    while True:
                        Hold2 = input('\nUSER: ' + Hold1 + '\nPASSWORD: ')
                        if Hold2 == '%back':
                            Brax1 = 2
                            break
                        elif Hold2 == Return1:
                            print(LineDash + "Password Accepted, Welcome to Numblock!")
                            Brax1 = 1
                            break
                        else:
                            print(LineDash + "Invalid Password, please try again,\nto go back, please type '%back'")
                else:
                    print(LineDash + "Sorry, but it seems that Username does not Exist, please try again,\nto become a new user, please type in %NULL")
    ActUser = Hold1
    ActPass = Hold2
    while True:  #The User Loop
        





print("escaped")












