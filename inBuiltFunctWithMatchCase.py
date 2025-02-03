# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 17:46:05 2025

@author: Bhushan
"""

print("--:MENU:--")
print("1: Length of function-->Len()")
print("2: Removing leading and trailing space-->strip()")
print("3: Printing in Uppercase-->upper()")
print("4: Printing in Lowercase-->lower()")
print("5: REplacing the value-->Replace()")
print("6: Spliting the string value-->split()")
print("7: search a perticular word-->find()")
print("8: check entered string is digit or not-->isdigit()")
print("enter your choice")
ch =int(input())

match ch:
    case 1:
        s = input("enter any string to find it's length please")
        length = len(s)
        print(f"the length of the entered string-->{s} is -->{length}")
    case 2:
        s = input("enter any string with space at the start and end ")
        print("The string including trailing and leading space is",s)
        print()
        temp=s.strip()
        print(f"The string after removal of trailing and leading space is-->{temp}")
    case 3:
        s = input("enter any string in lowercase please")
        print("the entered string is",s)
        print()
        temp = s.upper()
        print(f"the given string in uppercase is -->{temp}")
    case 4:
        s = input("enter the any string in uppercase")
        print(f"the entered string is -->{s}")
        print()
        temp = s.lower()
        print(f"the given string in lowercase is-->{temp}") 
    case 5:
        s = input("enter any string please")
        print("the entered string is",s)
        print()
        c = input("enter the characters you want to replace")
        r = input("enter the value of replacement ")
        temp=s.replace(c,r)
        print("the resulted string after replacement is",temp)
    case 6:
        s = input("Please enter any string")
        print("the entered string is",s)
        print()
        c = input("enter the characters based on which one to split in the given string--{s}")
        temp = s.split(c)
        print()
        print(f"the result is-->{temp}")
    case 7:
        s = input("enter any string please")
        print("the entered string is",s)
        print()
        c = input("enter word that you want to search")
        temp = s.find(c)
        print("the result is",temp)
    case 8:
        s = input("enter any string")
        print("the entered string is",s)
        print()
        b = isdigit(s)
        if b == True:
            print("the given string is digit")
        else:
            print("the given string is not digit")
            
    case default:
        print("Sorry,enter choice is invalid")

            


