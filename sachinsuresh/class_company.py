class Company:
    def __init__(self,name, number_of_employees, revenue, year_of_establishment, growth_percentage):
        self.name = name
        self.number_of_employees = number_of_employees
        self.revenue = revenue
        self.establish_year = year_of_establishment
        self.growth_percent = growth_percentage
    def hire(self):
        print("Hires new employee")
    def fire(self):
        print("Fires new employee")

itron = Company("Itron", 200, 4500000.00, 2012, 13.45)
print("grows at a percentage of", itron.growth_percent)
itron.hire()