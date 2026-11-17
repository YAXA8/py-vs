def add_contact():
    name = input("Contact's name: ").strip()
    phone = input("Phone number: ").strip()

    if not name or not phone:
        print("Name and phone number cannot be empty.")
        return

    if "|" in name or "|" in phone:
        print("Name and phone number cannot contain '|'.")
        return

    try:
        with open("contacts.txt", "a", encoding="utf-8") as file:
            file.write(f"{name}|{phone}\n")
    except OSError:
        print("Could not save the contact.")
        return

    print(f"Contact saved: {name}|{phone}")


def search_contact():
    search_name = input("Name to find: ").strip()

    if not search_name:
        print("Please enter a name.")
        return

    found = False

    try:
        with open("contacts.txt", "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split("|")

                if len(parts) != 2:
                    continue

                name, phone = parts
                name = name.strip()
                phone = phone.strip()

                if name and phone and name.lower() == search_name.lower():
                    print(f"{name}|{phone}")
                    found = True

    except FileNotFoundError:
        print("No contacts have been saved yet.")
        return
    except (OSError, UnicodeError):
        print("Could not read the contacts file.")
        return

    if not found:
        print("No contact found with this name.")


while True:
    print("\n1. Add contact")
    print("2. Search contact")
    print("3. Exit")

    choice = input("Your choice: ").strip()

    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        print("The program has ended.")
        break
    else:
        print("Invalid option. Please choose 1, 2, or 3.")