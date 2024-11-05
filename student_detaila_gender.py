class Studentdetails:
    
    #constructor initialization
    def __init__(self,firstname,lastname,dob,age,gender=""):
        self.firstname=firstname
        self.lastname=lastname
        self.dob=dob
        self.age=age
        self.gender=gender
   
   # method 
    def full_name(self):
        fullname = self.firstname+self.lastname
        if self.gender.lower() =="male":
            return(f"Mr.{fullname}")
        elif self.gender.lower() =="female":
            return(f"Ms.{fullname}")
        else:
            return(f"{fullname}")
    def main():
        student1 = Studentdetails("Vijay","Sai",15-10-20003,20,"Male")
        student2 = Studentdetails("Shreenaval","Kishori",20-5-2003,20,"Female")
        student3 =Studentdetails("pavan","kumar",24-1-2002,20,)
        print(student1.full_name())
        print(student2.full_name())
        print(student3.full_name())
    



# firstname = input("Enter Your Firstname : ")
# lastname = input("Ente Your Lastname : ")
# dob = input("Enter Your Date-of-birth : ")
# age = int(input("Enter Your Age : "))
# gender = input("Enter Your Gender : ")
# student = Studentdetails(firstname,lastname,dob,age,gender)
# print(student.full_name()) 


if __name__ == "__main__":
    Studentdetails.main()
