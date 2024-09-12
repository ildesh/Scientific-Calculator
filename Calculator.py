def Add(x, y):
    return x + y

def Subtract(x, y):
    return x - y

def Multiply(x, y):
    return x * y

def Divide(x, y):
    return x / y

def Elevate(x, y):
    return x ** y

print("\n Welcome! What operation do you want to do? ")
print("\n 1.Add \n 2.Subtract \n 3.Multiply \n 4.Divide \n 5.Elevate \n")

while True:
    choice = input("Select one of the numbers (1, 2, 3, 4, 5): ")

    if choice in ('1', '2', '3', '4', '5'):
        try:
            x = float(input("What is the first number? : "))
            y = float(input("What is the second number? : "))
        except ValueError:
            print("Invalid input. Please enter a number!")
            continue

        if choice == '1':
            print(f"The result is: {Add(x, y)}")

        elif choice == '2':
            print(f"The result is: {Subtract(x, y)}")

        elif choice == '3':
            print(f"The result is: {Multiply(x, y)}")

        elif choice == '4':
            if y != 0:
                print(f"The result is: {Divide(x, y)}")
            else:
                print("Cannot divide by zero!")
        
        elif choice == '5':
            print(f"The result is: {Elevate(x, y)}")

        # In questa parte controlliamo se l'utente vuole fare un altro calcolo
        while True:
            another = input("Want to do another operation? (Yes/No): ").lower()

            if another == 'no':
                print("Goodbye!")
                break

            elif another == 'yes':
                break
            else:
                print("Invalid input. Please enter 'Yes' or 'No'.")
        
        if another == 'no':
            break
    else:
        print("Invalid choice, please select a valid option!")
