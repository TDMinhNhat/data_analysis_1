import Rectangle as R

def display_menu():
    print("-------------------------------")
    print("1. Create a new Rectangle")
    print("2. Display all Rectangles")
    print("3. Sum of all Rectangles' areas")
    print("4. Display the rectangle with the smallest perimeter")
    print("5. Exit")
    print("-------------------------------")

choice = True
list_rectangles = []

while(choice):
    display_menu()
    input_choice = int(input("Enter your choice: "))
    
    if(input_choice == 1):
        width = int(input("Input your width: "))
        height = int(input("Input your height: "))
        rect = R.Rectangle(width, height)
        list_rectangles.append(rect)

        if(width < 0 or height < 0):
            print("The width and height rectangle should be positive number")
            print("Add a new rectangle failed")

        print("Add rectangle successfully!")
    elif (input_choice == 2):
        for i in list_rectangles:
            i.display()

    elif (input_choice == 3):
        sum_area = 0
        for i in list_rectangles:
            sum_area += i.calcArea()
        print(f"Sum of all rectangles' areas: {sum_area}")

    elif (input_choice == 4):
        min_perimeter = list_rectangles[0].calcPerimeter()
        index = 0
        for i in range(1, len(list_rectangles)):
            if(list_rectangles[i].calcPerimeter() < min_perimeter):
                min_perimeter = list_rectangles[i].calcPerimeter()
                index = i
        print("The rectangle with the smallest perimeter:")
        list_rectangles[index].display()
        
    elif (input_choice == 5):
        choice = False
        print("Stop program.")
    else:
        print("Invalid choice. Please try again.")
