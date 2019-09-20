class ticket:
    def __init__(self,screen,timing,movie_name,seat_number,price):
        self.screen=screen
        self.timing=timing
        self.movie_name=movie_name
        self.seat_number=seat_number
        self.price=price
class customer:
    def __init__(self,id,name,ticket):
        self.id=id
        self.name=name
        self.ticket=ticket
class seat:
    def __init__(self,seat_number,screen):
        self.seat_number=seat_number
        self.screen=screen
class screen:
    def __init__(self,location,movie_name):
        self.location=location
        self.movie=movie
class movie:
    def __init__(self,movie_name,language,rating):
        self.movie_name=movie_name
        self.language=language
        self.rating=rating
movie=movie("enter movie","english",45)
screen=screen("bellandur",movie)
seat=seat(12,"a12")
customer=customer(1,"abhishek",12)
ticket=ticket(screen,"7:30",movie_name,seat_number,200)

