class College:
    def __init__(self, type, year_established, branches_number, fees, number_of_students):
        self.type = type
        self.year_established = year_established
        self.branches_number = branches_number
        self.fees = fees
        self.number_of_students = number_of_students
    def get_type(self):
        if self.type == True:
            return "Public"
        else:
            return "Private"
    def placements(self):
        print("Places the students in companies")
    def teach(self):
        print("teaches the student")
    def cocurricular(self):
        print("gives opportunity to explore cocurricular activities")

bits = College(False, 1928, 9, 275000.00, 5050)
print("The college has", bits.number_of_students)
print(bits.get_type())