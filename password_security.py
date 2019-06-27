import string
import re
import sys
import time
import random
import getpass
s = 0
n = 0
l = 0
u = 0
f = 0
z = 0

file1 = open("variable", "w")
file2 = open("variable", "r")
lines = file2.readlines()
counter = 0
typing_speed = 50 #wpm
fobj = open("thousandpassword.txt")
text = fobj.read().strip().split()
fobj2 = open("dictionary.txt")
text1 = fobj2.read().strip().split()
file = open("passwords.txt", "a")

symbols = (string.punctuation)
numbers = (string.digits)
lowercase = (string.ascii_lowercase+ "ñ")
uppercase = (string.ascii_uppercase+ "Ñ")
symbol_list = [x for x in symbols]
number_list = [x for x in numbers]
lowercase_list = [x for x in lowercase]
uppercase_list = [x for x in uppercase]
password = ""
#functions
def is_symbol(character):
    if (ord(ch) > 32 and ord(ch) < 48) or (ord(ch) > 57 and ord(ch) < 65) or (ord(ch)> 90 and ord(ch) < 97) or (ord(ch) > 122 and ord(ch) <127):
        return True

def is_number(character):
    if (ord(ch) > 47 and ord(ch) < 58):
        return True

def is_lowercase(character):
    if (ord(ch) > 96 and ord(ch) < 123):
        return True

def is_uppercase(character):
    if (ord(ch) > 64 and ord(ch) < 91):
        return True

def slow_type(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

def cons(password):
    if len(password) <= 5:
        print("Password is too short, try adding a few symbols , uppercase letters ,lowercase letters or numbers")
    #1
    elif security_s(s) == True and security_n(n) == True and security_l(l) == True and security_u(u) == True:
        print("""The password is very secure, if you want to make it even more secure make it longer""")
    #2
    elif security_s(s) == True and security_n(n) == True and security_l(l) == True and security_u(u) == False :
        print("The password is secure, try adding uppercase letters to make it even more secure")
    #3
    elif security_s(s) == True and security_n(n) == True and security_l(l) == False and security_u(u) == False :
        print("The password is secure, make it better by adding lowercase and uppercase letters to make it even more secure")
    #4
    elif security_s(s) == True and security_n(n) == True and security_l(l) == False and security_u(u) == True :
        print("""The password is secure, if you want to make it even more secure make it longer and add lowercase letters""")
    #5
    elif security_s(s) == True and security_n(n) == False and security_l(l) == True and security_u(u) == True :
        print("""The password is secure, if you want to make it even more secure make it longer and add numbers""")
    #6
    elif security_s(s) == True and security_n(n) == False and security_l(l) == True and security_u(u) == False:
        print("""The password is not too secure, try adding uppercase letters and numbers to make it better""")
    #7
    elif security_s(s) == True and security_n(n) == False and security_l(l) == False and security_u(u) == True :
        print("""The password is not too secure, try adding lowercase letters, uppercase letters and numbers""")
    #8
    elif security_s(s) == True and security_n(n) == False and security_l(l) == False and security_u(u) == False :
        print("""The password is not secure, try adding lowercase letters, uppercase letters and numbers""")
    #9
    elif security_s(s) == False and security_n(n) == True and security_l(l) == True and security_u(u) == True :
        print("""The password is secure, but you might want to add symbols to make it better""")
    #10
    elif security_s(s) == False and security_n(n) == True and security_l(l) == True and security_u(u) == False :
        print("""The password is not too secure, add uppercase letters and symbols to make it even better""")
    #11
    elif security_s(s) == False and security_n(n) == True and security_l(l) == False and security_u(u) == True :
        print("""The password is not too secure, add lowercase letters and symbols to make it even better""")
    #12
    elif security_s(s) == False and security_n(n) == True and security_l(l) == False and security_u(u) == False:
        print("""The password is not secure, add lowercase and uppercase letters, and symbols to make it secure""")
    #13
    elif security_s(s) == False and security_n(n) == False and security_l(l) == True and security_u(u) == False :
        print("""The password is not  secure, add uppercase letters, symbols and numbers """)
    #14
    elif security_s(s) == False and security_n(n) == False and security_l(l) == False and security_u(u) == True :
        print("""The password is not secure, add lowercase letters, numbers and symbols to make it secure""")
    #15
    elif security_s(s) == False and security_n(n) == False and security_l(l) == True and security_u(u) == True :
        print("""The password is not too secure, add numbers and symbols to make better""")

for line in lines:
        conv_int = int(line)
        counter = conv_int + 1
print("""Information:
-This code will ask you your password, if anyone should somehow get access to it, we will not be responsible for it
-Follow the instructions this code says closely to avoid any security issues
-This code works only for passwords including:
    -uppercase letters in the english alphabet
    -lowercase letters
    -the 32 standard special characters
    -numbers""")
while True:
    yes_no = input("\033[1;37m Do you accept this terms and want to continue(Yes/No) \n")
    if yes_no == "Yes" or yes_no == "yes" or yes_no == "Y" or yes_no == "y":
        print("Continuing")
        break
    elif yes_no == "No" or yes_no == "N" or yes_no == "n" or yes_no == "no":
        sys.exit("Not continuing")
    else:
        print("\033[1;31m Please answer with Yes or No \n ")


while True:
    password = getpass.getpass("\033[1;37mEnter your password \n")
    if len(password) >= 5:
        slow_type("Password is being compared to the 100 thousand most used passwords and to english words...")
        break
    else:
        print("\033[1;31m Please answer with a password with at least five characters \n ")

for line in lines:
        conv_int = int(line)
        counter = conv_int + 1

file.write("""---
The password that was used was:""" + password)

file1.write(str(counter))
for ch in password:
    if is_symbol(ch):
        s = s + 1
    else:
        s = s + 0

for ch in password:
    if is_number(ch):
        n = n + 1
    else:
        n = n + 0

for ch in password:
    if is_lowercase(ch):
        l = l + 1
    else:
        l = l + 0

for ch in password:
    if is_uppercase(ch):
        u = u + 1
    else:
        u = u + 0


#print(s)
#print(n)
#print(l)
#print(u)


def security_s(s):
    if s >= 1:
        return True
    else:
        return False


def security_n(n):
    if n >= 1:
        return True
    else:
        return False


def security_l(l):
    if l >= 1:
        return True
    else:
        return False


def security_u(u):
    if u >= 1:
        return True
    else:
        return False

#print(security_s(s))
#print(security_n(n))
#print(security_l(l))
#print(security_u(u))


while True:
    if password == "":
        continue
    if password in text:
        f = f + 1
        break
    else:
        break

while True:
    if password == "":
        continue
    if password in text1:
        z = z + 1
        break
    else:
        break

time.sleep(5)
if f == 1 and z == 1:
    slow_type("""
    Your password is one of the million most used passwords and it is also an english word: """)
    time.sleep(3)
    print( """
    -This means that it would take a hacker less than a minute to get your password by running a dictionary attack""")
    time.sleep(3)
    print("""\033[1;31m
    - WE STRONGLY RECOMMEND YOU TO CHANGE YOUR PASSWORD \n""")
    sys.exit("End of the code")
elif f == 1:
    slow_type("Your password is one of the million most used passwords: ")
    time.sleep(3)
    print("-This means that it would take a hacker less than a minute to get your password by running a dictionary attack")
    time.sleep(3)
    print("\033[1;31m- WE STRONGLY RECOMMEND YOU TO CHANGE YOUR PASSWORD \n")
    sys.exit("End of the code")
elif z == 1:
    slow_type("Your password is an english word")
    time.sleep(3)
    print(
        "-This means that it would take a hacker less than a minute to get your password by running a dictionary attack")
    time.sleep(3)
    print("\033[1;31m- WE STRONGLY RECOMMEND YOU TO CHANGE YOUR PASSWORD \n")
else:
    slow_type("""
Your password is not one of the million most common passwords, Well Done!!""")
    slow_type("""
........................................Analyzing password...........................................

""")
    time.sleep(7)
    cons(password)


time.sleep(2)

#slow_type("""This is the end of the code
#""")
slow_type("""Credits:
""")
slow_type("""Made by:\033[1;32m Marcos Urgoiti 
\n""")
slow_type("""\033[1;37mProgrammed with:\n \033[1;32mPython 3.7.1 \n""")
print("""























|""")
slow_type("""-------------------------------------------------------------------------------------------------------""")



file.close()