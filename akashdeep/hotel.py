class Hotel:
    def __init__(self,name,nor):
        self.Name = name
        self.guest_list = []
        self.Number_of_rooms = nor

    def add_guest(self,Guest):
        if  self.Number_of_rooms != 0:
            self.guest_list.append(Guest)
            print("Rooms assing to:"+ G.name)
            self.Number_of_rooms -= 1
        else:
            print("No Rooms Available")

class Guest:
    def __init__(self,gname,uid,check_in,check_out):
        self.name = gname
        self.uid = uid
        self.check_in = check_in
        self.check_out = check_out


H = Hotel("jw mariott",1)
G = Guest("Akash",101,"10-12-2019","12-12-2019")
H.add_guest(G)
print(H.guest_list[0].__dict__)


G1 = Guest("Reet",201,"10-2-2014","15-2-2014")
H.add_guest(G1)

H1 = Hotel("OYO",2)
