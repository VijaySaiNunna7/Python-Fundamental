#Printing factorial of an numbers by entering the range.
# (start,end_value) user will enter the start value and end value.
# we need to print that each value of the factorial from start to end.

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)


def print_values(o,p):
    for i in range(o,p+1):
        print (f"Factorial of {i} is {factorial (i)}")


def main():
    o=int(input("Enter the Start Factorial : "))
    p=int(input("Enter the end Factorial : "))
    if 0<0 or p<0:
        print("Enter the valid numbers negative numbers is not valid")
    elif o==0 or p==0:
        print("Entered 0 value is 1")
    elif o==1 or p==1:
        print("Entered 1 value is also 1")
    else:
        print_values(o,p)
if __name__=="__main__":
    main()


# import math
# start_value=int(input("Enter the Start Factorial : "))
# end_value=int(input("Enter the end Factorial : "))
# def fact():
#     for i in range (start_value,end_value+1):
#         print(f"factorial{i} ",math.factorial(i))
# def main():
#     fact()
# if __name__=="__main__":
#     main()


