##########################################test#########################################################
#########
##function 1

def shut_down(s):
    if s == "yes":
        return "Shutting down"
    elif s == "no":
        return "Shutdown aborted"
    else:
        return "Sorry"

#s = ""
#print(shut_down(s))

#########
##function 2

import math
x = math.sqrt(13689)
print(x)

##################
## function 3

def distance_from_zero (input):
        if (type(input)== int or type(input) == float):
            if(input<0):
                return -1*input
            elif(input>=0):
                return input
        else:
            return "nope"


print(distance_from_zero(input = -1))
##also the fabs function from math can be used for this for the if statement that checks the type of the input
#########################
##function 4 INSTRUCTIONS ARE UNCLEAR##########################################################################
def computepay(hours, rate):
    if hours <= 40:
        return hours * rate
    else:
        return 40*rate + (hours-40)*rate*1.5

print(computepay(41,10))

########################
##function 5
hcpn = 140#hotelcostpernight
cc = 40 #car cost
def hotel_cost(nights):
    return nights*hcpn

def plane_ride_cost(city):
    if(city == "Charlotte"):
        return 183
    elif(city == "Tampa"):
        return 220
    elif(city == "Pittsburgh"):
        return 222
    elif(city =="Los Angeles"):
        return 475
    else:
        return

def rent_car_cost(days):
    if days>=7:
        return days*cc - 50
    elif 7>days and days>=3:
        return days*cc - 20
    else:
        return days*cc

def trip_cost(city, days, spending_money):
    nights = days - 1 #for hotel cost purpose, nothing else was given for the nights variable
    return hotel_cost(nights) + plane_ride_cost(city) + rent_car_cost(days) + spending_money

#print(trip_cost("Pittsburgh", 23, 2300))

##################
##function 6

def cube(number):
    return number*number*number

def by_three(number):
    if number%3 == 0:
        return cube(number)
    else:
        return False

#print(by_three(11))

################################################Homework 2#########################################



class Triangle():
    number_of_sides = 3
    def __init__ (self, angle1, angle2, angle3):
          self.angle1 = angle1
          self.angle2 = angle2
          self.angle3 = angle3

    def checkangles(self):
        if self.angle1 + self.angle2 + self.angle3 == 180:
            return True
        else:
            return False


mytriangle = Triangle(angle1= 90, angle2=30, angle3= 60)
#print(mytriangle.checkangles())
#print(mytriangle.number_of_sides)
#####################
####Excersise2####
class Song():
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        result = ''
        for element in self.lyrics:
            result += str(element)
            result += "\n"
        return result

happy_bday = Song(lyrics = ["May god bless you, ", "Have a sunshine on you,", "Happy Birthday to you !"])
print(happy_bday.sing_me_a_song())
####################
#####Excercise3
class Lunch():
    def __init__(self, menu):
        self.menu = menu
    def menu_price(self):
        if self.menu == "menu 1":
            return print("Your choice: " +self.menu + " Price 12.00")
        elif self.menu == "menu 2":
            return print("Your choice: " +self.menu + " Price 13.40")
        else:
            return print("Error in menu.")

Paul = Lunch("menu 1")
Paul.menu_price()

###############
###Excercise4
class Point3D(): #class Point3D(Point3D):

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
        return "(%d, %d, %d)" % (self.x, self.y, self.z)

my_point = Point3D(x=1, y=2, z=3)
print(my_point)
####githuba gidiyor mu test 13.04.2020 12.00
###bir şeyler ekliyorum ama pushlanmıyor