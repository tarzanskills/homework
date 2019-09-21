class Hotel:
    def __init__(self,hotel_name, location,staff_obj):
        self.hotel_name = hotel_name
        self.location = location
        self.staff_obj = staff_obj

class Staff:
    def __init__(self, staff_name, staff_id, qualificetion, gender, destination,customer_obj):
        self.staff_name = staff_name
        self.id = staff_id
        self.qualification = qualificetion
        self.gender = gender
        self.destination = destination
        self.customer = customer_obj

class Restaurant:
    def __init__(self, restaurant_name, special_food):
        self.restaurant_name = restaurant_name
        self.special_food = special_food


class Room:
    def __init__(self, no_of_bed, room_no):

        self.room_no = room_no
        self.no_of_bed = no_of_bed

class Customer:
    def __init__(self, customer_id, customer_name,room_no_obj,restaurant_obj):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.room_no_obj = room_no_obj
        self.restaurant_obj=restaurant_obj


room01 = Room(100,2)
resturant = Restaurant("KFC", "Pizza")
varun = Customer(1,"varun",room01,resturant)



staff1=Staff("Manya",1,"MBA","Male","Manager",varun)

print(varun.room_no_obj.room_no)
print(varun.restaurant_obj.restaurant_name)
print(staff1.customer.customer_name)