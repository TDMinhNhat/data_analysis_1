import Employee as E

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
    print("15. Draw a correlation chart by age")
    print("16. Draw a comparison chart by  ")
    print("17. Draw the total salary percentage chart by group age")
    print("18. Draw the number of employees percentage chart by group age")
    print("19. Save list employees into dbemp_output.db")
    print("With other choice will exit the program")
    print("-----------------------------------------------------------------")

def load_employee():
    try:
        with open("./dbemp_input.db", "rt") as file:
            list_lines = file.readlines()
            for i in list_lines:
                print(i)
    except FileNotFoundError:
        print("File not found")

exit = False
while(not exit):
    display_choice()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        load_employee()
    elif choice == 2:
        break
    else:
        exit = True