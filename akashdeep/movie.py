class Movie:
    def __init__(self,name,language,price):
        self.name = name
        self.language = language
        self.price = price

    def __str__(self):
        return self.name


class Screen:
    def __init__(self,location,movie):
        self.location = location
        self.movie = movie

    def __str__(self):
        return self.movie


class Seat:
    def __init__(self,seat_number,screen):
        self.seat = seat_number
        self.screen = screen

    def __str__(self):
        return self.screen


class Ticket:
    def __init__(self,time,movie,seat,screen):
        self.time = time
        self.movie = movie
        self.seat = seat
        self.screen = screen

    def __str__(self):
        return self.seat


class Customer:
    def __init__(self,cid,name,ticket):
        self.cid = cid
        self.name = name
        self.ticket = ticket

    def __str__(self):
        return self.ticket


m = Movie("Bahubali","Hindi","500")
sc = Screen("B-wing",m)
s1 = Seat("B-25",sc)
t1 = Ticket("1:00",m,sc,s1)
c1 = Customer("101","akash",t1)

