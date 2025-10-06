import json

FILE = "contact.json"

def load_contacts():
    try:
        with open(FILE) as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_contacts(contact):
    with open(FILE, "w") as file:
        json.dump(contact, file, indent=4)
        print("Contact Saved Successfully!")

def add_contacts(contact):
    name_str = input("Enter Name : ")
    name = name_str.lower()
    number = input("Enter Number : ")
    contact[name] = number
    print(f"The Contact For {name} Is Saved Successfully!")

def search_contacts(contact):
    name = input("Search The Contact Here! ")
    if name in contact:
        print(f"The Contact Number For {name} : {contact[name]}")
    else:
        print(f"No Contact Found!")

def main():
    contact = load_contacts()
    
    while True:
        print("\n--- Contact Manager Menu ---")
        print("1. Add a new contact")
        print("2. Search for an existing contact")
        print("3. Save and Quit")

        choice = int(input("Enter Your Choice : "))

        if choice == 1:
            add_contacts(contact)
        elif choice == 2:
            search_contacts(contact)
        elif choice == 3:
            save_contacts(contact)
            break
        else:
            print("Invalid Choice!")

if __name__ == "__main__":
    main()