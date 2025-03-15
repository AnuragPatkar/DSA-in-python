# Assignment-2: Classes and Objects

""" # 1. Define a python class Person with instance object variables name and age. Set Instance object variables in _init__() method. Also define show() method to display name and age of a person.
class Person:
    def __init__(self,name=None,age=None):
        self.name=name
        self.age=age
    def showPerson(self):
        print("Name:",self.name,"Age:",self.age)
p1=Person("Mahendra",25)
p1.showPerson() """
   
""" # 2. Define a class Circle with instance object variable radius. Provide setter and getter for radius. Also define getArea() and getCircumference() methods.
class Circle:
    def __init__(self,r=None):
        self.radius=r
    def setRadius(self,r):
        self.radius=r
    def getRadius(self):
        return self.radius
    def getArea(self):
        return 3.14*self.radius**2
    def getCircumference(self):
        return 2*3.14*self.radius
c1=Circle()
c2=Circle(7)
c1.setRadius(6)
print("c1: Radius-",c1.getRadius(),"Area-",c1.getArea(),"Circumference-",c1.getCircumference())
print("c2: Radius-",c2.getRadius(),"Area-",c2.getArea(),"Circumference-",c2.getCircumference()) """

""" # 3. Define a class Rectangle with length and breadth as instance object variables. Provide setDimensions(), showDimensions() and getArea() method in it.
class Ractangle:
    def __init__(self,length=None,breadth=None):
        self.length=length
        self.breadth=breadth
    def setDimension(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def showDimension(self):
        print("Lenght:",self.length,"Breadth:",self.breadth)
    def getArea(self):
        return self.length*self.breadth
r1=Ractangle()
r1.setDimension(5,6)
r1.showDimension()
print("Area:",r1.getArea()) """

""" # 4. Define a class Book with instance object variables bookid, title and price. Initialise them via init() method. Also define method to show book variables.
class Book:
    def __init__(self,bookid=None,title=None,price=None):
        self.bookid=bookid
        self.title=title
        self.price=price
    def showBook(self):
        print("Bookid:",self.bookid,"Title:",self.title,"Price:",self.price)
b1=Book(101,"The Lost Ship",250.0)
b1.showBook() """

""" # 5. Define a class Team with instance object variable a list of team member names. Provide methods to input member names and display member names.
class Team:
    def __init__(self):
        self.member=[]
    def addmembers(self,name):
        self.member.append(name)
    def displaymembers(self):
        print(self.member)
t1=Team()
t1.addmembers("Rohit")
t1.addmembers("Virat")
t1.addmembers("Dhoni")
t1.addmembers("Bhumrah")
t1.displaymembers()
 """