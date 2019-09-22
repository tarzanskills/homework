class Tarzan:
    def __init__(self, type, year_established,number_of_teachers, fees, number_of_students):
        self.type = type
        self.year_established = year_established
        self.number_of_teachers = number_of_teachers
        self.fees = fees
        self.number_of_students = number_of_students
    def get_type(self):
            return "Private"
    def placements(self):
        print("Places the students in companies")
    def teach(self):
        print("teaches the student")
    def cocurricular(self):
        print("gives opportunity to explore cocurricular activities")

tarzan= Tarzan(False, 1928, 4, 250000.00, 15)
print("The company has", tarzan.number_of_students)
print("The company has",tarzan.number_of_teachers)
print(tarzan.get_type())
