from student import student_details, student_dashboard
from admin import admin_dashboard
def welcome():
    print("=" * 50)
    print("CAMPVENTO".center(50))
    print("AI-Powered College Event Management Platform".center(50))
    print("=" * 50)
def main_menu():
    print("\n========== Main Menu ==========")
    print("1. Student Login")
    print("2. Club Admin Login")
    print("3. Exit")
    print("=" * 29)
while True:
    welcome()
    main_menu()
    while True:
        try:
            role=int(input("\n enter your login choice (1-3):"))
            if 1<=role<=3:
                break
            else:
                print("please enter 1 or 2 or 3")
        except ValueError:
            print("invalid input,please enter a number")
    if role==1:
        print("you have selected student login")
        name,department,year=student_details()
        student_dashboard(name)
    elif role == 2: 
        print("\nClub Admin Login Selected")
        admin_dashboard()
    elif role == 3:
        print("\nThank you for using Campvento!")
        print("Have a great day!")
        break
