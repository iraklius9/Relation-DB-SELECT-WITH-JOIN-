# Student Advisor Management System

This project is a simple student advisor management system that stores information about advisors and their assigned students.



## Installation

To use this project, follow these steps:

1. Clone the repository.
2. Make sure you have Python installed.
3. Install the required dependencies (`sqlite3`).
4. Run the `setup_database()` function to initialize the SQLite database.

## Usage

Once the database is set up, you can use the provided functions to interact with it. The database schema includes two tables: `Advisor` and `Student`.

- `Advisor` table stores information about advisors, including `AdvisorID` and `AdvisorName`.
- `Student` table stores information about students, including `StudentID`, `StudentName`, and `AdvisorIDs` (a comma-separated list of advisor IDs).

To retrieve information about advisors and their assigned students, run the provided SQL query in the `main.py` file.
