print("le dinh duy")
print("235752021610087")
import re
def check_password(password):
    if len(password) < 6 or len(password) > 12:
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[$#@]", password):
        return False
    return True
input_password = input("nhap mat khau phan tach nhau boi dau phay: ")
password = input_password.split(",")
valid_password = []

for password in password:
    if check_password(password.strip()):
        valid_passwords.append(password.strip())

print("mat khau hop le: ", ", ".join(valid_password))
      

    
    
