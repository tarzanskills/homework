class Customer:
    def __init__(self, id, name, ticket):
        self.id = id
        self.name = name
        self.ticket = ticket

class Ticket:
    def __init__(self,time, movie, seat, price):
        self.time = time
        self.movie = movie
        self.seat = seat
        self.price = price

class Seat:
    def __init__(self, seat_num, screen):
        self.seat_num = seat_num
        self.screen = screen

class Screen:
    def __init__(self, location, screen_name, movie):
        self.screen_name = screen_name
        self.location = location
        self.movie = movie

class Movie:
    def __init__(self, name, language):
        self.name = name
        self.language = language

AIRising = Movie('Ai Rising', 'english')
pvr = Screen('bengaluru', 'screen-A', AIRising)
a1 = Seat('A1', pvr)
ticket_1 = Ticket('12.30 pm', AIRising, a1, 200)
customer_1 = Customer('#01',"Pankaj Rathore",ticket_1)