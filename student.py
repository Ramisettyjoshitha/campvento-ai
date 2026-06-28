from event import events,college_events
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
Registered_events=[]
def registration(choice,name):
        selected_event=events[choice-1]
        if selected_event not in Registered_events:     
            print(f"you have sucessfully registered for {selected_event}")
            print("🎉 Your registration has been confirmed.")
            print(f"Thank you {name} for choosing campvento ,We look forward to seeing you at the event!")
            Registered_events.append(selected_event)
        else:
            print("you have already registered for this event")
        
def my_registration():
    print("\n======My Registered Events======")
    if len(Registered_events)==0:
        print("no events registered yet ")
    else:
        for i,event in enumerate(Registered_events,start=1):
            print(f"{i}.{event}")
def student_dashboard(name):
    while True:
        print("="*30)
        print("Student Dashboard".center(30))
        print("="*30)
        print("1.Browse events")
        print("2.My Registrations")
        print("3.logout")
        try:
            student_choice=int(input("enter your choice(1-3):"))
            if student_choice==1:
                while True:
                    college_events()
                    while True:
                        try:
                            choice=int(input("enter the event number(1-6):"))
                            if 1<=choice<=6:
                                break
                            else:
                                print("please enter a event number between 1 to 6:")
                        except ValueError:
                            print("Invalid input! Please enter a number.")
                    registration(choice,name)
                    again=input("\nDo you want to register for another event? (Y/N): ").strip().upper()
                    if again == "Y":
                        continue
                    elif again == "N":
                        my_registration()
                        print("\nReturning to Student Dashboard...")
                        break
                    else:
                        print("Invalid choice. Logging out...")
                        break         
            elif student_choice==2:
                my_registration()
            elif student_choice==3:
                print("logging out ...")
                break
            else:
                print("invalid input please choosse options provided")
        except ValueError:
            print("Invalid input! Please enter a number.")