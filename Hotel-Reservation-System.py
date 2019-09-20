import sys

class Hotel:
    def __init__(self, listofrooms):

        self.availablerooms = listofrooms

    def displayAvailablerooms(self):
        print("The rooms we have in our hotel are as catagorized:")
        print("================================")
        for book in self.availablerooms:
            print(book)

    def Bookingroom(self, requestedRoom):
        if requestedRoom in self.availablerooms:
            print("The room you requested has now been booked for you.")
            self.availablerooms.remove(requestedRoom)
        else:
            print("Sorry the room you have requested is currently not available")

    def addRoom(self, addemptyroom):
        self.availablerooms.append(addemptyroom)
        print("Room you had booked is now cancelled.")


class Customer:
    def requestBooking(self):
        print("Enter the name of the room you'd like to book>>")
        self.book = input()
        return self.book

    def cancelBooking(self):
        print("Enter the name of the room you'd like to cancel>>")
        self.book = input()
        return self.book


def main():
    hotel = Hotel(["Single", "Double", "Premium","Super Premium"])
    customer = Customer()
    done = False
    while done == False:
        print(""" ====== HOTEL RESERVATION SYSTEM =======
                  1. Display all available rooms
                  2. Request a room booking
                  3. Cancel a booking
                  4. Exit
                  """)
        choice = int(input("Enter Choice:"))
        if choice == 1:
            hotel.displayAvailablerooms()
        elif choice == 2:
            hotel.Bookingroom(customer.requestBooking())
        elif choice == 3:
            hotel.addRoom(customer.cancelBooking())
        elif choice == 4:
            sys.exit()

main()