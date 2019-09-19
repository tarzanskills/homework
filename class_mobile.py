class Mobile:
    def __init__(self,company, model, display_size, price, processor):
        self.company = company
        self.model = model
        self.display_size = display_size
        self.price = price
        self.processor = processor
    def call_user(self):
        print("Calls a user")
    def play_pubg(self):
        print("Plays PUBG")
    def watch_movie(self):
        print("Watch movie")

phone = Mobile("OnePlus", '7Pro', 6, 51999.00, 'SnapDragon855')
print("The processor is" , phone.processor)
phone.play_pubg()