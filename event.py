events = [
    "AI Workshop",
    "Hackathon",
    "Coding Contest",
    "Cultural Fest",
    "Project Expo",
    "Conference"
]
def college_events():
    print("\n" + "=" * 50)
    print("Today's College Events".center(50))
    print("=" * 50)
    import sqlite3
    conn=sqlite3.connect("campvento.db")
    c=conn.cursor()
    c.execute("SELECT * FROM eventtable")
    all_events=c.fetchall()
    for i,event in enumerate(all_events,start=1):
        print(f"{i}.{event[1]}")
    conn.close()
    