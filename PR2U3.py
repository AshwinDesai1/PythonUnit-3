class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth

    def display(self):
        print(f"Name: {self.name}")
        print(f"Country: {self.country}")
        print(f"Date of Birth: {self.date_of_birth}")

class Employee(Person):
    def __init__(self, name, country, date_of_birth, employee_id, position):
        super().__init__(name, country, date_of_birth)
        self.employee_id = employee_id
        self.position = position

    def details(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Position: {self.position}")
    
    def display(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee Country: {self.country}")
        print(f"Employee Date of Birth: {self.date_of_birth}")
        super().display()
        print(f"Employee ID: {self.employee_id}")
        print(f"Position: {self.position}")

name = input("Enter your name: ")
country = input("Enter your country: ")
date_of_birth = input("Enter your date of birth (YYYY-MM-DD): ")

person1 = Person(name, country, date_of_birth)

print("\nPerson details:")
person1.display()

name = input("\nEnter employee name: ")
country = input("Enter employee country: ")
date_of_birth = input("Enter employee date of birth (YYYY-MM-DD): ")
employee_id = input("Enter employee ID: ")
position = input("Enter employee position: ")

employee1 = Employee(name, country, date_of_birth, employee_id, position)

print("\nEmployee details:")
employee1.display()
