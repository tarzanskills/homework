class Library:
    def __init__(self,name):
        self.name = name



class Librarian:
    count = 0
    def __init__(self,member,book,startdate,enddate,rent):
      self.member = member
      self.book = book
      self.startDate = startdate
      self.enddate = enddate
      self.rent = rent
      Librarian.count += 1

    def __str__(self):
        # return str(self.__dict__)
          return str(vars(self))










class Books:
    def __init__(self,name,author,publication,price,genre):
        self.name = name
        self.author = author
        self.publication = publication
        self.price = price
        self.genre = genre





class Members:
    def __init__(self,m_id,name,address,pay):
        self.m_id = m_id
        self.name = name
        self.address = address
        self.pay =pay




B1 = Books("physics","karan","p1","20","science")
#2= Books("chemistry,"p1","20","science")
B3 = Books("biology","karan","p1","20","science")

m1 = Members(101,"joshi","stag",2)

li = Librarian(m1,B1,"1-10-2019","10-10-2019",100)

print(li)