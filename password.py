import time
password = ""  
## Setup PIN with. Only letters, min 8 characters
while True:
    password = input("Set your PIN (only letters, min 8 characters): ")
    
    # remove spaces
    password_no_spaces = password.replace(" ", "")
    
    if password == "":
        print("Error: PIN cannot be empty. Please try again.")
    elif password_no_spaces.isalpha() == False:
        print("Error: Numbers or symbols are not allowed! Use ONLY letters.")
    elif len(password) < 8:
        print("Error: PIN must be at least 8 letters long. Please try again.")
    else:
        confirm_password = input("Set your PIN (only letters, min 8 characters): ")
        if confirm_password != password:
            print("Error: Please set a valid PIN and remember it.")
        else:
            # PIN is set correctly and confirmed, after this point, the program will exit and the user can log in with the PIN
            print("PIN saved successfully!\n")
            break  # Exiting

# --- 2. WAIT-----
print("Please wait...")
time.sleep(2)
print("Now you can try to log in.\n")

# --- 3. LOGIN PROCESS with 3 max attempts ---
counter = 0
max_attempts = 3

while counter < max_attempts:
    user_password = input("Enter your PIN to log in: ")
    
    if user_password == password:
        print("Welcome back! Login successful.")
        exit()  # Ends the program after success if not, no login is recorded and the program will exit after 3 failed attempts
    else:
        counter = counter + 1
        remaining = max_attempts - counter
        print("Incorrect PIN. Attempts left: " + str(remaining))

print("Too many failed attempts. Exiting program...")
