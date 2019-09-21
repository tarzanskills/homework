class Company:
    def __init__(self, company_name, location,candidate_obj):
        self.company_name = company_name
        self.location = location
        self.candidate = candidate_obj


class Employee:
    def __init__(self, employee_name, employee_id, employee_designation):
        self.employee_name = employee_name
        self.employee_id = employee_id
        self.employee_designation = employee_designation
        self.employee_list = []


    def no_of_employee(self):
        employee_count = 0
        Employee.employee_count = Employee.employee_count + 1
        return employee_count


    def add_new_Employee(self,candidate):
        new_employee = self.employee_list.append(candidate)
        return new_employee


class Resources:
    def Hiring_Employee(self):
        details=self.eligibility
        return details


    def interview(self):
        return self.candidate


empolyee1 = Employee("Maddy",102024,"software testing")
company1 = Company("Capita India","kalyani nagr (Pune)",empolyee1)
print(company1.candidate.employee_name)

