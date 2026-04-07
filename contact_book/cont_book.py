file = "contacts.txt"

# Load contacts
contacts = {}
try:
    with open(file, "r") as f:
        for line in f:
            name, phone = line.strip().split(",")
            contacts[name] = phone
except:
    pass

while True:
    choice = input("\n1.Add  2.View  3.Search  4.Delete  5.Exit\nChoose: ")

    if choice == "1":
        name = input("Name: ")
        contacts[name] = input("Phone: ")

    elif choice == "2":
        for n, p in contacts.items():
            print(n, ":", p)

    elif choice == "3":
        name = input("Search: ")
        print(contacts.get(name, "Not found"))

    elif choice == "4":
        contacts.pop(input("Delete: "), None)

    elif choice == "5":
        break

    else:
        print("Invalid choice")

    # Save contacts
    with open(file, "w") as f:
        for n, p in contacts.items():
            f.write(f"{n},{p}\n")