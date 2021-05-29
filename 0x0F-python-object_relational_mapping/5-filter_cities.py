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
                cities.name
            FROM
                states
            JOIN
                cities
            ON
                states.id = cities.state_id
            WHERE
                states.name = BINARY %(name)s
            """, {
                'name': argv[4]
            })
        data = cursor.fetchall()
    if len(data) == 0:
        print()
    for x in range(len(data)):
        if x != len(data) - 1:
            print("{}, ".format(data[x][0]), end="")
        else:
            print(data[x][0])
