import time
import os
#start of the program
password = ""
clear_command = 'cls' if os.name == 'nt' else 'clear'


## Setup PIN with. Only letters, min 8 characters
while True:
    print("Setting up your PIN...")
    password = input("Set your PIN (only letters, min 8 characters): ")
    
    # remove spaces
    password_no_spaces = password.replace(" ", "")
    
    if password == "":
        print("Error: PIN cannot be empty. Please try again.")
        time.sleep(1.5)
    elif password_no_spaces.isalpha() == False:
        print("Error: Numbers or symbols are not allowed! Use ONLY letters.")
        time.sleep(1.5)
    elif len(password) < 8:
        print("Error: PIN must be at least 8 letters long. Please try again.")
        time.sleep(1.5)
    else:
        # Both prompts stay visible on the screen together
        print("Confirm your PIN:")
        confirm_password = input("Set your PIN (only letters, min 8 characters): ")
        
        if confirm_password != password:
            print("Error: Please set a valid PIN and remember it.")
            time.sleep(1.5)
        else:
            # PIN is set correctly and confirmed, after this point, the program will exit and the user can log in with the PIN
            print("PIN saved successfully!\n")
            break  # Exiting
            time.sleep(1.5)
            os.system(clear_command)  # Clear the console screen for better user experience

# --- 2. WAIT-----
os.system(clear_command)  # Clear the console screen for better user experience
time.sleep(1.5)
print("Please wait...")
time.sleep(2)
print("Now you can try to log in.\n")
time.sleep(2.5)

os.system(clear_command)  # Clear the console screen for better user experience

# --- 3. LOGIN PROCESS with 3 max attempts ---
counter = 0
max_attempts = 3

print("You have 3 attempts to log in with your PIN.\n")
time.sleep(1.5)
while counter < max_attempts:
    user_password = input("Enter your PIN to log in: ")
    
    if user_password == password:
        os.system(clear_command)  # Clear the console screen for better user experience
        print("Welcome back! Login successful.")
        time.sleep(5)
        os.system(clear_command)  # Clear the console screen for better user experience
        exit()  # Ends the program after success if not, no login is recorded and the program will exit after 3 failed attempts
    else:
        counter = counter + 1
        remaining = max_attempts - counter
        print("Incorrect PIN. Attempts left: " + str(remaining))

print("Too many failed attempts. Exiting program...")
