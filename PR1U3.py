from datetime import datetime

class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = datetime.strptime(date_of_birth, '%Y-%m-%d')
    
    def calculate_age(self):
        current_date = datetime.now()
        age = current_date.year - self.date_of_birth.year
        
        if (current_date.month, current_date.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        
        return age
    
    def __str__(self):
        return f"Name: {self.name}, Country: {self.country}, Age: {self.calculate_age()}"


name = input("Enter your name: ")
country = input("Enter your country: ")
date_of_birth = input("Enter your date of birth (YYYY-MM-DD): ")

person = Person(name, country, date_of_birth)

print(person)
