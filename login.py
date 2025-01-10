#Michelle Xilotl
# 12-4-24
#Login

def login():
    #Hardcoded valid username and password (modify these)
    valid_username = "YourUsername" #case in-sensitive
    valid_password = "YourPassword" #case sensitive

    #get user input for username and password (Ask user to enter both)
    v_user = input("Please enter your username: ")
    v_pass = input("Please enter your password: ")

    #convert the entered username to lowercase or uppercase by using
    v_user = v_user.lower()
    valid_username = valid_username.lower()

    #check if the entered username and password match the valid
    if v_user == valid_username and v_pass == valid_password:
        print("yay")
    if v_user != valid_username or v_pass != valid_password:
        print("invalid credentials")

#call the function to check credentials
login()
