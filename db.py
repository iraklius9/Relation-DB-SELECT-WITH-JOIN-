import sqlite3


def setup_database():
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()

    cursor.execute(''' 
    CREATE TABLE Advisor( 
        AdvisorID INTEGER NOT NULL, 
        AdvisorName TEXT NOT NULL, 
        PRIMARY KEY(AdvisorID) 
        )
    ''')
    cursor.execute('''
    CREATE TABLE Student(
        StudentID INTEGER PRIMARY KEY,
        StudentName TEXT NOT NULL,
        AdvisorIDs TEXT
        )
    ''')

    advisors = [
        (1, "John Paul"),
        (2, "Anthony Roy"),
        (3, "Raj Shetty"),
        (4, "Sam Reeds"),
        (5, "Arthur Clintwood")
    ]

    students = [
        (501, "Geek1", "1,2"),
        (502, "Geek2", "1"),
        (503, "Geek3", "3"),
        (504, "Geek4", "2"),
        (505, "Geek5", "4"),
        (506, "Geek6", "2,3"),
        (507, "Geek7", "2"),
        (508, "Geek8", "3,5"),
        (509, "Geek9", ""),
        (510, "Geek10", "1,4")
    ]

    cursor.executemany('INSERT INTO Advisor(AdvisorID, AdvisorName) VALUES (?, ?)', advisors)
    cursor.executemany('INSERT INTO Student(StudentID, StudentName, AdvisorIDs) VALUES (?, ?, ?)', students)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    setup_database()
