"""Sample (Mem-NL.txt)
#Current #Format: 2
#Format 1
---
$Users$ #Halsey# #Bruce#^
$User-Halsey$ #Ginger# *1*^
$User-Bruce$ #Norris# *1*^
&
---

#Format 2
---
$Users$ #Halsey# #Bruce#@^
$User-Halsey$ #Ginger# *1*^
$User-Bruce$ #Norris# *1*^
---

"""
LineDash = '------------------------------------------------------------------------------\n' #78 dashes
LvlVal = ['0-2', '3-5', '6-7', '8-9', '10-12', '13-14', '15-16', '17-18', '19-20'] #9 so far

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
                if i == TarChar or TarChar == '':
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

def additem(Input, TarChar, Pos): #What you want inserted into file ||| The char(s) that you are searching for ||| Where in respect to the char you want the insert (takes and int, 0 is before)
    if TarChar == '%append':
        with open('Mem-NL.txt', 'a') as A:
            A.write(Input)
    else:
        with open('Mem-NL.txt') as R: #Opens file so that it can be copied
            Hold3 = R.read()
        Count1 = 0
        Hold4 = ''
        for i in Hold3:
            if len(TarChar) > 1: 
                if len(Hold4) >= len(TarChar): 
                    Hold4 = Hold4[1:] 
                Hold4 += i
            else:
                Hold4 = i
            if Hold4 == TarChar:
                with open('Mem-NL.txt', 'w') as W:
                    W.write(Hold3[:Count1 + Pos - len(TarChar) + 1] + Input + Hold3[Count1 + Pos - len(TarChar) + 1:])
                    Count1 = 'x'
                    break
            Count1 += 1
        if Count1 != 'x':
            for i in range(len(TarChar)):
                if len(Hold4) > 1:
                    Hold4 = Hold4[1:]
                if Hold4 == TarChar:
                    with open('Mem-NL.txt', 'w') as W: #writing to file
                        W.write(Hold3[:Count1 + Pos - len(TarChar) + 1] + Input + Hold3[Count1 + Pos - len(TarChar) + 1:]) #inserts info
                        break
                Count1 += 1

def RunLvl(LvlInd, LvlMode, ActUser): #What lvl (Freestyle, Missed, or Lvl-%) ||| Relaxed or Timed Mode ||| What user is active (for recording score purposes)
    pass

Help = """Welcome to Numblock. This program is used to help with memorization.
When you begin learning, you will be assigned a level. The first level
is lvl 1. In lvl 1, you will be given +, -, *, /, // (floor division),
**(exponents), and %(modulos) problems with the numbers 0-2. There are
25 problems in total and you have 1 minute to solve all of them. you
must get at least 23/25 correct to progress to the next lvl. The format
looks like this (answers can be negative):
1*2 = 
7-10 =
7 % 6 =

In lvl 1, you will deal with numbers 0-2, lvl 2 has 3-5...6-7...8-9, etc
(What this means is that every problem will contain one of the numbers
above based on the lvl's value. Each new lvl may include the numbers
from the previous lvls).

Before each lvl, you have an option to either do 'Timed', which means to
do the 23/25 questions in 1 minute, or 'Relaxed', which means there is
no time limit.

During each level, you will be given an option to answer or skip the
problem, the time will be anounced periodically.

After each lvl, you will be shown the problems that you got wrong or
skipped, these will be put into a special file known as 'Missed'. You
can go the 'Missed' file and review the problems that you got wrong. The
'Missed' numbers may be repeated during the lvl so that you can remember
them better. You can repeat levels after you have finished them. You will
also be shown your score (?/25), the time it took, and the average time
per problem.

In order to progress to the next lvl, you will have to complete the 'Timed'
section in 1 minute, getting 23/25 questions correct.

There will also be a lvl known as 'Freestyle' which will include all of the
numbers of previous lvls.

I hope you enjoy Numblock!

(NOTE:
// (floor division) means to divide WITHOUT HAVING the REMAINDER in
the solution, the only answer is a whole number
% (modulus) meas to ONLY HAVE the REMAINDER as an answer, the only
answer is a whole number
** means an exponent, the number before is the normal number, and the
number afterwords is the exponent, Example: 2**3 = 8)

Type anything to continue.\n
"""
finditem('$', '', 'Users', '@', '^')
if Return1 == '':
    print('$Users$@^ Not Found, Initiating Re-Write...')
    with open('Mem-NL.txt', 'w') as W:
        W.write('$Users$@^')
        print('...Re-Write Complete')

Brax1 = 0
while True: #The Access Loop
    while True:
        if Brax1 == 1:
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
                            Brax1 = 3
                            Hold2 = input('NEW PASSWORD: ')
                            if Hold2 == '%back': #used to go back
                                Brax1 = 2
                            elif len(Hold2) < 3: #char count
                                Brax1 = 0
                            elif '%' in Hold2 or '$' in Hold2 or '#' in Hold2 or '*' in Hold2 or '&' in Hold2 or '^' in Hold2 or '@' in Hold2: #spec. char check
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
                                    #additem('\n$User-' + Hold1 +'$ #' + Hold2 + '# *1*^\n$Users$ #' + Hold1 + '#^', 'append', '') #old format, fixed to insert $Users$
                                    additem('\n$User-' + Hold1 +'$ #' + Hold2 + '# *1* &M-' + Hold1 + '&^', '%append', '%NULL')
                                    additem(' #' + Hold1 + '#', '@', 0)
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
                            Brax1 = 1
                            break
                        else:
                            print(LineDash + "Invalid Password, please try again,\nto go back, please type '%back'")
                else:
                    print(LineDash + "Sorry, but it seems that Username does not Exist, please try again,\nto become a new user, please type in %NULL")
    ActUser = Hold1
    ActPass = Hold2
    Hold1 = (70 - len(ActUser))
    if Hold1 % 2 == 1:
        User2 = '-'
    else:
        User2 = ''
    ###User Dash (creates - with the User name inside of it, pretty cool)
    UserDash = ''
    for i in range(Hold1 // 2):
        UserDash += '-'
    UserDash += User2 + ' User: ' + ActUser + ' '
    for i in range(Hold1 // 2):
        UserDash += '-'
    UserDash += '\n'
    ###
    
    Brax1 = 2
    while True:  #The User Loop
        if Brax1 == 2:
            print(UserDash + "Password Accepted, Welcome to NumbLock!")
        else:
            print(UserDash + 'Welcome to NumbLock!')
        Brax1 = 0
        while True:
            Hold1 = input("\nPlease choose from one of the choices below:\nStart\nHelp\nExit\n\n")
            if Hold1 == 'Start' or Hold1 == 'Help' or Hold1 == 'Exit':
                break
            else:
                print(UserDash + 'Sorry, it Seems you Mistyped, Please try Again')
        if Hold1 == 'Start':
            print(UserDash[:len(UserDash) - 1])
            while True: #Start Loop
                finditem('$', '*', 'User-' + ActUser, '%NULL', '^')
                ActLvl = int(Return1)
                Hold1 = '\n'
                for i in range(ActLvl):
                    Hold1 = Hold1 +"Lvl-" + str((i + 1)) +" (" + LvlVal[i] + ")\n"
                print("Please Choose from one of the choices below (if you don't know what to do,\ntype %back and type in the option 'Help'):\n\nFreestyle (Lvl-" + str(ActLvl) + ")\nMissed" + Hold1)
                Hold1 = input()
                if Hold1 == '%back':
                    break
                elif Hold1 == 'Freestyle' or Hold1[0:4] == 'Lvl-' or Hold1[0:4] == 'LVL-' or Hold1[0:4] == 'lvl-':
                    
                    try: #trying to see if the user actually put in the correct input
                        if Hold1 != 'Freestyle':
                            Hold1 = str(int(Hold1[4]))
                            if int(Hold1) > ActLvl:
                                raise
                    except:
                        print(UserDash + "Sorry, it seems you mistyped.")
                    else:
                        print(UserDash[:len(UserDash) - 1])
                        while True: #Lvl Mode Loop


                            
                            if Hold1 != 'Freestyle':
                                Hold2 = input("Active Lvl: " + Hold1 + ", type '%back' to go back\nYou can choose between two modes, 'Relaxed' or 'Timed'\nYou will get a brief description of each after you type them in.\n\n")
                            else:
                                Hold2 = input("Active Mode: " + Hold1 + " (Lvl " + str(ActLvl) + "), type '%back' to go back\nYou can choose between two modes, 'Relaxed' or 'Timed'\nYou will get a brief description of each after you type them in.\n\n")
                            if Hold2 == '%back':
                                print(UserDash[:len(UserDash) - 1])
                                break
                            elif Hold2 == 'Relaxed' or Hold2 == 'RELAXED' or Hold2 == 'relaxed':
                                Hold2 = 'Relaxed'
                                Hold3 = input(UserDash +
"""In Relaxed mode, there is no time limit (it will still be recorded though)
You will be given 25 questions. You will be given a Countdown of 3 secs
before the program begins

Type 'Skip' to skip the question
Type 'End' to quit the program
The time will be given to you periodically

Type '%back' to go back, Type Anything else to Continue.\n\n""")
                                if Hold3 == '%back':
                                    print(UserDash[:len(UserDash) - 1])
                                else:
                                    #Lvl Relaxed
                                    RunLvl(Hold1, Hold2, ActUser)
                                    pass
                                pass
                            elif Hold2 == 'Timed' or Hold2 == 'TIMED' or Hold2 == 'timed':
                                Hold2 = "Timed"
                                Hold3 = input(UserDash +
"""In Timed mode, there will be a time limit of 1 minute, you will need to get
at least 23/25 questions correct to progress to the next Lvl, The Lvl
will end after that minute and your score will be given to you. You will
be given a Countdown of 3 secs before the program begins

Type 'Skip' to skip the question
Type 'End' to quit the program
The time will be given to you periodically

Type '%back' to go back, Type Anything else to Continue.\n\n""")
                                if Hold3 == '%back':
                                    print(UserDash[:len(UserDash) - 1])
                                    break
                                else:
                                    #RunLvl(LvlInd, LvlMode, ActUser)
                                    #Lvl Timed
                                    RunLvl(Hold1, Hold2, ActUser) #Timed
                                    pass
                            else:
                                print(UserDash + "It seems you mistyped")

                elif Hold1 == 'Missed':
                    pass
                else:
                    print(UserDash + "Sorry, it seems you mistyped.")
        elif Hold1 == 'Help':
            input(UserDash + Help) ###I worked pretty hard on this description of NumbLock, I think I did a good job
        elif Hold1 == 'Exit':
            Hold1 = input("Are you sure? You will go back to the Sign in Page\nType Yes to go back, type anything to not Exit\n")
            if Hold1 == 'Yes' or Hold1 == 'YES' or Hold1 == 'yes': #Just to make sure that the many variations of 'Yes' will actually work
                ActUser, ActPass, ActLvl, Hold1, Hold2, Hold3 = '', '', '', '', '', ''
                break













