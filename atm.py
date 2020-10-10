from gtts import gTTS
import os
from os import system, name
import sys
from random import randint

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


mytext = 'welcome to this session. Please login with new account'
language = 'hi'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("welcome.mp3")

os.system("mpg321 welcome.mp3")

_ = system('clear')


username1 = raw_input("please enter your username : ")
password1 = raw_input("please enter your password : ")
mytext0 = 'welcom again' + username1 + "now you are logged in with your new account and password"
language= 'hi'

myobj0 = gTTS(text=mytext0, lang=language, slow=False)

myobj0.save("username.mp3")

os.system("mpg321 username.mp3")

_ = system('clear')


print("Hellow " + username1 + " you are now logged in with a password")


mytext1 = 'please type exit for verification of login and to enter ATM process. or enter any key to go out  from this session'
language = 'hi'
myobj1 = gTTS(text=mytext1, lang=language, slow=False)

myobj1.save("audio.mp3")

os.system("mpg321 audio.mp3")

_ = system('clear')

command = raw_input("please logoff for further verfication  \nto logoff type exit: ")
if command == "exit":
        print("You are loged off now")

else:
        exit()

mytext2 = 'please re enter the username and password that you created earlier'
language = 'hi'
myobj2 = gTTS(text=mytext2, lang=language, slow=False)

myobj2.save("new.mp3")

os.system("mpg321 new.mp3")

_ = system('clear')

username = raw_input("Please enter your username : ")
password = raw_input("Please enter your password : ")

attempt = 0


while username != username1 or password != password1:
        if attempt > 2:
                 mytext32 = 'sorry continues three unsuccessful attempts pleas try again later'
                 language = 'hi'
                 myobj32 = gTTS(text=mytext32, lang=language, slow=False)

                 myobj32.save("sorry.mp3")

                 os.system("mpg321 sorry.mp3")

                 _ = system('clear')

                 print("more than 3 attempts")
        sys.exit()

        attempt = attempt + 1
        mytext3 = 'sorry!! the password or username does is not matching. please re enter the username and password'
        language = 'hi'
        myobj3 = gTTS(text=mytext3, lang=language, slow=False)

        myobj3.save("verification.mp3")

        os.system("mpg321 verification.mp3")

        _ = system('clear')
        print("sorry username or password is incorrect please re-enter for validation ")
        username = raw_input("Please enter your username : ")
        password = raw_input("Please enter your password : ")



else:
        #print ("Your account number is: ")
        #print random_with_N_digits(12)
        mytext4 = 'login is successful' + username1 + 'Your Account Number is generated note down your account number'
        language = 'hi'
        myobj4 = gTTS(text=mytext4, lang=language, slow=False)

        myobj4.save("greeting.mp3")

        os.system("mpg321 greeting.mp3")
        print ("Your account number is: ")
        print random_with_N_digits(12)


        #_ = system('clear')

print(username + ", Thank you for creating an account")

mytext5 = 'please enter the amount to be deposited in your account'
language = 'hi'
myobj5 = gTTS(text=mytext5, lang=language, slow=False)

myobj5.save("deposit.mp3")

os.system("mpg321 deposit.mp3")

_ = system('clear')

balance = float(raw_input("Enter the amount to be deposited in your account : "))


mytext6 = 'please enter the option given below of your favour'
language = 'hi'
myobj6 = gTTS(text=mytext6, lang=language, slow=False)

myobj6.save("ver.mp3")

os.system("mpg321 ver.mp3")

_ = system('clear')
def printMenu():
        print("Please choose an option below : ")
        print("""Enter b to check your Balance \nEnter d to deposite money into your account \nEnter w to withdraw money from your account \nEnter q to quit the session""")


def getTransaction():
        transaction = str(raw_input("what would you like to do? "))
        return transaction

def withdraw(bal, amt):
        global balance
        balance = bal-amt
        if balance<0:
                balance = balance-10

def formatCurrency(amt):
        return "$%.2f" %amt

printMenu()
command = str(getTransaction())

while command != "q":
        if(command == "b"):
                mytext7 = 'your current balance is' + formatCurrency(balance)
                language = 'hi'
                myobj7 = gTTS(text=mytext7, lang=language, slow=False)

                myobj7.save("bal.mp3")

                os.system("mpg321 bal.mp3")

                _ = system('clear')

                print(username + "Your current balance is", formatCurrency(balance))
                printMenu()
                command = str(getTransaction())
                _ = system('clear')

        elif(command == "d"):
                mytext8 = 'Enter the amount to be deposited'
                language = 'hi'
                myobj8 = gTTS(text=mytext8, lang=language, slow=False)

                myobj8.save("dep.mp3")

                os.system("mpg321 dep.mp3")

                _ = system('clear')

                amount = float(raw_input("Enter the amount : "))

                balance = balance+amount
                printMenu()
                command = str(getTransaction())
                _ = system('clear')


        elif(command == "w"):
                mytext9 = 'Enter the amount to be withdraw from your account'
                language = 'hi'
                myobj9 = gTTS(text=mytext9, lang=language, slow=False)

                myobj9.save("wit.mp3")

                os.system("mpg321 wit.mp3")

                _ = system('clear')

                amount = float(raw_input("Please enter the amount to be withdraw: "))

                withdraw(balance, amount)
                printMenu()
                command = str(getTransaction())
                _ = system('clear')
        else:
                mytext10 = 'Invalid command. Please enter the options given below'
                language = 'hi'
                myobj10 = gTTS(text=mytext10, lang=language, slow=False)

                myobj10.save("invl.mp3")

                os.system("mpg321 invl.mp3")

                _ = system('clear')
                print("Incorrect command. Please try again. ")
                printMenu()
                command = str(getTransaction())
                _ = system('clear')

print("Goodbye! " + username + " see you again soon")
