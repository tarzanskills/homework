class Hotel:

    def __init__(self,name,address,check_in_date,check_out_date,room_no,service=0,price=0,laundry=0,game=0,r=0):
        self.r=r
        self.service=service
        self.laundry=laundry
        self.price=price
        self.game=game
        self.name=name
        self.address=address
        self.check_in_date=check_in_date
        self.check_out_date=check_out_date
        self.room_no=room_no


    def input_data(self):
        self.name=input("Enter your name:")
        self.address=input("Enter your address:")
        self.check_in_date=input("Enter your check in date:")
        self.check_out_date=input("Enter your checkout date:")
        print("Your room no.:",self.room_no,"\n")

    def roomrent(self):
        print ("We have the following rooms:-")
        print ("1.  type A---->rs 6000 PN\-")
        print ("2.  type B---->rs 5000 PN\-")
        print ("3.  type C---->rs 4000 PN\-")
        print ("4.  type D---->rs 3000 PN\-")
        x=int(input("Enter Your Choice Please->"))
        n=int(input("For How Many Nights Did You Stay:"))

        if (x == 1):
            print("you have opted room type A")
            self.price = 6000 * n
        elif (x == 2):
            print("you have opted room type B")
            self.price = 5000 * n
        elif (x == 3):
            print("you have opted room type C")
            self.price = 4000 * n
        elif (x == 4):
            print("you have opted room type D")
            self.price = 3000 * n
        else:
            print("please choose a room")
        print("your room rent is =", self.price, "\n")


    def restaurant_bill(self):
        print("*****RESTAURANT MENU*****")
        print("1.water----->Rs20","2.tea----->Rs10","3.breakfast combo--->Rs90","4.lunch---->Rs110","5.dinner--->Rs150","6.Exit")

        while (1):
            c=int(input("Enter your choice:"))
            if (c==1):
                d=int(input("Enter the quantity:"))
                self.service=self.service+20*d
            elif (c==2):
                 d=int(input("Enter the quantity:"))
                 self.service= self.service + 10 * d
            elif (c==3):
                 d=int(input("Enter the quantity:"))
                 self.service= self.service + 90 * d
            elif (c==4):
                 d=int(input("Enter the quantity:"))
                 self.service= self.service + 110 * d
            elif (c==5):
                 d=int(input("Enter the quantity:"))
                 self.service= self.service + 150 * d
            elif (c==6):
                break;
            else:
                print("Invalid option")
        print ("Total food Cost=Rs", self.service, "\n")

    def laundry_bill(self):
        print("******LAUNDRY MENU*******")
        print("1.Shorts----->Rs3", "2.Trousers----->Rs4", "3.Shirt--->Rs5", "4.Jeans---->Rs6", "5.Girlsuit--->Rs8",
              "6.Exit")

        while (1):
            e = int(input("Enter your choice:"))
            if (e == 1):
                f = int(input("Enter the quantity:"))
                self.laundry = self.laundry + 3 * f
            elif (e == 2):
                f = int(input("Enter the quantity:"))
                self.laundry = self.laundry + 4 * f
            elif (e == 3):
                f = int(input("Enter the quantity:"))
                self.laundry = self.laundry + 5 * f
            elif (e == 4):
                f = int(input("Enter the quantity:"))
                self.laundry = self.laundry + 6 * f
            elif (e == 5):
                f = int(input("Enter the quantity:"))
                self.laundry = self.laundry + 8 * f
            elif (e == 6):
                break;
            else:
                print("Invalid option")
        print("Total Laundry Cost=Rs", self.laundry, "\n")

    def game_bill(self):
        print ("******GAME MENU*******")
        print ("1.Table tennis----->Rs60","2.Bowling----->Rs80","3.Snooker--->Rs70","4.Video games---->Rs90","5.Pool--->Rs50==6","6.Exit")

        while (1):

            g=int(input("Enter your choice:"))

            if (g==1):
                h=int(input("No. of hours:"))
                self.game= self.game + 60 * h
            elif (g==2):
                h=int(input("No. of hours:"))
                self.game= self.game + 80 * h
            elif (g==3):
                h=int(input("No. of hours:"))
                self.game= self.game + 70 * h
            elif (g==4):
                h=int(input("No. of hours:"))
                self.game= self.game + 90 * h
            elif (g==5):
                h=int(input("No. of hours:"))
                self.game= self.game + 50 * h
            elif (g==6):
                break;
            else:
                print ("Invalid option")

        print ("Total Game Bill=Rs", self.game, "\n")

    def display(self):
        print ("******HOTEL BILL******")
        print ("Customer details:")
        print ("Customer name:",self.name)
        print ("Customer address:",self.address)
        print ("Check in date:",self.check_in_date)
        print ("Check out date",self.check_out_date)
        print ("Room no.",self.room_no)
        print ("Your Room rent is:",self.price)
        print ("Your Food bill is:",self.service)
        print ("Your laundary bill is:",self.laundry)
        print ("Your Game bill is:", self.game)

        self.bill= self.price + self.service + self.game + self.r

        print ("Your sub total bill is:", self.bill)
        print ("Additional Service Charges is",self.a)
        print ("Your grandtotal bill is:", self.bill + self.a, "\n")
        self.room_no+=1


def main():

    a=Hotel("Oyo","bengaluru","20/09/19","25/09/19",101)


    while (1):
        print("1.Enter Customer Data")

        print("2.Calculate rommrent")

        print("3.Calculate restaurant bill")

        print("4.Calculate laundry bill")

        print("5.Calculate gamebill")

        print("6.Show total cost")

        print("7.EXIT")

        b=int(input("\nEnter your choice:"))
        if (b==1):
            a.input_data()

        if (b==2):

            a.roomrent()

        if (b==3):

            a.restaurant_bill()

        if (b==4):

            a.laundry_bill()

        if (b==5):

            a.game_bill()

        if (b==6):

            a.display()

        if (b==7):

            quit()



main()