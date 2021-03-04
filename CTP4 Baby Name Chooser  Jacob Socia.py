import random


gender = ['Male','Female']

babyNamesMale = ['Charlie',
            'Jake',
            'Henry',
            'Ben',
            'Juan',
            'Jack',
            'George']


babyNamesFemale = ['Kate',
            'Bella',
            'Claudia',
            'Addy',
            'Ava',
            'Mia',
            'Sophia']


player1 = [ ]
nametoGive = [ ]


genderOfBaby = input("Hey you! Whats the gender of your baby?    ")

try:
    if genderOfBaby == "Female":
        print("I'll give you your female baby names".format(nametoGive))

    if genderOfBaby == "Male":
        print("I'll give you your Male baby names".format(nametoGive))
    else:
        print("Please pick a gender.   ")

except ValueError:
    print("Caught the error!")

nametoGive = input("How many names should I give to you?   ")

try:
    if int(nametoGive) > 0:
        print("I'll give you {} baby names".format(nametoGive))
        for x in range(0, int(nametoGive)):
            babyNamesMale = babyNamesMale.pop(random.randint(0,len(babyNamesMale)))
            player1.append(babyNamesMale)
        print(player1)
    else:
        print("Else print")
except ValueError:
    print("Caught the error!")

#Didn't finish my code completely, but It's like 80% done just ran into an error that I got stuck on.

#ERROR=Traceback (most recent call last):File "C:\Users\jacob.socia_thecubed\Downloads\CTP4 Baby Name Chooser  Jacob Socia.py", line 48, in <module>babyNamesMale = babyNamesMale.pop(random.randint(0,len(babyNamesMale)))AttributeError: 'str' object has no attribute 'pop'


