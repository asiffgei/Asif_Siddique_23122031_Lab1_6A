
print("================================")
print("     PAK TRAVEL AGENCY")
print("================================")

print("\n--- Registration ---")

name = input("Enter your name: ")
phone = input("Enter your phone number: ")

print("\nRegistration Complete!")
print("Welcome", name)

while True:

    print("\n--- Main Menu ---")
    print("1. Book a Trip")
    print("2. Contact Us")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        print("\n--- Select City ---")
        print("1. Lahore")
        print("2. Islamabad")
        print("3. Hunza")

        city = input("Select city: ")

        if city == "1":
            print("\nLahore Trip Selected!")
            print("Package: Rs. 10,000")

        elif city == "2":
            print("\nIslamabad Trip Selected!")
            print("Package: Rs. 12,000")

        elif city == "3":
            print("\nHunza Trip Selected!")
            print("Package: Rs. 25,000")

        else:
            print("Invalid selection.")

        print("\n1. Next")
        print("2. Back")

        option = input("Enter choice: ")

        if option == "1":
            print("\nYour booking request has been received.")
            print("We will contact you at", phone)

        elif option == "2":
            print("\nReturning to main menu...")

        else:
            print("Invalid choice.")

    elif choice == "2":

        print("\n--- Contact Us ---")
        print("Phone: 0300-1234567")
        print("Email: paktravel@gmail.com")

        print("\n1. Next")
        print("2. Back")

        option = input("Enter choice: ")

        if option == "1":
            print("Thank you for contacting Pak Travel Agency!")

        elif option == "2":
            print("Returning to main menu...")

        else:
            print("Invalid choice.")

    elif choice == "3":

        print("\nThank you", name)
        print("Have a safe journey!")
        break

    else:
        print("\nInvalid choice. Please try again.")
