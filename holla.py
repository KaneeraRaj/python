phonebook={}

def add_contact():
    name=input("Enter name:").strip()
    number=input("Enter phone number:").strip()
    if name in phonebook:
        print("Contact already exists.")

    else:
        phonebook[name]=number
        print(f"contact'{name}'added.")
def searh_contact():
    name=input("Enter name to search").strip()

    if name in phonebook:
        print(f"contact'{name}:{phonebook[name]}")

    else:
        print("Contact not found")

def delete_contact():
    name=input("Enter name to delete").strip()
    
    if name in phonebook:
        del phonebook[name]
        print("contact'{name}'deleted")
    
    else:
        print("Contact not found")

def display_contacts():
    if not phonebook:
        print("Phonebook is empty")
    else:
        print("Contacts")
        for name,number in phonebook.items():
            print(f"{name}:{number}")

def main():
    while True:
     print("\n---Phonebook Menu--- ")
     print("1 Add contact")
     print("2 Search contact")
     print("3 Delete  contact")
     print("4 Display all  contact")
     print("5 Exit")

     choice=input("Choose an option(1-5):").strip()

     if choice=='1':
      add_contact()
     elif choice=='2':
         searh_contact()
     elif choice=='3':
         delete_contact()
     elif choice=='4': 
         display_contacts()
     elif choice=='5': 
         print("Exiting phonebook . Goodbye!")
     else:
         print("Invalid option.Please try again")
main()