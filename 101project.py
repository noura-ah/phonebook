import ast

dict = {1111111111: "Amal", 2222222222: "Mohammed", 3333333333: "Khadijah",
        4444444444: "Abdullah", 5555555555: "Rawan", 6666666666: "Faisal",
        7777777777: "Layla"}


def searchByPhone():
    num = input("enter phone number:")
    if int(num) in dict:
        print(dict.get(int(num)))
    elif len(num) != 10:
        print("This is invalid number")
    else:
        print("Sorry, the number is not found")


def searchByName():
    name = input("search by name:")
    num = [l for [l, x] in dict.items() if name == x]
    if num == []:
        print("Sorry, the name is not found ")
    else:
        print(num.pop())

def addNum():
    num = input("enter a new phone number:")
    if len(num) != 10:
        print("This is invalid number")
    elif not num.isdigit():
        print("Sorry, you did not enter phone number")
    elif int(num) in dict:
        print("number is already exist")
    else:
        name = input("enter the name of the person who had the phone number:")
        dict[num] = name


class file():
    def __init__(self, path=None):
        self.path = path

    def createPhonebook(self):
        with open(self.path, "w+") as f:
            f.write(str(dict))

    def readPhonebook(self):
        with open(self.path, 'r') as f:
            s = f.read()
            self.whip = ast.literal_eval(s)
            return self.whip


file = file()
file.path="phonebook.txt"
import os
if os.path.isfile(file.path):
    dict=file.readPhonebook()
else: file.createPhonebook()


while True:
    inp= input("enter function (add) to add new phone number,\r\n(print) to print list of numbers, \
               \r\n(search by name), (search by number) or (finish):")
    if inp=="add":
        addNum()
        file.createPhonebook()
    elif inp=="print":
        for i in dict.items():
            print(i)
    elif inp=="search by name":
        searchByName()
    elif inp=="search by number":
        searchByPhone()
    elif inp=="finish":
        break
    else:
        print("wrong entry")
        end=input("Do you want to end the program?y/n:")
        if end=="y":
            break

