# Program Age Classifier
# Description: Determines the age and organizes it.
#   
#
# Author: <> 
# Date: <19/2/2025>
# Revised: 
#   <19/2/2025>


#Prints opening Statement



def Valid_option_menu():
    try_again = input("Would you like to enter another number? Y/N: ")

    if try_again.upper() == "Y":
                        
            persons_age()

    elif try_again.upper() == "N":
                        
            print("Exiting....created by Ricardo Montoya, Code updated 04/17/2025..................................................See Yah! Ignore the junk Code below if any.")

            SystemExit
            quit()
                
    else:

        print("Invalid option!")

        Valid_option_menu()

print("Organizes the age and places it in categories. By Ricardo Montoya-Adame")

# This Determines the age and organizes based on the age group
def persons_age():
    try:
        person = int(input("What is the age of the person?: "))
        if person <= 1:
            print("they are an infant")
            Valid_option_menu()
        elif person in range(2,14):
            print("they are a child")
            Valid_option_menu()
        elif person in range(14,20):
            print("they are a teenager")
            Valid_option_menu()
        elif person in range(20,61):
            print("They are an adult")
            Valid_option_menu()
        elif person in range(61,110):
            print("They are a senior")
            Valid_option_menu()
        elif person > 111:
            print("They're really old.")
            Valid_option_menu()
    except:
        print("error value entered was not a number.")
        persons_age()

# Runs the Program
persons_age()

#End of Program
