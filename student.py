from event import college_events
from datetime import datetime
import sqlite3


def student_details():
    name = input("Enter your name: ")
    department = input("Enter your department: ")

    while True:
        try:
            year = int(input("Enter your year of study (1-4): "))
            if year in [1, 2, 3, 4]:
                break
            else:
                print("Please enter 1, 2, 3, or 4.")
        except ValueError:
            print("Invalid input! Please enter a number.")

    print(f"\nWelcome, {name}!")
    print(f"Department: {department}")
    print(f"Year: {year}")

    return name, department, year


def registration(choice, name, department, year):

    registration_date = datetime.now().strftime("%Y-%m-%d")

    conn = sqlite3.connect("campvento.db")
    c = conn.cursor()

    # Get selected event from database
    c.execute(
        "SELECT event_name FROM eventtable WHERE id=?",
        (choice,)
    )

    event = c.fetchone()

    if event:

        selected_event = event[0]

        # Check duplicate registration
        c.execute(
            """
            SELECT * FROM registrationtable
            WHERE student_name=? AND event_name=?
            """,
            (name, selected_event)
        )

        already_registered = c.fetchone()

        if already_registered:
            print("You have already registered for this event.")

        else:
            c.execute(
                """
                INSERT INTO registrationtable
                (student_name, department, year, event_name, registration_date)
                VALUES (?, ?, ?, ?, ?)
                """,
                (name, department, year, selected_event, registration_date)
            )

            conn.commit()

            print(f"\nSuccessfully registered for {selected_event}.")
            print("Registration confirmed.")

    else:
        print("Invalid event selected.")

    conn.close()


def my_registration(name):

    print("\n====== My Registered Events ======")

    conn = sqlite3.connect("campvento.db")
    c = conn.cursor()

    c.execute(
        "SELECT event_name FROM registrationtable WHERE student_name=?",
        (name,)
    )

    registrations = c.fetchall()

    if len(registrations) == 0:
        print("No registrations yet.")
    else:
        for i, event in enumerate(registrations, start=1):
            print(f"{i}. {event[0]}")

    conn.close()


def student_dashboard(name, department, year):

    while True:

        print("=" * 30)
        print("Student Dashboard".center(30))
        print("=" * 30)
        print("1. Browse Events")
        print("2. My Registrations")
        print("3. Logout")

        try:

            student_choice = int(input("Enter your choice (1-3): "))

            if student_choice == 1:

                while True:

                    college_events()

                    while True:

                        try:
                            choice = int(input("Enter the event number: "))

                            conn = sqlite3.connect("campvento.db")
                            c = conn.cursor()
                            c.execute("SELECT COUNT(*) FROM eventtable")
                            total_events = c.fetchone()[0]
                            conn.close()

                            if 1 <= choice <= total_events:
                                break
                            else:
                                print(f"Please enter a number between 1 and {total_events}.")

                        except ValueError:
                            print("Invalid input! Please enter a number.")

                    registration(choice, name, department, year)

                    again = input(
                        "\nDo you want to register for another event? (Y/N): "
                    ).strip().upper()

                    if again == "Y":
                        continue

                    elif again == "N":
                        my_registration(name)
                        print("\nReturning to Student Dashboard...")
                        break

                    else:
                        print("Invalid choice.")
                        break

            elif student_choice == 2:
                my_registration(name)

            elif student_choice == 3:
                print("Logging out...")
                break

            else:
                print("Please choose 1, 2, or 3.")

        except ValueError:
            print("Invalid input! Please enter a number.")