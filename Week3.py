#comparison operators

i = 6
print(i<5)
print(i>=4)
print(i!=3)

#branching

'''age = int(input("Enter age: "))
if age >= 18:
    print("You can enter the concert")
elif age < 18:
    print("You can enter another concert")
else:
    print("move on")'''

# logic operators
'''age = int(input("Enter age: "))
if age == 19 or age == 20:
    print('You can come')
else:
    print('You can not come')'''

'''age = int(input("Enter age: "))
if age == 19 and age == 20:
    print('You can come')
else:
    print('You can not come')'''

#for loops
for i in range(0,13):
    print(i)

squares = ["blue", "green", 'red', 'yellow', 'orange']
for i, square in enumerate(squares):
    squares[i] = "white"
    #print(squares)
print(squares)

#while loops

squares = ["blue", "green", 'red', 'yellow', 'orange']
new_squares=[]
i = 0
while squares[i] == 'red':
    new_squares.append(squares[i])
    i = i+1
print(new_squares)

#functions

s = [2, 3, 5, 6, 1, 4, 9]
print(len(s))
print(sum(s))
# sorted method returns a new list whereas sort method sorts the existing list or tuple
new_s = sorted(s)
print(new_s)
print(s)
#print(s.sort())

def add(b):
    a = b + 1
    return a
a = add(5)
print(a)

def mul(a , b):
    return a * b
c = mul(2, 4)
print(c)

def no_work():
    pass
a = no_work()
print(a)

def printstuff(stuff):
    for i , s in enumerate(stuff):
        print("Album", i, "Ratings", s)

ratings = [10.0, 8, 9.7]
printstuff(ratings)

def names(*nam):
    for i in nam:
        print(nam)

names("Tooba", "Sheikh", "Yo")


def square(a):
    # Local variable b
    b = 1
    c = a * a + b
    print(a, "if you square + 1", c)
    return (c)
# Initializes Global variable

x = 3
# Makes function call and return function a y
y = square(x)
# Directly enter a number as parameter

square(2)
#objects and classes

#if x = 2 then it is an integer object or an instance of type integer

class circle(object):
    def __init__(self,radius, color):
        self.radius = radius
        self.color = color
        print(radius)
        print(color)

red_circle = circle(4, "red")

'''class circle(object):
    def __init__(self,radius, color):
        self.radius = radius
        self.color = color
    def add_radius(self, r):
        self.radius = self.radius + r
        return self.radius

c1 = circle(2, "red")
c1.radius(8)

#red_circle = circle(4, "red")'''

# Import the library

import matplotlib.pyplot as plt


class Circle(object):

    # Constructor
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color

        # Method

    def add_radius(self, r):
        self.radius = self.radius + r
        return (self.radius)

    # Method
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()

# Create an object RedCircle

RedCircle = Circle(10, 'red')
dir(RedCircle)
# Print the object attribute radius

print(RedCircle.radius)
# Print the object attribute color

print(RedCircle.color)
# Set the object attribute radius

RedCircle.radius = 1
print(RedCircle.radius)
# Call the method drawCircle

RedCircle.drawCircle()

#drawing a rectangele

# Create a new Rectangle class for creating a rectangle object

class Rectangle(object):

    # Constructor
    def __init__(self, width=2, height=3, color='r'):
        self.height = height
        self.width = width
        self.color = color

    # Method
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.height, fc=self.color))
        plt.axis('scaled')
        plt.show()

# Create a new object rectangle

SkinnyBlueRectangle = Rectangle(2, 10, 'blue')
# Print the object attribute height

print(SkinnyBlueRectangle.height)
# Print the object attribute width

print(SkinnyBlueRectangle.width)
# Print the object attribute color

print(SkinnyBlueRectangle.color)
# Use the drawRectangle method to draw the shape

SkinnyBlueRectangle.drawRectangle()

#creating second object for rectangle

# Create a new object rectangle
#first width then height

FatYellowRectangle = Rectangle(20, 5, 'yellow')
# Print the object attribute height

print(FatYellowRectangle.height)
# Print the object attribute width

print(FatYellowRectangle.width)
# Print the object attribute color

print(FatYellowRectangle.color)
# Use the drawRectangle method to draw the shape

FatYellowRectangle.drawRectangle()
