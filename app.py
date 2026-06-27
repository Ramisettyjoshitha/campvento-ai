def welcome():
    print("=" * 50)
    print("CAMPVENTO".center(50))
    print("AI-Powered College Event Management Platform".center(50))
    print("=" * 50)
def main_menu():
    print("\n========== Main Menu ==========")
    print("1. Student Login")
    print("2. Club Admin Login")
    print("3. Exit")
    print("=" * 29)
def student_details():
    name = input("Enter your name: ")
    department = input("Enter your department: ")
    while True:
        try:
            year = int(input("Enter your year of study (1-4): "))
            if year in [1, 2, 3, 4]:
                break
            else:
                print(" Please enter 1, 2, 3, or 4.")
        except ValueError:
            print("Invalid input! Please enter a number.")
    print(f"\nWelcome, {name}!")
    print(f"Department: {department}")
    print(f"Year: {year}")
    return name,department,year
def college_events():
    print("\n" + "=" * 50)
    print("Today's College Events".center(50))
    print("=" * 50)
    print("1. AI Workshop")
    print("2. Hackathon")
    print("3. Coding Contest")
    print("4. Cultural Fest")
    print("5. Project Expo")
    print("6. Conference")
def registration(choice,name):
    if choice == 1:
        print("\nYou have successfully registered for AI Workshop.")
    elif choice == 2:
        print("\n You have successfully registered for Hackathon.")
    elif choice == 3:
        print("\n You have successfully registered for Coding Contest.")
    elif choice == 4:
        print("\n You have successfully registered for Cultural Fest.")
    elif choice == 5:
        print("\n You have successfully registered for Project Expo.")
    elif choice == 6:
        print("\n You have successfully registered for Conference.")
    print("🎉 Your registration has been confirmed.")
    print("We look forward to seeing you at the event!")
while True:
    welcome()
    main_menu()
    while True:
        try:
            role=int(input("\n enter your login choice (1-3):"))
            if 1<=role<=3:
                break
            else:
                print("please enter 1 or 2 or 3")
        except ValueError:
            print("invalid input,please enter a number")
    if role==1:
        print("you have selected student login")
        name,department,year=student_details()
        while True:
            college_events()
            while True:
                try:
                    choice=int(input("enter the event number you want to register(1-6):"))
                    if 1<=choice<=6:
                        break
                    else:
                        print("please enter a event number between 1 to 6:")
                except ValueError:
                     print("Invalid input! Please enter a number.")

            registration(choice, name)

            again = input("\nDo you want to register for another event? (Y/N): ").strip().upper()

            if again == "Y":
                continue

            elif again == "N":
                print(f"\nThank you, {name}, for registering through Campvento.")
                print("Logging out...\n")
                break

            else:
                print("Invalid choice. Logging out...")
                break

        continue
    elif role == 2:

        print("\nClub Admin Login Selected")
        print(" Club Admin Dashboard - Coming Soon")

        input("\nPress Enter to Logout...")

        continue

    elif role == 3:

        print("\nThank you for using Campvento!")
        print("Have a great day!")
        break
                    

    
    
