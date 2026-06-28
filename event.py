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
    for i,event in enumerate(events,start=1):
        print(f"{i}.{event}")