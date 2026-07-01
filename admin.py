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
                import sqlite3
                conn=sqlite3.connect("campvento.db")
                c=conn.cursor()
                c.execute("INSERT INTO eventtable (event_name) VALUES(?)",(add_event,))
                conn.commit()
                conn.close()
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
                    import sqlite3
                    conn=sqlite3.connect("campvento.db")
                    c=conn.cursor()
                    c.execute("SELECT event_name FROM eventtable WHERE id=?",(delete_event,))
                    event = c.fetchone()
                    if event:
                        c.execute("DELETE FROM eventtable WHERE id=?",(delete_event,))
                        print(f"{event[0]} deleted sucessfully")
                        conn.commit()
                        college_events()
                    else:
                        conn.close()
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

