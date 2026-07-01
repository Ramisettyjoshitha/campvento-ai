import sqlite3
import csv
from datetime import datetime
from event import college_events, search_event, event_details


def admin_login():

    print("\n========== Club Admin Login ==========")

    email = input("Enter Admin Email: ")
    password = input("Enter Password: ")

    conn = sqlite3.connect("campvento.db")
    c = conn.cursor()

    c.execute("""
    SELECT
    admin_id,
    full_name,
    club_id
    FROM club_admins
    WHERE email=? AND password=?
    """,
    (email, password))

    admin = c.fetchone()

    conn.close()

    if admin:

        print(f"\nWelcome {admin[1]}")

        admin_dashboard(
            admin[0],
            admin[1],
            admin[2]
        )

    else:

        print("Invalid Email or Password.")


def create_event(admin_id, club_id):

    print("\n========== Create Event ==========")

    event_title = input("Event Title: ")
    description = input("Description: ")
    category = input("Category: ")
    venue = input("Venue: ")
    event_date = input("Event Date (YYYY-MM-DD): ")
    event_time = input("Event Time: ")
    registration_deadline = input("Registration Deadline (YYYY-MM-DD): ")

    while True:

        try:
            capacity = int(input("Capacity: "))
            break

        except ValueError:

            print("Please enter a valid number.")

    poster = input("Poster File Name (optional): ")

    created_at = datetime.now().strftime("%Y-%m-%d")

    conn = sqlite3.connect("campvento.db")
    c = conn.cursor()

    c.execute("""
    INSERT INTO events
    (
    event_title,
    description,
    category,
    venue,
    event_date,
    event_time,
    registration_deadline,
    capacity,
    poster,
    club_id,
    admin_id,
    created_at
    )
    VALUES
    (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """,
    (
    event_title,
    description,
    category,
    venue,
    event_date,
    event_time,
    registration_deadline,
    capacity,
    poster,
    club_id,
    admin_id,
    created_at
    ))

    conn.commit()
    conn.close()

    print("\nEvent created successfully.")
def update_event(admin_id):
    college_events()

    try:
        event_id = int(input("\nEnter Event ID to Update: "))
    except ValueError:
        print("Invalid Event ID.")
        return

    conn = sqlite3.connect("campvento.db")
    c = conn.cursor()

    c.execute("""
    SELECT *
    FROM events
    WHERE event_id=? AND admin_id=?
    """, (event_id, admin_id))

    event = c.fetchone()

    if event is None:
        print("Event not found or you are not authorized to update it.")
        conn.close()
        return

    print("\nLeave blank if you don't want to change a field.\n")

    event_title = input(f"Title [{event[1]}]: ")
    description = input(f"Description [{event[2]}]: ")
    category = input(f"Category [{event[3]}]: ")
    venue = input(f"Venue [{event[4]}]: ")
    event_date = input(f"Date [{event[5]}]: ")
    event_time = input(f"Time [{event[6]}]: ")
    registration_deadline = input(f"Deadline [{event[7]}]: ")
    capacity = input(f"Capacity [{event[8]}]: ")

    if event_title == "":
        event_title = event[1]

    if description == "":
        description = event[2]

    if category == "":
        category = event[3]

    if venue == "":
        venue = event[4]

    if event_date == "":
        event_date = event[5]

    if event_time == "":
        event_time = event[6]

    if registration_deadline == "":
        registration_deadline = event[7]

    if capacity == "":
        capacity = event[8]
    else:
        capacity = int(capacity)

    c.execute("""
    UPDATE events
    SET
    event_title=?,
    description=?,
    category=?,
    venue=?,
    event_date=?,
    event_time=?,
    registration_deadline=?,
    capacity=?
    WHERE event_id=?
    """,
    (
    event_title,
    description,
    category,
    venue,
    event_date,
    event_time,
    registration_deadline,
    capacity,
    event_id
    ))

    conn.commit()
    conn.close()

    print("\nEvent updated successfully.")


def delete_event(admin_id):

    college_events()

    try:
        event_id = int(input("\nEnter Event ID to Delete: "))
    except ValueError:
        print("Invalid Event ID.")
        return

    conn = sqlite3.connect("campvento.db")
    c = conn.cursor()

    c.execute("""
    SELECT event_title
    FROM events
    WHERE event_id=? AND admin_id=?
    """, (event_id, admin_id))

    event = c.fetchone()

    if event is None:
        print("Event not found or you are not authorized.")
        conn.close()
        return

    confirm = input(f"Delete '{event[0]}'? (Y/N): ").upper()

    if confirm == "Y":

        c.execute("""
        DELETE FROM events
        WHERE event_id=?
        """, (event_id,))

        conn.commit()

        print("Event deleted successfully.")

    else:

        print("Delete cancelled.")

    conn.close()


def view_events():

    college_events()


def search_events():

    search_event()


def view_event_details():

    try:
        event_id = int(input("\nEnter Event ID: "))
        event_details(event_id)

    except ValueError:
        print("Invalid Event ID.")
def view_registered_students():

    try:
        event_id = int(input("\nEnter Event ID: "))
    except ValueError:
        print("Invalid Event ID.")
        return

    conn = sqlite3.connect("campvento.db")
    c = conn.cursor()

    c.execute("""
    SELECT
    students.full_name,
    students.department,
    students.year,
    registrations.registration_date,
    registrations.status
    FROM registrations
    JOIN students
    ON registrations.student_id = students.student_id
    WHERE registrations.event_id=?
    """,
    (event_id,))

    students = c.fetchall()

    conn.close()

    if len(students) == 0:

        print("\nNo students registered.")

    else:

        print("\n========== Registered Students ==========")

        for i, student in enumerate(students, start=1):

            print(f"""
{i}
Name : {student[0]}
Department : {student[1]}
Year : {student[2]}
Registration Date : {student[3]}
Status : {student[4]}
----------------------------------------
""")


def export_csv():

    try:
        event_id = int(input("\nEnter Event ID: "))
    except ValueError:
        print("Invalid Event ID.")
        return

    conn = sqlite3.connect("campvento.db")
    c = conn.cursor()

    c.execute("""
    SELECT
    students.full_name,
    students.email,
    students.department,
    students.year,
    registrations.status
    FROM registrations
    JOIN students
    ON registrations.student_id = students.student_id
    WHERE registrations.event_id=?
    """,
    (event_id,))

    rows = c.fetchall()

    conn.close()

    if len(rows) == 0:

        print("No registrations found.")
        return

    filename = f"event_{event_id}_registrations.csv"

    with open(filename, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Student Name",
            "Email",
            "Department",
            "Year",
            "Status"
        ])

        writer.writerows(rows)

    print(f"\nCSV exported successfully as {filename}")


def admin_dashboard(admin_id, admin_name, club_id):

    while True:

        print("\n" + "=" * 40)
        print("Club Admin Dashboard".center(40))
        print("=" * 40)

        print(f"Welcome : {admin_name}")

        print("\n1. Create Event")
        print("2. View Events")
        print("3. Search Events")
        print("4. View Event Details")
        print("5. Update Event")
        print("6. Delete Event")
        print("7. View Registered Students")
        print("8. Export Registration CSV")
        print("9. Logout")

        try:

            choice = int(input("\nEnter your choice: "))

            if choice == 1:

                create_event(admin_id, club_id)

            elif choice == 2:

                view_events()

            elif choice == 3:

                search_events()

            elif choice == 4:

                view_event_details()

            elif choice == 5:

                update_event(admin_id)

            elif choice == 6:

                delete_event(admin_id)

            elif choice == 7:

                view_registered_students()

            elif choice == 8:

                export_csv()

            elif choice == 9:

                print("\nLogging out...")
                break

            else:

                print("Please enter a number between 1 and 9.")

        except ValueError:

            print("Invalid input. Please enter a number.")