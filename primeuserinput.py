
def user_validation(user_input):
    try:
        int(user_input)
        return True
    except ValueError:
        return False
    
def is_Prime(num):

    for x in range(2, num):
        if (num%x) == 0:
            return False
    return True

def prime_Function():

    numsinput = input(f"\nPlease enter a number between 1 & 100 \n")
    if user_validation(numsinput) is False:
        print(f"\ninvalid input, Please try again\n")
    elif user_validation(numsinput) is True:
        if is_Prime(int(numsinput)) is False:
            print("The number you entered is ", numsinput, "and it is not a prime number")
        else:
            print("The number you entered is ", numsinput, "and it IS a prime number!")


print("\nWelcome to the Prime Number tester\n")   
prime_Function()
while True:
    
    answer = input("\nDo you want to try again? Enter 'Y' to try again or press any key to exit\n").upper()
    if answer == "Y":
        prime_Function()
        continue

    else:
        print("Thank you for using the Prime Number tester")
        break








