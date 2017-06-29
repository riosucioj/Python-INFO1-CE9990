# making graph paper

import sys

r = int(input("How many rows of boxes? "))
c = int(input('How many columns of boxes? '))
sr = int(input('How many rows of spaces in each box? '))
sc = int(input('How many columns of spaces in each box? '))


a = 0                       #creating variable to test against header line.
while a < r:                #statement says a is less than rows entered. Will be false when a is greater than rows entered.
    b = 0                   #creating variable to test against header line.
    while  b < c            #statement being tested
        print("+", sc * "-", sep = "", end = "") #prints spaces because statement is true
        b += 1
    print()
    d = 0
    while d < sr:
        e = 0
        while e < c:
            print("|", sc * " ", sep = "", end = "")
            e += 1
        print()
        d += 1
    a += 1

    
sys.exit(0)


