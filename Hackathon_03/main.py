from employee import Employee
from employee_manager import EmployeeManager
from storage import Storage

def main():

    manager = EmployeeManager()
    store = Storage()

    saved_employees = store.load()
    manager.load_employee(saved_employees)

    while True:
        print("\n-----------------------------------------")
        print("-        Employee Management CLI        -")
        print("-  1. Add Employee                      -")
        print("-  2. View All Employee                 -")
        print("-  3. Search Employee by ID             -")
        print("-  4. Delete Employee                   -")
        print("-  5. Save and Exit                     -")
        print("-----------------------------------------")

        choice = input("Enter Your Choice --> ")

        if choice == '1':
            name = input("Enter Name: ")
            department = input("Enter Department: ")
            designation = input("Enter Designation: ")
            gross = float(input("Enter Gross Salary: "))
            tax = float(input("Enter Tax: "))
            bonus = float(input("Enter Bonus: "))
            employee = Employee(name, department, designation, gross, tax, bonus)
            manager.add_employee(employee)
            store.save(manager.view_all_employees())
            print("Employee added Successfully")

        elif choice == '2':
            for employee in manager.view_all_employees():
                print(employee.to_dict())

        elif choice == '3':
            employee_id = input("Enter Employee ID: ")
            employee = manager.search_employee(employee_id)
            print(employee.to_dict()if employee else "Employee not FOund. ")

        elif choice == '4':
            employee_id = input("Enter Employee ID to Delete: ")
            if manager.delete_employee(employee_id):
                print("Employee deleted.")
            else:
                print("Employee not found. ")

        elif choice == '5':
            store.save(manager.view_all_employees())
            print("Data saved. Exiting Now. Bye...")
            break

        else:
            print("Invalid Choice. Please Try Again")

if __name__ == "__main__":
    main()