#!/usr/bin/python3
"""
lists all states from selected database
"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3],)
    with db.cursor() as cursor:
        cursor.execute("""
            SELECT
                *
            FROM
                states
            WHERE
                name = BINARY %(name)s
            """, {
                'name': argv[4]
            })
        data = cursor.fetchall()
    for item in data:
        print(item)
