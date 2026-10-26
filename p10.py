store1 = {
    "Laptop": 10,
    "Mouse": 25,
    "Keyboard": 15
}

store2 = {
    "Laptop": 5,
    "Mouse": 10,
    "Monitor": 8
}

inventory = {
    item: store1.get(item, 0) + store2.get(item, 0)
    for item in store1.keys() | store2.keys()
}

while True:
    print("\n--- Inventory Tracker ---")
    print("1. Display inventory")
    print("2. Search item")
    print("3. Add stock")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        for item, quantity in inventory.items():
            print(item, ":", quantity)

    elif choice == "2":
        item = input("Enter item name: ")
        print("Quantity:", inventory.get(item, 0))

    elif choice == "3":
        item = input("Enter item name: ")
        try:
            quantity = int(input("Enter quantity to add: "))

            if quantity < 0:
                print("Quantity cannot be negative.")
            else:
                inventory[item] = inventory.get(item, 0) + quantity
                print("Stock updated.")
        except ValueError:
            print("Enter a valid integer.")

    elif choice == "4":
        break

    else:
        print("Invalid choice.")