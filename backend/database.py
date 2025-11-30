import sqlite3
import os

def init_db():
    conn = sqlite3.connect('database/college.db')
    cursor = conn.cursor()
    
    # Create tables
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS faqs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            keywords TEXT,
            question TEXT,
            answer TEXT
        )
    ''')
    
    # Insert sample college data from synopsis
    faqs = [
        ("schedule class timetable", "What is the class schedule?", "Classes run from 9 AM to 5 PM. Check the notice board or college app for your specific timetable."),
        ("exam timetable dates", "When are the exams?", "Exam timetable is posted 2 weeks before exams start. Check academic section or ask faculty."),
        ("faculty professor details", "Who is my professor?", "Faculty list: Prof. Balram Yadav (Guide), Computer Science Dept. Email available on college portal."),
        ("library hours books", "Library timings?", "Library: 8 AM - 8 PM weekdays, 10 AM - 4 PM weekends. 2 books max for students."),
        ("assignment deadline submission", "Assignment deadlines?", "Assignments due every Friday 5 PM. Submit via college LMS portal."),
        ("notice updates events", "Latest campus notices?", "Check notice board or college website for events, holidays, and updates.")
    ]
    
    cursor.executemany("INSERT OR IGNORE INTO faqs (keywords, question, answer) VALUES (?, ?, ?)", faqs)
    conn.commit()
    conn.close()
    print("✅ Database created with sample FAQs")

if __name__ == "__main__":
    os.makedirs("database", exist_ok=True)
    init_db()
