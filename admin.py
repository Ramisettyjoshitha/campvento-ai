from event import events,college_events
def admin_dashboard():
    while True:
        print("="*30)
        print("Club Admin Dashboard".center(30))
        print("="*30)
        print("1.Add event")
        print("2. View event")
        print("3. Delete event")
        print("4. Log out")
        try:
            admin_choice=int(input("enter your choice(1-4):"))
            if admin_choice==1:
                add_event=input("enter the event you want to create:")
                events.append(add_event)
                print(f"\n {add_event} has been added successfully in the events")
                college_events()
            elif admin_choice==2:
                print("======Available events======")
                college_events()
            elif admin_choice==3:
                print("delete event selected")
                college_events()
                try:
                    delete_event=int(input("enter the event number you want to delete:"))
                    if 1<=delete_event<=len(events):
                        deleted_event=events.pop(delete_event-1)
                        print(f"{deleted_event} has been deleted successfully")
                        print("\n updated events list")
                        college_events()
                    else:
                        print("\n please enter a valid number")  
                except ValueError:
                    print("invalid input please enter valid number")
            elif admin_choice==4:
                print("logging out")
                break
            else:
                print("Please enter a number between 1 and 4")
        except ValueError:
            print("Invalid input! Please enter a number")

