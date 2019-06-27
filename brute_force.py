import time
import itertools
import getpass
import sys
Alphabet = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890`~!@#$%^&*()_+-={}[]|\:;"'<>?,./\|')
alphabet = "abcdefghijklmnopqrstuvwxyz"
dictionary = open("dictionary.txt")
most = open("thousandpassword.txt")
text = most.read().strip().split()
text1 = dictionary.read().strip().split()
file2 = open("thousandpassword.txt" , "a")
f = 0
z = 0

Password = getpass.getpass("What is your password?\n")

start = time.time()

counter = 1

CharLength = 1

def slow_type(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)


#comparing Password to most common passwords and english words
slow_type("""Starting dictionary 'attack'
""")
while True:
    if Password == "":
        continue
    if Password in text:
        f = f + 1
        break
    else:
        break

while True:
    if Password == "":
        continue
    if Password in text1:
        z = z + 1
        break
    else:
        break

if f ==1 and z ==1:
    end = time.time()
    timetaken = end - start
    time.sleep(3)
    print("Found it in ", timetaken, " seconds")
    time.sleep(2)
    sys.exit("""\033[31mEnd of Code
    
    
    
    
    """)
elif f == 1:
    end = time.time()
    timetaken = end - start
    time.sleep(3)
    print("Found it in ", timetaken, " seconds")
    time.sleep(2)
    sys.exit("""\033[31mEnd of Code




        """)
elif z == 1:
    end = time.time()
    timetaken = end - start
    time.sleep(3)
    print("Found it in ", timetaken, " seconds")
    time.sleep(2)
    sys.exit("""\033[31mEnd of Code




        """)
elif
# If it doesn't work, time to brute force
slow_type("Starting brute force...")
for CharLength in range(25):

    passwords = (itertools.product(Alphabet, repeat=CharLength))
    for i in passwords:
        counter += 1
        i = str(i)
        i = i.replace("[", "")
        i = i.replace("]", "")
        i = i.replace("'", "")
        i = i.replace(" ", "")
        i = i.replace(",", "")
        i = i.replace("(", "")
        i = i.replace(")", "")

        if i == Password:

            end = time.time()

            timetaken = end - start

            print("Found it in ", timetaken, " seconds and ", counter, "attempts")

            print(i)
            print("Press enter when you have finished")

            sys.exit()

