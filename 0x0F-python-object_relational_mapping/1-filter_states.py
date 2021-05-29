#!/usr/bin/python3
"""
lists all states from selected database
"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states")
    data = cursor.fetchall()
    for item in data:
        if item[1][0] == "N":
            print(item)
