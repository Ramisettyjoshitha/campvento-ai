import sqlite3
from datetime import datetime

conn = sqlite3.connect("campvento.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS students(
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    department TEXT NOT NULL,
    year INTEGER NOT NULL,
    phone TEXT,
    created_at TEXT
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS clubs(
    club_id INTEGER PRIMARY KEY AUTOINCREMENT,
    club_name TEXT UNIQUE NOT NULL,
    faculty_coordinator TEXT,
    description TEXT
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS club_admins(
    admin_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    phone TEXT,
    club_id INTEGER,
    FOREIGN KEY(club_id) REFERENCES clubs(club_id)
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS events(
    event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_title TEXT NOT NULL,
    description TEXT,
    category TEXT,
    venue TEXT,
    event_date TEXT,
    event_time TEXT,
    registration_deadline TEXT,
    capacity INTEGER,
    poster TEXT,
    club_id INTEGER,
    admin_id INTEGER,
    created_at TEXT,
    FOREIGN KEY(club_id) REFERENCES clubs(club_id),
    FOREIGN KEY(admin_id) REFERENCES club_admins(admin_id)
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS registrations(
    registration_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    event_id INTEGER,
    registration_date TEXT,
    status TEXT,
    FOREIGN KEY(student_id) REFERENCES students(student_id),
    FOREIGN KEY(event_id) REFERENCES events(event_id)
)
""")

c.execute("SELECT COUNT(*) FROM clubs")
count = c.fetchone()[0]

if count == 0:

    clubs = [
        ("Coding Club", "Dr. Arun", "Programming and Coding Activities"),
        ("CSI", "Dr. Priya", "Computer Society of India"),
        ("IEEE", "Dr. Kumar", "Technology and Innovation"),
        ("GDSC", "Dr. Meena", "Google Developer Student Club"),
        ("Cultural Club", "Dr. Raj", "Arts and Cultural Events"),
        ("Sports Club", "Dr. Ravi", "Sports Activities")
    ]

    c.executemany("""
    INSERT INTO clubs
    (club_name, faculty_coordinator, description)
    VALUES (?, ?, ?)
    """, clubs)

    print("Default clubs inserted.")

c.execute("SELECT COUNT(*) FROM club_admins")
count = c.fetchone()[0]

if count == 0:

    admins = [
        ("Coding Admin", "coding@campvento.com", "coding123", "9876543210", 1),
        ("CSI Admin", "csi@campvento.com", "csi123", "9876543211", 2),
        ("IEEE Admin", "ieee@campvento.com", "ieee123", "9876543212", 3),
        ("GDSC Admin", "gdsc@campvento.com", "gdsc123", "9876543213", 4),
        ("Cultural Admin", "culture@campvento.com", "culture123", "9876543214", 5),
        ("Sports Admin", "sports@campvento.com", "sports123", "9876543215", 6)
    ]

    c.executemany("""
    INSERT INTO club_admins
    (full_name, email, password, phone, club_id)
    VALUES (?, ?, ?, ?, ?)
    """, admins)

    print("Default admins inserted.")

c.execute("SELECT COUNT(*) FROM events")
count = c.fetchone()[0]

if count == 0:

    today = datetime.now().strftime("%Y-%m-%d")

    events = [
        (
            "AI Workshop",
            "Introduction to Artificial Intelligence",
            "Workshop",
            "Seminar Hall",
            "2026-07-10",
            "10:00 AM",
            "2026-07-08",
            100,
            "",
            1,
            1,
            today
        ),
        (
            "Hackathon",
            "24 Hour Coding Challenge",
            "Technical",
            "Lab 3",
            "2026-07-15",
            "09:00 AM",
            "2026-07-12",
            150,
            "",
            1,
            1,
            today
        ),
        (
            "Coding Contest",
            "Competitive Programming Competition",
            "Technical",
            "Lab 1",
            "2026-07-18",
            "09:30 AM",
            "2026-07-16",
            120,
            "",
            2,
            2,
            today
        ),
        (
            "Project Expo",
            "Display Innovative Student Projects",
            "Expo",
            "Auditorium",
            "2026-07-20",
            "11:00 AM",
            "2026-07-18",
            200,
            "",
            3,
            3,
            today
        ),
        (
            "Cultural Fest",
            "Dance, Music and Drama Events",
            "Cultural",
            "Open Stage",
            "2026-07-25",
            "05:00 PM",
            "2026-07-22",
            300,
            "",
            5,
            5,
            today
        ),
        (
            "Sports Meet",
            "Indoor and Outdoor Sports",
            "Sports",
            "College Ground",
            "2026-07-30",
            "08:00 AM",
            "2026-07-28",
            250,
            "",
            6,
            6,
            today
        )
    ]

    c.executemany("""
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
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, events)

    print("Default events inserted.")

conn.commit()
conn.close()

print("\nCampvento database created successfully.")
print("All tables created successfully.")