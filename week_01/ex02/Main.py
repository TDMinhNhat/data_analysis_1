import Employee as E
import numpy as np
import matplotlib.pyplot as plt

def display_choice():
    print("-----------------------------------------------------------------")
    print("1. Load list employess from a file .db")
    print("2. Add a new employee into a list")
    print("3. Display the list of employees")
    print("4. Display information from a employee by code")
    print("5. Update information from a employee")
    print("6. Remove a employee from list")
    print("7. Increase salary to a employee")
    print("8. Decrease salary to a employee")
    print("9. Display the number of employees from list")
    print("10. Sum of salary ")
    print("11. Calculate the avarage salary")
    print("12. Calculate the avarage age")
    print("13. List of oldest age employee")
    print("14. Sort increase employees by salary")
    print("15. Draw a correlation salary chart by age")
    print("16. Draw a comparison salary chart by group age: < 35, 35 - 50 and > 50")
    print("17. Draw the total salary percentage chart by group age")
    print("18. Draw the number of employees percentage chart by group age")
    print("19. Save list employees into dbemp_output.db")
    print("With other choice will exit the program")
    print("-----------------------------------------------------------------")

exit = False
list_employees = []

while(not exit):
    display_choice()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        try:
            with open("./week_01/ex02/dbemp_input.db", "rt") as file:
                list_lines = file.readlines()
                for i in list_lines:
                    if i == "\n" or i == "":
                        continue
                    employee = i.split(",")
                    emp = E.Employee(employee[0], employee[1], employee[2], employee[3])
                    list_employees.append(emp)
                print("Load employees successfully")
        except FileNotFoundError:
            print("Failed: File not found")
        except Exception:
            print("Failed: Something went wrong")
    elif choice == 2:
        code = input("Enter code: ")
        name = input("Enter name: ")
        age = input("Enter age: ")
        salary = input("Enter salary: ")
        emp = E.Employee(code, name, age, salary)
        list_employees.append(emp)
        print("Add employee successfully")
    elif choice == 3:
        for emp in list_employees:
            emp.display()
    elif choice == 4:
        code = input("Enter code: ")
        find = False
        for emp in list_employees:
            if emp.code == code:
                emp.display()
                find = True
        if not find:
            print("Employee not found")
    elif choice == 5:
        code = input("Enter code: ")
        find = False
        for emp in list_employees:
            if emp.code == code:
                name = input("Enter name: ")
                age = input("Enter age: ")
                salary = input("Enter salary: ")
                emp.name = name
                emp.age = age
                emp.salary = salary
                print("Update employee successfully")
                find = True
        if not find:
            print("Employee not found")
    elif choice == 6:
        code = input("Enter code: ")
        find = False
        for emp in list_employees:
            if emp.code == code:
                list_employees.remove(emp)
                print("Remove employee successfully")
                find = True
        if not find:
            print("Employee not found")
    elif choice == 7:
        code = input("Enter code: ")
        find = False
        for emp in list_employees:
            if emp.code == code:
                amount = float(input("Enter amount: "))
                emp.increase_salary(amount)
                print("Increase salary successfully")
                find = True
        if not find:
            print("Employee not found")
    elif choice == 8:
        code = input("Enter code: ")
        find = False
        for emp in list_employees:
            if emp.code == code:
                amount = float(input("Enter amount: "))
                emp.decrease_salary(amount)
                print("Decrease salary successfully")
                find = True
        if not find:
            print("Employee not found")
    elif choice == 9:
        print("Number of employees: ", len(list_employees))
    elif choice == 10:
        result = np.sum([float(emp.salary) for emp in list_employees])
        print("Sum of salary that company pay for each month: ", result)
    elif choice == 11:
        result = np.average([float(emp.salary) for emp in list_employees])
        print("Average salary: ", result)
    elif choice == 12:
        result = np.average([int(emp.age) for emp in list_employees])
        print("Average age: ", result)
    elif choice == 13:
        max_age = list_employees[0].age
        
        for emp in list_employees:
            if emp.age > max_age:
                max_age = emp.age
            
        for emp in list_employees:
            if emp.age == max_age:
                emp.display() 
    elif choice == 14:
        list_sorted = np.sort(list_employees, key=lambda x: x.age)
        list_sorted.forEach(lambda x: x.display())
    elif choice == 15:
        list_employees_age = [emp.age for emp in list_employees]
        list_employees_salary = [emp.salary for emp in list_employees]
        plt.scatter(x = list_employees_age, y = list_employees_salary)
        plt.xlabel("Age")
        plt.ylabel("Salary")
        plt.show()
    elif choice == 16:
        list_employee_age_smaller_35 = [emp for emp in list_employees if int(emp.age) < 35]
        list_employee_age_35_50 = [emp for emp in list_employees if 35 <= int(emp.age) <= 50]
        list_employee_age_bigger_50 = [emp for emp in list_employees if int(emp.age) > 50]
        
        average_salary_smaller_35 = np.average([float(emp.salary) for emp in list_employee_age_smaller_35])
        average_salary_35_50 = np.average([float(emp.salary) for emp in list_employee_age_35_50])
        average_salary_bigger_50 = np.average([float(emp.salary) for emp in list_employee_age_bigger_50])

        plt.bar(["< 35", "35 - 50", "> 50"], [average_salary_smaller_35, average_salary_35_50, average_salary_bigger_50])
        plt.xlabel("Age")
        plt.ylabel("Salary")
        plt.show()
        
        break
    elif choice == 17:
        sum_salary_smaller_35 = sum([float(emp.salary) for emp in list_employees if int(emp.age) < 35])
        sum_salary_35_50 = sum([float(emp.salary) for emp in list_employees if 35 <= int(emp.age) <= 50])
        sum_salary_bigger_50 = sum([float(emp.salary) for emp in list_employees if int(emp.age) > 50])
        
        plt.pie([sum_salary_smaller_35, sum_salary_35_50, sum_salary_bigger_50], labels=["< 35", "35 - 50", "> 50"], autopct='%1.1f%%')
        plt.title("Total salary percentage by group age")
        plt.show()
    elif choice == 18:
        list_employees_age_smaller_35 = np.array([emp for emp in list_employees if int(emp.age) < 35])
        list_employees_age_35_50 = np.array([emp for emp in list_employees if int(emp.age) >= 35 and int(emp.age) <= 50])
        list_employees_age_bigger_50 = np.array([emp for emp in list_employees if int(emp.age) > 50])

        plt.pie(
            [list_employees_age_smaller_35.__len__(), 
             list_employees_age_35_50.__len__(), 
             list_employees_age_bigger_50.__len__()], labels=["< 35", "35 - 50", "> 50"], autopct='%1.1f%%')
        plt.title("Number of employees percentage by group age")
        plt.show()
    elif choice == 19:
        try:
            with open("./week_01/ex02/dbemp_output.db", "wt") as file:
                for emp in list_employees:
                    file.write(emp.code + "," + emp.name + "," + emp.age + "," + emp.salary + "\n")
                
                print("Save employees successfully")
        except FileNotFoundError:
            print("Error: File not found")
        except Exception:
            print("Error: Something went wrong")
    else:
        exit = True
        print("Exit program")