import uuid

class Employee:
    def __init__(self, name, department, designation, gross_salary, tax, bonus):
        self.id = str(uuid.uuid4())
        self.name = name
        self.department = department
        self.designation = designation
        self.gross_salary = gross_salary
        self.tax = tax
        self.bonus = bonus
        self.net_salary = self.calculate_net_salary()

    def calculate_net_salary(self):
        return self.gross_salary - self.tax + self.bonus
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "department": self.department,
            "designation": self.designation,
            "gross_salary": self.gross_salary,
            "tax": self.tax,
            "bonus": self.bonus,
            "net_salary": self.net_salary
        }

    @staticmethod   
    def from_dict(data):
        return Employee(
            name=data["name"],
            department=data["department"],
            designation=data["designation"],
            gross_salary=data["gross_salary"],
            tax=data["tax"],
            bonus=data["bonus"],
            emp_id=data["id"]
        )
    