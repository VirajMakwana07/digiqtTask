import mysql.connector as connector


# connection string
class dbhelper:
    def __init__(self):
        self.con = connector.connect(
            host="localhost",
            user="root",
            password="",
            database="imdb"
        )

    # Select
    def fetch_all(self):
        query = "SELECT * FROM top20"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("ID:", row[0])
            print("Movie_Name:", row[1])
            print("Movie_Ratings:", row[2])
            print("Release Year:", row[3])
            print("Duration:", row[4])
            print("Description:", row[5])
            print()

    def search(self, mid):
        query = "SELECT * FROM top20 where Id={}".format(mid)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        row = cur.fetchone()
        print("\n")
        print(row)
        print("\n Search Completed")
        print()

    def delete_rec(self, mid):
        query = "DELETE FROM top20 where Id={}".format(mid)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Data Deleted")
