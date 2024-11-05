# Write a Program which will take the age input. if age > 18 Print Allowed to Vote else print "Please wait you need be atleast 18" 
class voter: # Class Name


    def __init__(self, age):  # Triggeed when Instance of Class is Created. Creating Object
        print (f"Inside Constructer {age}")
        self.voter_age = age


    def check_age(self):
        if self.voter_age >=18:
            print ("Voter is allowed to Vote")
        else:
            print ("You are not a Voter. You need to atleast 18 age")


    def check_age2(age):
        if age >=18:
            print ("Voter is allowed to Vote")
        else:
            print ("You are not a Voter. You need to atleast 18 age")
    


voter =voter(18)
voter.check_age()
voter.check_age2()