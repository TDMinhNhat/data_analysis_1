class Employee:

    def __init__(self, code, name, age, salary):
        self.code = code
        self.name = name
        self.age = age
        self.salary = salary
    
    def income(self):
        return 0.9 * 12 * self.salary

    def display(self):
        print(f"Code: {self.code}, Name: {self.name}, Age: {self.age}, Salary: {self.salary}")

    def increase_salary(self, amount):
        self.salary += amount

    def decrease_salary(self, amount):
        value_20_percent = self.salary * 0.2
        if(amount > value_20_percent):
            print("Error: The amount is greater than 20% of the salary")
        else:
            self.salary -= amount

    def display(self):
        print(f"Code: {self.code}, Name: {self.name}, Age: {self.age}, Salary: {self.salary}")