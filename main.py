from db import setup_database
import sqlite3

setup_database()

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cursor.execute('''
    SELECT Advisor.AdvisorID, Advisor.AdvisorName, COUNT(Student.StudentID) AS StudentCount
    FROM Advisor
    JOIN Student ON Student.AdvisorIDs LIKE '%' || Advisor.AdvisorID || '%'
    GROUP BY Advisor.AdvisorID
    ORDER BY Advisor.AdvisorID;
    ''')

for row in cursor.fetchall():
    print(f"ID: {row[0]}, Name: {row[1]}, Number of Students: {row[2]}")

conn.close()
