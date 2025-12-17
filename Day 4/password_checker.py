password = str(input("enter password to be checked: "))

# CRITERIA
# must be at least 12 characters
# must include at least one of these !@#$%^&*
# must have an uppercase and lowercase letter
# must have numbers

numbers = (1,2,3,4,5,6,7,8,9,0)
symbols = ("!","@","#","$","%","^","&","*","(",")","_","+")

is_password_long_enough = False
is_there_number = False
is_there_symbol = False
is_there_upperlower = False

# check if there is number inside the password string
for number in numbers:
    if not password.find(str(number)) == -1:
        is_there_number = True

# check if there is symbol inside the string
for symbol in symbols:
    if not password.find(str(symbol)) == -1:
        is_there_symbol = True

# check password length
if len(password) < 12:
    is_password_long_enough = False
else:
    is_password_long_enough = True

# check if it has uppercase and lowercase
if not password.islower() and not password.isupper():
    is_there_upperlower = True

print("---RESULT---")
print(f"more than 12 characters: {is_password_long_enough}")
print(f"includes number: {is_there_number}")
print(f"includes symbol: {is_there_symbol}")
print(f"contains combination of lowercase and uppercase: {is_there_upperlower}")
print("------------")
