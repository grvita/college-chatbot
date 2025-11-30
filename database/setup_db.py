import sqlite3

# This path matches app.py: '../database/college.db'
conn = sqlite3.connect("college.db")
cur = conn.cursor()

# 1) Create students table
cur.execute("""
CREATE TABLE IF NOT EXISTS students (
    enrollment_no TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    branch TEXT NOT NULL,
    year_sem TEXT NOT NULL
)
""")

# 2) Insert one sample student (change details if you want)
cur.execute("""
INSERT OR REPLACE INTO students (enrollment_no, name, branch, year_sem)
VALUES (?, ?, ?, ?)
""", ("0704CS231062", "Test Student", "CSE", "1st Year - 2nd Sem"))

conn.commit()
conn.close()

print("Database ready with students table.")

