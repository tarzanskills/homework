class Restaurant:
    def __init__(self, type, year_established, cuisine, price_per_2, number_of_staff):
        self.type = type
        self.year_established = year_established
        self.cuisine = cuisine
        self.price_per_2 = price_per_2
        self.number_of_staff = number_of_staff
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

meridian = Restaurant(True, 1902, "South Indian", 400.00, 50)
print("The cuisine is", meridian.price_per_2)
print(meridian.get_type())