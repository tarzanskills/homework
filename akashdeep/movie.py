class Customer:
    def __init__(self,cid,name,Ticket):
        self.cid = cid
        self.name = name
        self.ticket = Ticket()


class Ticket:
    def __init__(self,time,Movie,Seat,Screen):
        self.time = time
        self.movie = Movie()
        self.seat = Seat()
        self.screen = Screen()


class Seat:
    def __init__(self,seat_number,Screen):
        self.seat = seat_number
        self.screen = Screen()


class Screen:
    def __init__(self,location,Seat,Movie):
        self.location = location
        seat = [Seat()]
        self.movie = Movie()

