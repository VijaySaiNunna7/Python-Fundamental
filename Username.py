#   Username
#       Validation : Username must have @ Symbol
#   Password
#       Validation - Min Length should be 10 
# Login (Reponse)
#   200 - UserLogin is Succesful 
#   401 - Un Authorized
#   400 - Something Went Wrong
#   404 - Page Not Found
#   500 - Internal Server Error 

def login(username,password):
    if len(username) > 8 and len(password) > 10:
        if '@' in username and 'VJ' in password :
            if username == "Vijay Sai@" and password == "VJ9652394215":
                print("User Login success")
            else:
                print("Please enter the correct username or password")
        else:
            print("Mention the '@'in the username or 'VJ' in the password")
    else:
        print("Please enter the more than 8 characters in username or more than 10 characters in the password")

def validation(username,password):
    if username == "Vijay Sai@" and password == "VJvijaysai":
        return 200
    else:
          return 404
    
def purpose_user_input(usrname,password):
    response=validation(usrname,password)
    if response == 200:
        print("Login successfull")
    if response == 404:
            print("Something went worng")



def main():
    username = input("Enter the username : ")
    password = input("Enter the password : ")
    login(username,password)
    purpose_user_input(username,password)

if __name__ == "__main__":
    main()

            