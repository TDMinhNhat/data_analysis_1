import Rectangle as R
import os 

exit = False
list_rectangle = []

def display_choice():
    print("------------------------------------------")
    print("1. Read data from input.db")
    print("2. Add a new rectangle")
    print("3. Display the list of rectangles")
    print("4. Save list rectangles to output.db")
    print("With another choice will exit program")
    print("------------------------------------------")

def load_rectangle():
    try:
        with open("./week_01/ex01/input.db", "rt") as file:
            list_lines = file.readlines()
            component_rectangle = [line.strip().split("-") for line in list_lines]
            for i in component_rectangle:
                new_init = R.Rectangle(int(i[0]), int(i[1]))
                list_rectangle.append(new_init)

            print("Load data from input.db successfully")
    except FileNotFoundError:
        print("File not found")

def add_rectangle():
    print("Enter the length and width of the rectangle: ")
    length = int(input("Length: "))
    width = int(input("Width: "))
    new_init = R.Rectangle(length, width)
    list_rectangle.append(new_init)

def display_rectangle():
    for i in list_rectangle:
        i.display()

def save_rectangle():
    with open("./week_01/ex01/output.db", "wt") as file:
        for i in list_rectangle:
            file.write(i.__str__())

while(not exit):
    display_choice()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        load_rectangle()
    elif choice == 2:
        add_rectangle()
    elif choice == 3:
        display_rectangle()
    elif choice == 4:
        save_rectangle()
    else:
        exit = True
        print("Exit program")