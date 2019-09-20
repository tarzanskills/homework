class Customer:
    def __init__(self,cid,name,ticket):
        self.cid = cid
        self.name = name
        self.ticket = Ticket()


class Ticket:
    def __init__(self,time,movie,seat,screen):
        self.time = time
        self.movie = Movie()
        self.seat = Seat()
        self.sreen = Screen()


class Seat:
    def __init__(self,seat_number,screen):
        self.seat = seat_number
        self.screen = screen()


class Screen:
    def __init__(self,location,seat,movie):
        self.location = location
        seat = [Seat()]
        self.movie = Movie()


class Movie:
    def __init__(self,name,lang,price):
        self.name = name
        self.language = lang
        self.price = price


# c1 = Customer("101","Akash",Ticket())
# s1 = Seat("f-25")
#
# sc = Screen("B-wing")
#
# m = M("bahubali","Hindi","300")
