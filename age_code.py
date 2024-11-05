class Age:
    #initilzing age through default constructor.
    def __init__(self,age):
        print("1.Assiging age to age varbile in intilization method")
        self.age=age

    #defining an method for checking whether is eligible or not.if above 18 eligible he is.
    def check_age(self):
        if self.age<18:
            print("2.1 Executing if block")
            print("Your Not eligible")

        #else book if above 18 this block will execute
        else:
            print("2.2 Executing else block")
            print("You are eligble")


#Taking age input from the user
age=int(input("Enter the age: "))
#creating an object for class
person_age=Age(age)


person_age.check_age()