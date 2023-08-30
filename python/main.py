# print("i love maggi")
# name="varshu"
# print("hi"+name)
# print(type(name))
# first_name="akshaya"
# last_name="sri"
# full_name=first_name+last_name
# print(full_name)
# print(type(full_name))
# age=17
# age+=1
# print(age)
# print("your age is:"+str(age))
# print(float(age))
# human= True
# print("are you a human?:"+str(human))
# print(////////////////////)
# multiple assignment allows to assign variables at a time
# age=akshaya = shero= alekya= 18
# print(age)
# print(akshaya)
# print(////////////////////)
# string methods
# name="shero"
# print(len(name))
# print(name.find("e"))
# print(name.upper())
# print(name.isdigit())
# print(name.isalpha())
# print(name.count("o"))
# print(name.replace("s",""))
# print(name*4)
# print(////////////////////)
# type casting
# m=1
# n=2.3
# o="9"
# n=int(n)
# o=int(o)
# print(m)
# print(n)
# print(o)
# print(o*4)
# we can only concat a string and a string not with any other data type
# print(////////////////////)
# user input
# name=input("what is your name?:")
# age=int(input("how old are you?:"))
# age=age+1
# print("hello"+name)
# print(////////////////////)
# import math
# pi=3.14
# x=2
# y=5
# z=8
# print(round(pi))
# print(math.ceil(pi))
# print(math.floor(pi))
# print(abs(pi))
# print(pow(pi,2))
# print(math.sqrt(420))
# print(min(x,y,z))
# print(////////////////////)

# slicing [start:stop:step]

# name="akshaya sri"
# first_name=name[0:7]
# print(first_name)
# last_name=name[8:11]
# print(last_name)
# funky_name=name[::5]
# print(funky_name)
# reversed_name=name[::-1]
# print(reversed_name)


"""
website="http://google.com"
slice=slice(7,-4)
print(website[slice])
"""
# conditional loops
"""
age=int(input("how old are you?:"))
if age>=18:
    print("you are an adult")
elif age==100:
    print("century !!")
elif age<0:
    print("you are not even born yet!!")
else:
    print("you are a child")
 """
"""
#logical operators (and,or,not)
temp=int(input("what is the temperature outside?:"))
if temp>0 and temp<=30:
    print("take a chill pill buddy!😎")
    print("go outside!")
elif temp<0 or temp>30:
    print("it's extreme ,don't go outside!🫥😐" )
"""
"""
temp=int(input("what is the temperature outside?:"))
if not temp>0 and temp<=30:
    print("it's extreme ,don't go outside!🫥😐")
elif not temp<0 or temp>30:
    print("it's extreme ,don't go outside!🫥😐" )
    print("take a chill pill buddy!😎")
    print("go outside!")
"""
# while loop
"""
while 1==1:
    print("help! I am stuck in a loop")
"""
"""
name=""
while len(name)==0:
    name=input("enter your name:")
    print("hello"+name)
"""
# for loop
# while loop:infinite times, for loop:limited times
"""
for i in range(10):
    print(i+1)
    for x in range(0,20):
       print(x+1)
"""
"""
for x in range(0,20):
       print(x+1)
"""
"""
for x in range(0,20,2):
       print(x+1)
for m in "bro code":
    print(m)
"""
"""
import time
for second in range(10,0,-1):
    print(second)
    time.sleep(1)
print("happy new year!")
"""
# nested loops
"""
rows=int(input("how many rows?:"))
coloumns=int(input("how many coloumns?:"))
symbol=input("enter a symbol to use:")
"""
"""
for i in range(rows):
    for j in range(coloumns):
        print(symbol,end="")
    print()
"""
# loop control statments
"""
while True:
    name=input("enter your name:")
    if name !="":
       break
"""
"""
phone_number="123-456-789"
for i in phone_number:
    if i=="-":
        continue
    print(i,end="")
#end=""-> this is for appearing in one single line, if that is not used each letter appears in a differnt line.
"""
"""
for i in range(1,20):
    if i==13:
        pass
    else:
        print(i)
"""
# lists

# food = ['pizza', 'burger', 'noodles', 'ice cream']
# print(food[1])
# food[0] = "sushi"
# print(food[0])
"""
for x in food:
    print(x)
"""

# food = ['pizza', 'burger', 'noodles', 'ice cream']
# food.remove('pizza')

# print(food)
# food.pop()
# food.insert(0, 'cake')
# food.sort()
# food.clear()

# 2d lists

# drinks = ["coffee", "soda", "tea"]
# dinner = ["pizza", "hamburger", "hotdog"]
# deserts= ["cake", "icecream"]
# food = [drinks, dinner, deserts]
# print(food[2][0])

# tuples
# student = ("akki", 18, "female")
# print(student.count("akki"))
# print(student.index("female"))

# for x in student:
#   print(x)

#  if "akki" in student:
#  print("akki is here")

# set
# utensils = {"spoon", "knife", "fork"}
# dishes = {"bowl", "plate", "cup", "knife"}
# print(dishes.difference(utensils))
# print(utensils.intersection(dishes))
# utensils.add("jar")
# utensils.remove("spoon")
# utensils.clear()
# dinner_table = utensils.union(dishes)
# for x in utensils:
#   print(x)
# for x in dinner_table:
#  print(x)

# DICTIONARY = A CHANGEBALE, UNORDERED COLLECTION OF UNIQUE KEY: VALUE PAIRS FAST BECAUSE THEY USE HASHING, ALLOW US TO ACESS A VALUE QUICKLY
'''
capitals = {'USA': 'washington DC',
            'INDIA': 'New Delhi',
            'Russia': 'Moscow'}
capitals.update({'Germany': 'Berlin'})
capitals.update({'USA': 'las vegas'})
capitals.pop('INDIA')
capitals.clear()

#print(capitals['Russia'])
#print(capitals.get('germany'))
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())

for key, value in capitals.items():
   print(key, value)
'''
# index operator[]

# name = "akshaya sri"

# if(name[0].islower()):
# name = name.capitalize()
# first_name = name[0:3].upper()
# last_name = name[4:].lower()
# last_character = name[-2]
# print(last_name)
# print(last_character)

# print(~~~~~~~~~~~~~~~~~~~~~~~~~~)
# FUNCTIONS = a block of code which is executed
#            only when it is called.

# def hello(name):
#    print("hello"+name)
#    print("have a nice day")
# hello()
# name = "dude"
# hello(name)
# hello("akshaya")
# hello("dude")

# def hello(first_name,last_name,age):
#    print("hello"+first_name+last_name)
#    print("you are"+str(age)+"years old")
#    print("have a nice day")
# hello("bro","code",21)

# RETURN STATEMENTS = FUNCTIONS SEND PYTHON VALUES/ OBJECTS BACK
#                   TO THE CALLER. THESE VALUES ARE KNOWN AS THE FUNCTION'S RETURN VALUE

# def multiply(number1,number2):
#    result = number1*number2
#    return result
# x = multiply(6,8)
# print(x)

# KEYWORDS:THE ORDER OF PARAMETER DO NOT MATTER
'''
def hello(first,middle,last):
    print("hello"+first+middle+last)

hello(first="arasada",middle="akshaya",last="sri")
'''
'''
#nested function calls
print(round(abs(float(input("enter a whole number:")))))
'''
'''
#SCOPE= THE REGION THAT A VARIABLE IS RECOGNISED
name = "code"  #global scope
def display_name():
    name = "hi"  #local scope
    print(name)
display_name()
print(name)
#HERE 🐍 USES LEGB RULE I.E, LOCAL, ENCLOSING , GLOBE ,BUILT-IN
'''

# *args = PARAMETER THAT WILL PACK ALL ARGUMENTS INTO A TUPLE
#        USEFUL SO THAT FUNCTION CAN ACCEPT A VARYING AMOUNT OF ARGUMENTS
'''
def add(num1, num2):
    sum = num1 + num2
    return sum

print(add(1,2,3))  #here you can only pass 2 arguments , so we use *args we can pass variable number of arguments
'''
'''
def add(*args):
    sum= 0
    args = list(args)
    args[0]=0
    for i in args:
        sum += i
    return sum
print(add(1,2,3,4,5,6,7))
'''


# **kwargs = parameter that will pack arguments into a dictionary
#            useful so that a function can accept a varying amount of keyword arguments
'''
def hello(**kwargs):
    print("hello " + kwargs['first'] + " " + kwargs['last'])
    print("hello", end=" ")

hello(first="bro", middle="dude", last="code")
'''

# str.format()
'''
animal = "cow"
item = "moon"
print("the {} jumped over {} ".format(animal,item)) #positional argument
print("the {1} jumped over {0} ".format(animal,item)) # keyword argument
print("the {animal} jumped over {animal} ".format(animal = "cow",item ="moon")) # keyword argument
'''
'''
name = "bro"

print("hello, my name is {}".format(name))
print("hello, my name is {:10}. nice to meet you".format(name))
print("hello, my name is {:<10}. nice to meet you".format(name))
print("hello, my name is {:>10}. nice to meet you".format(name))
print("hello, my name is {:^10}. nice to meet you".format(name))
'''

#str.format()
'''
number = 1000
print("the number is {:.3f}".format(number))
print("the number is {:,}".format(number))
print("the number is {:b}".format(number))
print("the number is {:o}".format(number))
print("the number is {:x}".format(number))
print("the number is {:E}".format(number))
'''
'''
# RANDOM NUMBERS

import random

#x = random.randint(1,6)
#mylist = ['rock','paper' , 'scissors']
#z = random.choice(mylist)
#print(z)

cards = [1, 2, 3, 4, 5, "j", "q", "k", "a"]
random.shuffle(cards)
print(cards)
'''



# exception = events detected during execution that interrupt the flow of a programm
'''
try:
     numerator = int(input("enter a number to divide: "))
     denominator = int(input("enter a number to divide by: "))
     result = numerator / denominator
     print(result)
except zerodivisionerror as e:
    print(e)
    print("u cant divide with 0 idiot!!")
except Exception:
    print("something went wrong :")
else:
    print(result)
finally:
    print("this will always excecute")
  '''
'''
import os

path = "A:\\akshaya.txt"

if os.path.exists(path):
    print("That location exists")
    if os.path.isfile(path):
        print("that is a file")
elif os.path.isdir(path):
    print("that is a directory!")



else:
    print("That location does not exist")
'''
'''
try:
  with open('A:\example.txt') as file:
       print(file.read())
except FileNotFoundError:
    print("that file was not found")
   '''
'''
text = "girl"
with open('A:\example.txt','w') as file:
    file.write(text)
'''
'''
#copyfile() = copies content of a file
#copy() = copyfile()+ permission mode + destination can be a directory
#copy2() = copy()+ copies metadata ( file's creation and modification times)
import shutil
shutil.copyfile('A:\example.txt','A:\copy.txt')
'''
'''
import os

source = "C:\\Users\\akshaya sri arasada\\Pictures\\test.txt"
destination = "C:\\Users\\akshaya sri arasada\\Desktop\\test.txt"

try:
    if os.path.exists(destination):
       print("there is already a file there")
    else:
        os.replace(source,destination)
        print(source+"was moved")


except FileNotFoundError:
    print(source+" was not found")
'''
'''
import os
path = "A:\\achamma.txt"
os.remove(path)
'''
'''
import os
path = "C:\\Users\\akshaya sri arasada\\Desktop\\empty folder"


try :
    #os.remove(path) # delete a file
     os.rmdir(path)  #removes an empty directory
    #shutil.rmtree(path)  #delete a directory containg files **dont do it its dangerous.
except FileNotFoundError:
    print("file not found")
except PermissionError:
    print("you do not have permission to delete it")
else:
    print(path+"was deleted")
'''
#modules
'''
import messages

messages.hello()
messages.bye()
'''
'''
from messages import*
hello()
bye()
'''
'''
import messages as msg
msg.hello()
msg.bye()
'''
'''
help("modules")
'''
'''
import random
choices = ["rock","paper","scissors"]
computer = random.choice(choices)
print(computer)
'''
'''
#rock,paper,scissor game

import random


choices = ["rock","paper","scissors"]
computer = random.choice(choices)
player = None
while player not in choices:
    player = input("rock, paper, scissors?:").lower()
if player== computer:

   print("computer:", computer)
   print("player:" ,player)
   print("tie!!")
elif player =="rock":
    if computer == "paper":
       print("computer:",computer)
       print("player:",player)
       print("you loose!")
    if computer == "scissors":
        print("computer:",computer)
        print("player:",player)
        print("you win!!")
elif player =="scissors":
    if computer == "rock":
       print("computer:",computer)
       print("player:",player)
       print("you win!")
    if computer == "paper":
        print("computer:",computer)
        print("player:",player)
        print("you win!!")
elif player =="paper":
    if computer == "scissors":
       print("computer:",computer)
       print("player:",player)
       print("you loose!")
    if computer == "rock":
        print("computer:",computer)
        print("player:",player)
        print("you win!!")
'''
'''
#quiz game
#------------------------
def new_game():
    guesses = []
    correct_gusses = 0
    question_num = 1

    for key in questions:
        print("------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A,B,C,OR D):")
        guess = guess.upper()
        guesses.append(guess)
        correct_gusses += check_answer(questions.get(key),guess)
        question_num += 1

    display_score(correct_gusses,guesses)

#------------------------
def check_answer(answer, guess):
    if answer == guess:
        print("✅")
        return 1
    else:
        print("❌")
        return 0
#------------------------
def display_score(correct_guesses, guesses):
    print("------------------------")
    print("RESULTS")
    print("------------------------")
    print("Answers:",end="")
    for i in questions:
        print(questions.get(i),end=" ")
    print()

    print("Guesses:", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("your score is:"+str(score)+"%")
#------------------------
def play_again():
  response = input("do you wanna play again? (yes or no):")
  response = response.upper()

  if response == "YES":
     return True
  else:
      return False




questions = {
    "who created python?": "A",
    "what year was python created?": "B",
    "Python is tributed to which comedy group?" : "B",
    "Is the earth around?": "A"

}
options = [["A.guido van rossum" ,"B. Elon musk"],
           ["A.1989" ,"B.1991"],
           ["A. lonely island" , "B. Monty python"],
           ["A. True" , "B. False"]]

new_game()

while play_again():
    new_game()
print("BYEEE🙋‍♂️")
'''

'''
#OBJECT ORIENTED PROGRAMMING

from Car import Car

car_1 = Car("Chevy","Corvette","2021","blue")
car_2 = Car("Ford", "mustang", "2022","red")
print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)

car_2.drive()
car_2.stop()
'''

'''
from Car import Car
#car_1 = Car("Chevy","Corvette","2021","blue")
#car_2 = Car("Ford", "mustang", "2022","red")

#print(car_1.wheels)
#print(car_2.wheels)
print(Car.wheels)
'''
'''
#INHERITANCE
class Animal:
    alive = True
    def eat(self):
        print("this animal is eating")
    def sleep(self):
        print("this animal is sleeping")
class Rabbit(Animal):
    def run(self):
        print("this rabit is running")
class Fish(Animal):
    def swim(self):
     print("this fish can swim")
class Hawk(Animal):
    def fly(self):
     print("this hawk can fly")
rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
#fish.eat()
fish.swim()
hawk.fly()
rabbit.run()
'''

#MULTI LEVEL INHERITANCE
'''
class Organism:
    alive = True

class Animal(Organism):
    def eat(self):
        print("this animal is eating")
class Dog(Animal):
    def bark(self):
        print("this dog is barking")
dog = Dog()
print(dog.alive)
dog.eat()
dog.bark()
'''
'''
#MULTIPLE INHERITANCE

class Prey:
    def flee(self):
        print("this animal flees")
class Predator:
    def hunt(self):
        print("this animal is hunting")

class Rbbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey,Predator):
    pass

rabbit = Rbbit()
hawk = Hawk()
fish = Fish()

#rabbit.flee()
#hawk.hunt()

fish.flee()
fish.hunt()
'''
'''
#method overwriting
class Animal:
    def eat(self):
        print("this animal is eating")
class Rabbit(Animal) :
    def eat(self):
        print("this rabbit is eating a carrot")

rabbit = Rabbit()
rabbit.eat()
'''
'''
#method chaining

class Car:
    def turn_on(self):
        print("you start the engine")
        return self
    def drive(self):
        print("you drive the car")
        return self
    def brake(self):
        print("you step on the brakes")
        return self
    def turn_off(self):
        print("you turn off the engine")
        return self

car = Car()
#car.turn_on().drive()
#car.brake().turn_off()
(car.turn_on()\
 .drive()\
 .brake()\
 .turn_off())
'''
'''
#super()
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)  # A square's length and width are the same
    def area(self):
        return self.length * self.width

class Cube(Square):  # Cube is a specific type of square
    def __init__(self, side):
        super().__init__(side)
    def volume(self):
        return self.length ** 3

square = Square(3)
print(square.area())

cube = Cube(3)
print(cube.volume())
'''

#abstract class
# Prevents a user from creating an object of that class
# + compels a user to override abstract methods in a child class

# abstract class = a class which contains one or more abstract methods.
# abstract method = a method that has a declaration but does not have an implementation.
'''
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("You drive the car")

    def stop(self):
        print("This car is stopped")

class Motorcycle(Vehicle):

    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("This motorcycle is stopped")


#vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

#vehicle.go()
car.go()
motorcycle.go()

#vehicle.stop()
car.stop()
motorcycle.stop()
'''

'''
#python objects as arguments
class Car:

    color = None

class Motorcycle:

    color = None

def change_color(vehicle,color):

    vehicle.color = color


car_1 = Car()
car_2 = Car()
car_3 = Car()

bike_1 = Motorcycle()

change_color(car_1,"red")
change_color(car_2,"white")
change_color(car_3,"blue")
change_color(bike_1,"black")

print(car_1.color)
print(car_2.color)
print(car_3.color)
print(bike_1.color)


# duck typing = concept where the class of an object is less important than the methods/attributes
#               class type is not checked if minimum methods/attributes are present
#               “If it walks like a duck, and it quacks like a duck, then it must be a duck.”

class Duck:

    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("This duck is qwuacking")

class Chicken:

    def walk(self):
        print("This chicken is walking")

    def talk(self):
        print("This chicken is clucking")

class Person():

    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("You caught the critter!")


duck = Duck()
chicken = Chicken()
person = Person()

person.catch(chicken)
'''
'''
# walrus operator :=
# new to Python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression

# happy = True
# print(happy)

# print(happy := True)

# foods = list()
# while True:
#   food = input("What food do you like?: ")
#       if food == "quit":
#           break
#   foods.append(food)

foods = list()
while food := input("What food do you like?: ") != "quit":
    foods.append(food)
'''
'''
#assign function to variables

def hello():
    print("Hello")


hi = hello
hello()
hi()

# say = print
# say("Whoa! I can't believe this works! :O")
'''
'''
#  Higher Order Function =  a function that either:
#                           1. accepts a function as an argument
#                               or
#                           2. returns a function
#                           (In python, functions are also treated as objects)

# ----- 1. accepts a function as an argument -----
def loud(text):
   return text.upper()

def quiet(text):
   return text.lower()

def hello(func):
   text = func("Hello")
   print(text)


hello(loud)
hello(quiet)
# ------------ 2. returns a function -------------
#def divisor(x):
   #def dividend(y):
       #return y / x
   #return dividend


#divide = divisor(2)
#print(divide(10))
'''
'''
# lambda function = function written in 1 line using lambda keyword
#                   accepts any number of arguments, but only has one expression.
#                   (think of it as a shortcut)
#                   (useful if needed for a short period of time, throw-away)
#
# lambda parameters:expression

double = lambda x: x * 2
print(double(1))

multiply = lambda x, y: x * y
print(multiply(1,2))

add = lambda x, y, z: x + y + z
print(add(1,2,3))

full_name = lambda first_name, last_name: first_name+" "+last_name
print(full_name("Bro","Code"))

age_check = lambda age: True if age >= 18 else False
print(age_check(12))
'''
'''
# sort() method   = used with lists
# sort() function = used with iterables

students = (("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick","D", 36),
            ("Spongebob","B", 20),
            ("Mr.Krabs","C", 78))

grade = lambda grades:grades[1]
# students.sort(key=age)                                       # sorts current list
sorted_students = sorted(students,key=grade) # sorts and creates a new list

for i in sorted_students:
    print(i)
'''
#map() = applies function to each in an iterable(list, tuple, etc,)
# map(function,iterable)
'''
store = [("shirt",20.00),
         ("pants",25.00),
         ("jacket",50.00),
         ("socks",10.00)]

to_euros = lambda data: (data[0],data[1]*0.82)
# to_dollars = lambda data: (data[0],data[1]/0.82)

store_euros = list(map(to_euros, store))

for i in store_euros:
    print(i)
'''
'''
# filter() =    creates a collection of elements from an iterable,
#               for which a function returns true
#
#               filter(function, iterable)

friends = [("Rachel",19),
           ("Monica",18),
           ("Phoebe",17),
           ("Joey",16),
           ("Chandler",21),
           ("Ross",20)]

age = lambda data:data[1] >= 18

drinking_buddies = list(filter(age, friends))

for i in drinking_buddies:
    print(i)
'''
# reduce() = apply a function to an iterable and reduce it to a single cumulative value.
#            performs function on first two elements and repeats process until 1 value remains
#
# reduce(function, iterable)
'''
import functools

letters = ["H","E","L","L","O"]
word = functools.reduce(lambda x, y,:x + y,letters)
print(word)

factorial = [5,4,3,2,1]
result = functools.reduce(lambda x, y,:x * y,factorial)
print(result)
'''
'''
# list comprehension =  a way to create a new list with less syntax
#                       can mimic certain lambda functions, easier to read
#                       list = [expression for item in iterable]
#                       list = [expression for item in iterable if conditional]
#                       list = [expression if/else for item in iterable]
# --------------------------------------------------------------
squares = []                # create an empty list
for i in range(1,11):       # create a for loop
    squares.append(i * i)    # define what each loop iteration should do
print(squares)

# create a list AND defines what each loop iteration should do
squares = [i * i for i in range(1,11)]
print(squares)

# --------------------------------------------------------------
students = [100,90,80,70,60,50,40,30,0]

passed_students = list(filter(lambda x: x >= 60, students))
passed_students = [i for i in students if i >= 60]
# passed_students = [i if i >= 60 else "FAILED" for i in students]

print(passed_students)

# --------------------------------------------------------------
'''
'''
# dictionary comprehension = create dictionaries using an expression
#                            can replace for loops and certain lambda functions
#
# dictionary = {key: expression for (key,value) in iterable}
# dictionary = {key: expression for (key,value) in iterable if conditional}
# dictionary = {key: (if/else) for (key,value) in iterable}
# dictionary = {key: function(value) for (key,value) in iterable}
# -------------------------------------------------------------------------
cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
cities_in_C = {key: round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}
print(cities_in_C)

# -------------------------------------------------------------------------
# weather = {'New York': "snowing", 'Boston': "sunny", 'Los Angeles': "sunny", 'Chicago': "cloudy"}
# sunny_weather = {key: value for (key,value) in weather.items() if value == "sunny"}
# print(sunny_weather)

# -------------------------------------------------------------------------
# cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
# desc_cities = {key: ("WARM" if value >= 40 else "COLD") for (key,value) in cities.items()}
# print(desc_cities)

# -------------------------------------------------------------------------
# def check_temp(value):
    # if value >= 70:
        # return "HOT"
    # elif 69 >= value >= 40:
        # return "WARM"
    # else:
        # return "COLD"


# cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
# desc_cities = {key: check_temp(value) for (key,value) in cities.items()}
# print(desc_cities)

# -------------------------------------------------------------------------
'''

'''
# zip(*iterables) =  aggregate elements from two or more iterables (list, tuples, sets, etc.)
#                    creates a zip object with paired elements stored in tuples for each element

usernames = ["Dude", "Bro", "Mister"]
passwords = ("p@ssword", "abc123", "guest")
login_dates = ["1/1/2021","1/2/2021","1/3/2021"]

# --------------------------------------
users = list(zip(usernames,passwords))

for i in users:
    print(i)

# --------------------------------------
users = dict(zip(usernames,passwords))

for key,value in users.items():
    print(key+" : "+value)

# --------------------------------------
users = zip(usernames,passwords,login_dates)

for i in users:
    print(i)

# --------------------------------------
'''
'''
# ***********************************
# if _name_ == '__main__'
# ***********************************

# y tho?
# 1. Module can be run as a standalone program
#    or
# 2. Module can be imported and used by other modules

#  Python interpreter sets "special variables", one of which is _name_
#  Python will assign the _name_ variable a value of '__main__' if it's
#  the initial module being run

def main():
    print("Hello!")


if _name_ == '__main__':
    main()

# ***********************************
'''
'''
# ***************************************************************************
import time
# ***************************************************************************
print(time.ctime(0))    # convert a time expressed in seconds since epoch to a readable string
#                                        epoch = when your computer thinks time began (reference point)
print(time.time())      # return current seconds since epoch
print(time.ctime(time.time())) # will get current time

# ***************************************************************************
#time.strftime(format, time_object) = formats a time_object to a string
time_object = time.localtime() # local time
time_object = time.gmtime()  # UTC time
local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
print(local_time)

# ***************************************************************************
# time.strptime(string_string, format) = parses a string representing time/date and returns a struct_time object
# time_string = "20 April, 2020"
# time_object = time.strptime(time_string,"%d %B, %Y")
# print(time_object)

# ***************************************************************************
# time.asctime(time_tuple) = accepts a time_object or a tuple up to 9 elements and returns a string
# (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
# time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
# time_string = time.asctime(time_tuple)
# print(time_string)
# ***************************************************************************
# time.asctime(time_tuple) = accepts a time_object or a tuple up to 9 elements and return seconds since epoch
# (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
# time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
# time_string = time.mktime(time_tuple)
# print(time_string)

# ********************************************************************
'''
'''
# ****************************************************
# Python threading tutorial
# ****************************************************
# thread =  a flow of execution. Like a separate order of instructions.
#                  However each thread takes a turn running to achieve concurrency
#                  GIL = (global interpreter lock),
#                  allows only one thread to hold the control of the Python interpreter at any one time

# cpu bound = program/task spends most of it's time waiting for internal events (CPU intensive)
#             use multiprocessing

# io bound = program/task spends most of it's time waiting for external events (user input, web scraping)
#            use multithreading

import threading
import time


def eat_breakfast():
    time.sleep(3)
    print("You eat breakfast")


def drink_coffee():
    time.sleep(4)
    print("You drank coffee")


def study():
    time.sleep(5)
    print("You finish studying")


x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_coffee, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

x.join()
y.join()
z.join()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())

# ****************************************************
'''
'''
# **********************************************************
# Python daemon threads
# **********************************************************

# daemon thread = a thread that runs in the background, not important for program to run
#                 your program will not wait for daemon threads to complete before exiting
#                 non-daemon threads cannot normally be killed, stay alive until task is complete
#
#                 ex. background tasks, garbage collection, waiting for input, long running processes

import threading
import time


def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for: ", count, "seconds")


x = threading.Thread(target=timer, daemon=True)
x.start()

# x.setDaemon(True)
# print(x.isDaemon())
answer = input("Do you wish to exit?")

# **********************************************************
'''
'''
# *********************************
# Python multiprocessing
# *********************************
# multiprocessing = running tasks in parallel on different cpu cores, bypasses GIL used for threading
#                   multiprocessing = better for cpu bound tasks (heavy cpu usage)
#                   multithreading = better for io bound tasks (waiting around)

from multiprocessing import Process, cpu_count
import time


def counter(num):
    count = 0
    while count < num:
        count += 1


def main():

    print("cpu count:", cpu_count())

    a = Process(target=counter, args=(500000000,))
    b = Process(target=counter, args=(500000000,))

    a.start()
    b.start()

    print("processing...")

    a.join()
    b.join()

    print("Done!")
    print("finished in:", time.perf_counter(), "seconds")


if __name__ == '__main__':
    main()
'''
'''
# *********************************
from tkinter import *

window = Tk() #instantiate an instance of a window
window.geometry("420x420")
window.title("Bro Code first GUI program")

#icon = PhotoImage(file='logo.png')
#window.iconphoto(True,icon)
window.config(background="#5cfcff")

window.mainloop() #place window on computer screen, listen for events
'''
'''
# label = an area widget that holds text and/or an image within a window
from tkinter import *
window = Tk()

#photo = PhotoImage(file='person.png')

label = Label(window,
              text="bro, do you even code?",
              font=('Arial',40,'bold'),
              fg='#00FF00',
              bg='black',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              #image=photo,
              compound='bottom')
label.pack()
#label.place(x=0,y=0)

window.mainloop()
'''
'''
from tkinter import *

# button = you click it, then it does stuff

count = 0

def click():
    global count
    count+=1
    print(count)

window = Tk()

#photo = PhotoImage(file='like.png')

button = Button(window,
                text="click me!",
                command=click,
                font=("Comic Sans",30),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",
                state=ACTIVE,
                #image=photo,
                compound='bottom')
button.pack()

window.mainloop()
'''
