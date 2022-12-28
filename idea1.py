# Write a python code where it loops using the Collatz Conjecture (3n + 1) utilizing user input

def isInteger(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

def collatz_Sequence(num):
    num_seq = [num]
    if num < 1:
        return []
    while num > 1:
        if num % 2 == 0:
            num = num / 2
        else:
            num = 3 * num + 1
        num_seq.append(num)
    return num_seq

def main_function():

    while True:
        num1 = int((input("\nPlease enter a number between 1 & 100\n")))
        if isInteger(num1) is False:
            print(f"\n{num1} is not a valid input, please try again\n")
            continue
        print(collatz_Sequence(num1))
        answer = input("do you wish to continue? Y/N").upper()
        if answer == "Y":
            continue
        else:
            break

print("\nThe Collatz Conjecture generator A.K.A 3n + 1\n")
main_function()



    
    

        