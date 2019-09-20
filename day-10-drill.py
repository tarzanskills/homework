class Mobile:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price

    def Show_information(self):
        print("Name of brand:  ", self.brand)
        print("Model: ", self.model)
        print("price :", self.price)
        print("------------------------")

    @classmethod
    def change_location(cls, location_name):
            cls.country = location_name

android = Mobile("Nokia","Nokia-510",2000)
ios = Mobile("apple","o-phone-6",10)
android.Show_information()
ios.Show_information()
android.change_location("south-zone")


class Motorbike:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def show_details(self):
        def Show_information(self):
            print("Name of brand:  ", self.brand)
            print("Model: ", self.model)
            print("Price :", self.price)
            print("------------------------")

        @classmethod
        def change_location(cls, location_name):
            cls.country = location_name

Bike = Mobile("Pulsar","185-cc",20)
scooty = Mobile("Roojdoot","dio",60000)
Bike.Show_information()
scooty.Show_information()
Bike.change_location("south-zone")

class Restaurant:
    def __init__(self,name,type,place):
        self.name=name
        self.type=type
        self.place=place
    def show_details(self):
        def Show_information(self):
            print("Name of agencies:  ", self.name)
            print("Address: ", self.place)
            print("Group :", self.type)
            print("------------------------")

        @classmethod
        def change_location(cls, location_name):
            cls.country = location_name

family_restaurent = Mobile("kfc","karnatka","only-veg")
bachlor_restaurent = Mobile("Davico","tehraan","veg or non-veg both")
family_restaurent.Show_information()
bachlor_restaurent.Show_information()
Bike.change_location("south-zone")

class library:
    def __init__(self,name,address,open_time,close_time):
        self.name=name
        self.address=address
        self.open_time=open_time
        self.close_time=close_time
    location="North-zone"
    def Show_information(self):
        print("Name of Librarian:  ",self.name)
        print("Address: ",self.address)
        print("Opening time :",self.open_time)
        print("Closing Time :",self.close_time)
        print("------------------------")

    @classmethod
    def change_location(cls, location_name):
        cls.country = location_name

central_library=library("veer kuwar singh","arah","10:30 Am","12:30 Am")
zonal_library=library("Dinkar","Patna","11:00 AM","12:00 AM")
central_library.Show_information()
zonal_library.Show_information()
central_library.change_location("south-zone")


class College:
    def __init__(self,name,grade,type):
        self.name=name
        self.grade=grade
        self.type=type


    location="North-zone"
    def Show_information(self):
        print("Name of college:  ",self.name)
        print("Naac grade: ",self.grade)
        print("Type of college : ",self.type)
        print("------------------------")

    @classmethod
    def change_location(cls, location_name):
        cls.country = location_name

indian=College("veer kuwar singh","C-","govt")
American=College("W.C University","A+","non-govt")
indian.Show_information()
American.Show_information()
indian.change_location("south-zone")

class Company:
    def __init__(self,name,revenue,strength_employee):
        self.name=name
        self.revenue=revenue
        self.strength_employee=strength_employee

    location="North-zone"
    def Show_information(self):
        print("Name of company:  ",self.name)
        print("revenue: ",self.revenue)
        print("Opening time :",self.strength_employee)
        print("------------------------")

    @classmethod
    def change_location(cls, location_name):
        cls.country = location_name

production_company=Company("IBM","3.6$",20000)
service_company=Company("Wipro","2.1$",3000)
production_company.Show_information()
service_company.Show_information()
production_company.change_location("south-zone")
