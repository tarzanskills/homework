#----restaurant----
class Restaurant:
    def __init__(self,place,restaurant_name,cuisine_type):
        self.place
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type

    def restaurant_description(self):
        print(self.restaurant_name,"serves",self.cuisine_type,"at",self.place)

Empire=Restaurant("Bangalore","Empire","Thai")
Empire.restaurant_description()




#-----Motorbike-----

class Motorbike:
    def __init__(self,company,color):
        self.company=company
        self.color=color

    def display(self):
        print("This is a ",self.color,self.company)

object=Motorbike("Roper","Red")
object.display()


#------MOBILE------

class Mobile:
    def __init__(self,brand,price,color):
        self.brand=brand
        self.price=price
        self.color=color

    def show(self):
        print("this is ",self.brand,"for",self.price,"in",self.color)

object=Mobile("Iphone",300000,"Rosegold")
object.show()


#-----Library-----

class Library:
    def __init__(self,name,id,phone,address):
        self.name=name
        self.id=id
        self.phone=phone
        self.address=address

    def details(self):
        print("The details of a stakeholder are",self.name,self.id,self.phone,self.address)

Stakeholder=Library("Saniya",101,9972579626,"Tumkur")
Stakeholder.details()


#----College----

class College:
    def __init__(self,name,courses):
        self.name=name
        self.courses=courses

    def show(self):
        print(self.name,"college offers",self.courses)

object=College("St.Mary's","Science,Arts,Commerce")
object.show()


#----company----

class Company:
    def __init__(self,name,type,place):
        self.name=name
        self.type=type
        self.place=place

    def details(self):
        print(self.name,"company is",self.type,"located at",self.place)

object=Company("Microsoft","product-based","USA")
object.details()