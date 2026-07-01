import sqlite3
def college_events():

    conn = sqlite3.connect("campvento.db")
    c = conn.cursor()

    c.execute("""
    SELECT
    event_id,
    event_title,
    category,
    event_date,
    event_time,
    venue
    FROM events
    ORDER BY event_date
    """)

    events = c.fetchall()

    print("\n" + "=" * 90)
    print("Available College Events".center(90))
    print("=" * 90)

    if len(events) == 0:
        print("No events available.")

    else:
        for event in events:

            print(f"""
Event ID : {event[0]}
Title    : {event[1]}
Category : {event[2]}
Date     : {event[3]}
Time     : {event[4]}
Venue    : {event[5]}
{"-" * 90}
""")

    conn.close()


# Search events by title
def search_event():

    keyword = input("\nEnter event name: ")

    conn = sqlite3.connect("campvento.db")
    c = conn.cursor()

    c.execute("""
    SELECT
    event_id,
    event_title,
    category,
    event_date,
    event_time,
    venue
    FROM events
    WHERE event_title LIKE ?
    """, ('%' + keyword + '%',))

    results = c.fetchall()

    if len(results) == 0:

        print("\nNo matching events found.")

    else:

        print("\nSearch Results")

        for event in results:

            print(f"""
Event ID : {event[0]}
Title    : {event[1]}
Category : {event[2]}
Date     : {event[3]}
Time     : {event[4]}
Venue    : {event[5]}
{"-" * 90}
""")

    conn.close()


# Display complete details of one event
def event_details(event_id):

    conn = sqlite3.connect("campvento.db")
    c = conn.cursor()

    c.execute("""
    SELECT
    event_title,
    description,
    category,
    venue,
    event_date,
    event_time,
    registration_deadline,
    capacity
    FROM events
    WHERE event_id=?
    """, (event_id,))

    event = c.fetchone()

    conn.close()

    if event:

        print("\n========== Event Details ==========")

        print(f"Title                 : {event[0]}")
        print(f"Description           : {event[1]}")
        print(f"Category              : {event[2]}")
        print(f"Venue                 : {event[3]}")
        print(f"Date                  : {event[4]}")
        print(f"Time                  : {event[5]}")
        print(f"Registration Deadline : {event[6]}")
        print(f"Capacity              : {event[7]}")

    else:

        print("Event not found.")


# Return event title using event ID
def get_event_name(event_id):

    conn = sqlite3.connect("campvento.db")
    c = conn.cursor()

    c.execute("""
    SELECT event_title
    FROM events
    WHERE event_id=?
    """, (event_id,))

    event = c.fetchone()

    conn.close()

    if event:
        return event[0]

    return None