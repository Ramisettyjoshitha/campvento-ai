from event import events
import sqlite3
conn=sqlite3.connect("campvento.db")
c=conn.cursor()
c.execute(""" CREATE TABLE IF NOT EXISTS eventtable(
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          event_name TEXT NOT NULL
          )
""")
c.execute(""" CREATE TABLE IF NOT EXISTS registrationtable(
          registration_id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_name TEXT NOT NULL,
        department TEXT NOT NULL,
        year INTEGER NOT NULL,
        event_name TEXT NOT NULL,
        registration_date TEXT NOT NULL

          )
""")
c.execute("SELECT COUNT(*) FROM eventtable")
count=c.fetchone()[0]
if count==0:
    for event in events:
         c.execute("INSERT INTO eventtable (event_name) VALUES (?)",(event,))
    print("Default events inserted successfully.")
else:
     print("the table already exists default events")

conn.commit()
conn.close()
print("database and events table sucessfully created")
