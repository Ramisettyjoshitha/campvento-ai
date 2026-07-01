import sqlite3
from datetime import datetime
from event import college_events, search_event, event_details, get_event_name


def student_signup():

    print("\n========== Student Sign Up ==========")

    full_name = input("Enter Full Name: ")
    email = input("Enter College Email: ")
    password = input("Create Password: ")
    department = input("Enter Department: ")

    while True:
        try:
            year = int(input("Enter Year (1-4): "))
            if year in [1, 2, 3, 4]:
                break
            else:
                print("Please enter 1, 2, 3 or 4.")
        except ValueError:
            print("Invalid input.")

    phone = input("Enter Phone Number: ")

    created_at = datetime.now().strftime("%Y-%m-%d")

    conn = sqlite3.connect("campvento.db")
    c = conn.cursor()

    c.execute(
        "SELECT * FROM students WHERE email=?",
        (email,)
    )

    student = c.fetchone()

    if student:
        print("\nEmail already registered.")

    else:
        c.execute("""
        INSERT INTO students
        (
        full_name,
        email,
        password,
        department,
        year,
        phone,
        created_at
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
        full_name,
        email,
        password,
        department,
        year,
        phone,
        created_at
        ))

        conn.commit()

        print("\nStudent account created successfully.")

    conn.close()


def student_login():

    print("\n========== Student Login ==========")

    email = input("Enter Email: ")
    password = input("Enter Password: ")

    conn = sqlite3.connect("campvento.db")
    c = conn.cursor()

    c.execute("""
    SELECT
    student_id,
    full_name,
    department,
    year,
    email
    FROM students
    WHERE email=? AND password=?
    """,
    (email, password))

    student = c.fetchone()

    conn.close()

    if student:

        print(f"\nWelcome {student[1]}")

        student_dashboard(
            student[0],
            student[1],
            student[2],
            student[3],
            student[4]
        )

    else:

        print("\nInvalid Email or Password.")
def browse_events():

    while True:

        print("\n========== Browse Events ==========")
        print("1. View All Events")
        print("2. Search Event")
        print("3. View Event Details")
        print("4. Back")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                college_events()

            elif choice == 2:
                search_event()

            elif choice == 3:

                try:
                    event_id = int(input("Enter Event ID: "))
                    event_details(event_id)

                except ValueError:
                    print("Invalid Event ID.")

            elif choice == 4:
                break

            else:
                print("Please choose between 1 and 4.")

        except ValueError:
            print("Invalid input.")


def register_event(student_id):

    college_events()

    try:

        event_id = int(input("\nEnter Event ID to Register: "))

    except ValueError:

        print("Invalid Event ID.")
        return

    conn = sqlite3.connect("campvento.db")
    c = conn.cursor()

    c.execute(
        "SELECT * FROM events WHERE event_id=?",
        (event_id,)
    )

    event = c.fetchone()

    if event is None:

        print("Event not found.")
        conn.close()
        return

    c.execute("""
    SELECT *
    FROM registrations
    WHERE student_id=? AND event_id=?
    """,
    (student_id, event_id))

    already_registered = c.fetchone()

    if already_registered:

        print("You have already registered for this event.")

    else:

        registration_date = datetime.now().strftime("%Y-%m-%d")

        c.execute("""
        INSERT INTO registrations
        (
        student_id,
        event_id,
        registration_date,
        status
        )
        VALUES (?, ?, ?, ?)
        """,
        (
        student_id,
        event_id,
        registration_date,
        "Registered"
        ))

        conn.commit()

        event_name = get_event_name(event_id)

        print(f"\nSuccessfully registered for {event_name}")

    conn.close()


def cancel_registration(student_id):

    conn = sqlite3.connect("campvento.db")
    c = conn.cursor()

    c.execute("""
    SELECT
    registrations.registration_id,
    events.event_title
    FROM registrations
    JOIN events
    ON registrations.event_id = events.event_id
    WHERE registrations.student_id=?
    AND registrations.status='Registered'
    """,
    (student_id,))

    registrations = c.fetchall()

    if len(registrations) == 0:

        print("\nNo active registrations.")

        conn.close()
        return

    print("\n====== Registered Events ======")

    for registration in registrations:

        print(registration[0], "-", registration[1])

    try:

        registration_id = int(
            input("\nEnter Registration ID to Cancel: ")
        )

    except ValueError:

        print("Invalid input.")
        conn.close()
        return

    c.execute("""
    UPDATE registrations
    SET status='Cancelled'
    WHERE registration_id=?
    """,
    (registration_id,))

    conn.commit()

    if c.rowcount > 0:

        print("Registration cancelled successfully.")

    else:

        print("Registration ID not found.")

    conn.close()
def my_registrations(student_id):

    conn = sqlite3.connect("campvento.db")
    c = conn.cursor()

    c.execute("""
    SELECT
    events.event_title,
    events.category,
    events.event_date,
    events.event_time,
    registrations.status
    FROM registrations
    JOIN events
    ON registrations.event_id = events.event_id
    WHERE registrations.student_id=?
    ORDER BY events.event_date
    """,
    (student_id,))

    registrations = c.fetchall()

    print("\n========== My Registrations ==========")

    if len(registrations) == 0:

        print("No registrations found.")

    else:

        for i, registration in enumerate(registrations, start=1):

            print(f"""
{i}.
Event      : {registration[0]}
Category   : {registration[1]}
Date       : {registration[2]}
Time       : {registration[3]}
Status     : {registration[4]}
-------------------------------
""")

    conn.close()


def student_profile(student_id):

    conn = sqlite3.connect("campvento.db")
    c = conn.cursor()

    c.execute("""
    SELECT
    full_name,
    email,
    department,
    year,
    phone,
    created_at
    FROM students
    WHERE student_id=?
    """,
    (student_id,))

    student = c.fetchone()

    conn.close()

    if student:

        print("\n========== Student Profile ==========")

        print(f"Name        : {student[0]}")
        print(f"Email       : {student[1]}")
        print(f"Department  : {student[2]}")
        print(f"Year        : {student[3]}")
        print(f"Phone       : {student[4]}")
        print(f"Joined On   : {student[5]}")

    else:

        print("Student not found.")


def student_dashboard(student_id, full_name, department, year, email):

    while True:

        print("\n" + "=" * 40)
        print("Student Dashboard".center(40))
        print("=" * 40)

        print(f"Welcome : {full_name}")
        print(f"Department : {department}")
        print(f"Year : {year}")

        print("\n1. Browse Events")
        print("2. Register Event")
        print("3. Cancel Registration")
        print("4. My Registrations")
        print("5. My Profile")
        print("6. Logout")

        try:

            choice = int(input("\nEnter your choice: "))

            if choice == 1:

                browse_events()

            elif choice == 2:

                register_event(student_id)

            elif choice == 3:

                cancel_registration(student_id)

            elif choice == 4:

                my_registrations(student_id)

            elif choice == 5:

                student_profile(student_id)

            elif choice == 6:

                print("\nLogging out...")
                break

            else:

                print("Please enter a number between 1 and 6.")

        except ValueError:

            print("Invalid input. Please enter a number.")