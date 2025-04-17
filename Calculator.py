
# WOW Calc
# Calc is short for calculator
# Cant divide by decimals
# But it can divide by whole numbers
# Also also. Addition was not working fixed that too!



x = 1

y = 1

options = int()


# ------------------------------------------------------------------------------------------------------------


def Valid_option_menu():
    try_again = input("Would you like to try again? Y/N: ")

    if try_again.upper() == "Y":

        try_again = 1

        if try_again == 1:
                        
            main()

    elif try_again.upper() == "N":

        try_again = 2

        if try_again == 2:
                        
            print("Exiting....created by Ricardo Montoya 04/17/2025..................................................See Yah!")
                
    else:

        print("Invalid option!")

        Valid_option_menu()
# ------------------------------------------------------

def values_addition():
    try:
        x = round(int(input("Select your first number: ")))
        y = round(int(input("Select your second number: ")))
        z = round(x) + round(y)


        if z == z:
            print(f"{x} + {y} equals to = {z}")
            Valid_option_menu()


    except:
        print("Error invalid input.")
        values_addition()
# ----------------------------------------------------------------------------------------------

def values_subtraction():
    try:
        x = round(int(input("Select your first number: ")))
        y = round(int(input("Select your second number: ")))
        z = round(x) - round(y)



        if z == z:
            print(f"{x} - {y} equals to = {z}")
            Valid_option_menu()

        
        



    except:
        print("Error invalid input.")
        values_subtraction()
# ----------------------------------------------------------------------------------------------
def values_multiplication():
    try:
        x = round(int(input("Select your first number: ")))
        y = round(int(input("Select your second number: ")))
        z = round(x) * round(y)


        if z == z:
            print(f"{x} x {y} equals to = {z}")
            Valid_option_menu()


    except:
        print("Error invalid input.")
        values_multiplication()
# ----------------------------------------------------------------------------------------------
def values_division():
    try:
        x = round(int(input("Select your first number: ")))
        y = round(int(input("Select your second number: ")))
        z = round(x) / round(y)

        try:
            
            if z == z:
                print(f"{x} / {y} equals to = {z}")
                Valid_option_menu()


        except ZeroDivisionError:
            print("Can't Divide by zero")


    except:
        print("Error invalid input.")
        values_division()
# ----------------------------------------------------------------------------------------------

def main():
    print("Select your math Categories:")
    print(" 1. Addition")
    print(" 2. Subtraction")
    print(" 3. Multiplication")
    print(" 4. Division")

    try:
        options = int(input("Enter Option Number: "))

    except:
        print("Invalid Option.")
        print()
        print()
        main()


#-----------------------------------------------------------------------------------
    if options <= 0:
        print("Invalid Option")
        print()
        main()
    elif options >= 5:
        print("Invalid Option")
        print()
        main()
#-----------------------------------------------------------------------------------
    if options == 1:
        try:
            values_addition()
    
        except:
                print("invalid Number")
                values_addition()
                

    elif options == 2:
        try:
            values_subtraction()
    
        except:
            print("invalid Number")
            values_subtraction()
    elif options == 3:
        try:
            values_multiplication()
    
        except:
            print("invalid Number")
            values_multiplication()
    elif options == 4:
        try:
            values_division()
    
        except:
            print("invalid Number")
            values_division()


    

    





if __name__ == "__main__":
    main()
