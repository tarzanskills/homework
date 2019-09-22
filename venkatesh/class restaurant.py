
class Restaurant:
    def __init__(self, type, year,price,cuisine,staff):
        self.type = type
        self.year = year
        self.price= price
        self.cuisine = cuisine
        self.number_of_staff =staff
    def get_type(self):
        if self.type == True:
            return "Veg"
        else:
            return "Non-veg"
    def prepare_food(self):
        print("Prepares the food")
    def take_order(self):
        print("Takes the order")
    def serve_food(self):
        print("Serves the food")

restaurant = Restaurant(True, 2012,1000, "South Indian", 50)
print("The cuisine is", restaurant.price)
print(restaurant.get_type())