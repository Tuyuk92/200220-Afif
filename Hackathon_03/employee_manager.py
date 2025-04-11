from employee import Employee

class EmployeeManager(object):

    def __init__(self):
        self.employees = []

    #add employee
    def add_employee(self, employee):
        self.employees.append(employee)

    #view all employee
    def view_all_employees(self):
        return self.employees

    #search employee 
    def search_employee(self, employee_id):
        for employee in self.employees:
            if employee_id == employee_id:
                return employee
            return None

    #delete employee
    def delete_employee(self, employee_id):
        employee = self.search_employee(employee_id)
        if employee:
            self.employees.remove(employee)
            return True
        return False

    def load_employee(self, employee):
        self.employees = employee
        