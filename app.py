from student import student_signup
from student import student_login

from admin import admin_login

import database


def welcome():

    print("=" * 60)
    print("CAMPVENTO".center(60))
    print("AI-Powered College Event Management Platform".center(60))
    print("=" * 60)


def main_menu():

    while True:

        welcome()

        print("\n========== Main Menu ==========")

        print("1. Student Sign Up")
        print("2. Student Login")
        print("3. Club Admin Login")
        print("4. Exit")

        try:

            choice = int(input("\nEnter your choice: "))

            if choice == 1:

                student_signup()

            elif choice == 2:

                student_login()

            elif choice == 3:

                admin_login()

            elif choice == 4:

                print("\nThank you for using Campvento.")
                print("Good Bye!")
                break

            else:

                print("Please enter a number between 1 and 4.")

        except ValueError:

            print("Invalid input. Please enter a number.")


main_menu()