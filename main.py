# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import connect
from connect import dbhelper


def main():
    db = dbhelper()
    while True:
        print("IMDB LIST OF TOP 20 MOVIES OF ALL TIME")
        print("...Press 1 for See full List:")
        print("...Press 2 for Showing Single Movie Detail:")
        print("...Press 3 for Delete record")
        print()
        try:
            choice = int(input())
            if choice == 1:
                # Select Full List
                db.fetch_all()
                pass
            elif choice == 2:
                # Search Record by Id
                mid = int(input("Enter Movie Id:"))
                db.search(mid)
            elif choice == 3:
                # Delete Record by Id
                mid = int(input("Enter Movie Id:"))
                db.delete_rec(mid)
        except Exception as e:
            print(e)
            print("Invalid Data")


if __name__ == "__main__":
    main()
