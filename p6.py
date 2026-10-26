contacts = {}

while True:
    print("\n--- Phonebook ---")
    print("1. Add contact")
    print("2. Search contact")
    print("3. Update contact")
    print("4. Delete contact")
    print("5. Display all contacts")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")

        contacts[name] = {
            "phone": phone,
            "email": email
        }
        print("Contact added.")

    elif choice == "2":
        name = input("Enter name to search: ")
        print(contacts.get(name, "Contact not found."))

    elif choice == "3":
        name = input("Enter name to update: ")

        if name in contacts:
            contacts[name]["phone"] = input("New phone: ")
            contacts[name]["email"] = input("New email: ")
            print("Contact updated.")
        else:
            print("Contact not found.")

    elif choice == "4":
        name = input("Enter name to delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")

    elif choice == "5":
        for name, details in contacts.items():
            print(name, details)

    elif choice == "6":
        break

    else:
        print("Invalid choice.")