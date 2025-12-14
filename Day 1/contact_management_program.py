phone_numbers = {"Dummy":"081234567890"}

def display():

    print("----- CONTACT LIST -----")
    for key, value in phone_numbers.items():
            print(f"{key}: {value}")
    print("------------------------")

def add(contact, number):
    pass

def edit(contact, number):
    pass

def delete(contact):
    pass


print("welcome to my contact management program!")
while True:
    action = input("select actions (display/add/edit/delete/exit): ").lower()

    if(action == "add"):
        name = input("enter new contact: ").capitalize()
        number = input("enter the phone number: ")
        phone_numbers.update({name:number})

    elif(action == "display"):
        display()
    elif(action == "edit"):
        display()
        targeted_key = input("which contact do you want to edit: ").capitalize()
        if targeted_key in phone_numbers:
            phone_numbers[targeted_key] = input(f"type in new value for contact {targeted_key}: ")
            
        else:
            print("that contact doesnt exist in the list!")
    elif(action == "delete"):
        display()
        targeted_key = input("which contact do you want to delete: ").capitalize()
        try:
            phone_numbers.pop(targeted_key)
        except:
            print("that contact doesnt exist in the list!")
    elif(action == "exit"):
        print("Thanks for using our program!")
        break
    else:
        print("invalid actions, try again!")