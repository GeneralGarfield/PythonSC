# Wow another python script!
# This generates a random number with a given range.
# Im so proud of myself that i can code faster now.
# This script a long time ago would have taken me 2 days, but this only took me 10 minutes :D
# Enjoy




x = 1

y = 1

test = 1

user_input = int()


import random





def random_number_main():
    try:
        user_input = int(input("First number: "))

        user_input2 = int(input("Second Number: "))

        if user_input2 < user_input:
            print("Second Number must be greater than the first number")
            random_number_main()


        elif user_input == 0:
            print("The first number can't equal to 0, First value was converted into a 1")
            
            user_input = 1

            random_number = random.randint(user_input, user_input2)

            print(random_number)

            Valid_option_menu()

        elif user_input and user_input2:

            random_number = random.randint(user_input, user_input2)

            print(random_number)

            Valid_option_menu()

    except:
        print("Value is not a number.")
        random_number_main()


def Valid_option_menu():
    try_again = input("Would you like to try again? Y/N: ")

    if try_again.upper() == "Y":
                        
            main()

    elif try_again.upper() == "N":
                        
            print("Exiting....created by Ricardo Montoya 04/18/2025..................................................See Yah!")

            SystemExit
                
    else:

        print("Invalid option!")

        Valid_option_menu()





def main():

    print("Welcome! Type the numbers range in which you want your number to be in!")

    random_number_main()



if __name__ == "__main__":
    main()
