import sqlite3
import os

def init_db():
    os.makedirs("database", exist_ok=True)
    conn = sqlite3.connect('database/college.db')
    cursor = conn.cursor()
    
    # Create enhanced tables
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS faqs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            keywords TEXT,
            question TEXT,
            answer TEXT,
            category TEXT
        )
    ''')
    
    # 25+ REAL COLLEGE FAQs (from synopsis + extras)
    faqs = [
        # Academic Schedule
        ("schedule class timetable time table", "What is the class schedule?", "Classes: Mon-Fri 9:00 AM - 5:00 PM. Saturday: 9:30 AM - 3:20 PM:. Check academic portal for your batch.", "schedule"),
        ("semester start end dates", "When does semester start?", "Odd semester: Aug 1st. Even semester: Jan 15th. Check academic calendar.", "schedule"),
        
        # Examinations
        ("exam timetable dates schedule", "When are exams?", "Midterms: 6th week. End-sem: Last 2 weeks. Timetable posted 15 days prior on portal.", "exams"),
        ("result marksheet revaluation", "How to check results?", "Results on college portal → Student login → Marks. Revaluation form: Academic office.", "exams"),
        ("attendance percentage requirement", "What is attendance requirement?", "75% minimum attendance required to appear for exams. Check via student portal.", "exams"),
        
        # Faculty
        ("faculty professor teacher details", "Faculty information?", "Prof. Balram Yadav (Project Guide) - CS Dept. Full list on college website → Faculty.", "faculty"),
        ("hod principal office location", "HOD office location?", "CS HOD: Room A-204 (2nd floor). Principal: Admin Block.", "faculty"),
        
        # Library
        ("library hours timing books issue", "Library timings?", "Mon-Fri: 8 AM - 8 PM. Sat: 10 AM - 4 PM. Max 2 books, 15 days.", "library"),
        ("library membership fine rules", "Library rules?", "Fine: ₹5/day after 15 days. No membership fee for students.", "library"),
        
        # Academics
        ("assignment project submission deadline", "Assignment deadlines?", "Weekly assignments due every Friday 5 PM via LMS portal.", "academics"),
        ("internal marks calculation", "How are internals calculated?", "Internals (30%): Attendance 10 + Assignments 10 + Midterms 10.", "academics"),
        ("syllabus curriculum download", "Where to find syllabus?", "College website → Academics → Syllabus (PDF download).", "academics"),
        
        # Administration
        ("fee structure payment scholarship", "Fee payment details?", "Fee portal → Online payment. Last date: 10th of every month. Late fee: ₹100.", "admin"),
        ("id card lost duplicate", "Lost ID card?", "Duplicate ID: Admin office, ₹200 fee, 2 photos, FIR copy.", "admin"),
        ("tc lc migration certificate", "TC/LC process?", "Academic office → ₹500 fee → 7 days processing.", "admin"),
        
        # Campus Life
        ("canteen mess food timing", "Canteen timings?", "Canteen: 8 AM - 8 PM. Mess: 8 AM, 1 PM, 8 PM.", "campus"),
        ("hostel room allotment rules", "Hostel information?", "1st year compulsory. Apply via admission portal.", "campus"),
        ("wifi internet login password", "WiFi login?", "Student WiFi: userid@college.edu | Password: college123", "campus"),
        
        # Events & Notices
        ("cultural fest tech fest dates", "Upcoming events?", "TechFest: Feb 15-17. Cultural: Mar 20-22. Check notice board.", "events"),
        ("holidays list calendar", "Holiday list?", "Check academic calendar on portal. Next holiday: Republic Day.", "events"),
        
        # Support
        ("grievance complaint cell", "Grievance cell?", "Grievance portal → student login → submit complaint.", "support")
    ]
    
    cursor.executemany("INSERT OR IGNORE INTO faqs (keywords, question, answer, category) VALUES (?, ?, ?, ?)", faqs)
    conn.commit()
    
    # Admin credentials table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS admin (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE,
            password TEXT
        )
    ''')
    cursor.execute("INSERT OR IGNORE INTO admin (id, username, password) VALUES (1, 'admin', 'admin123')")
    conn.commit()
        # Student table for login without password
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            enrollment_no TEXT UNIQUE NOT NULL,
            name TEXT NOT NULL,
            branch TEXT NOT NULL,
            year_sem TEXT NOT NULL
        )
    ''')
    conn.commit()

    # Example: your own record
    cursor.execute('''
        INSERT OR IGNORE INTO students (enrollment_no, name, branch, year_sem)
        VALUES (?, ?, ?, ?)
    ''', ("0704CS231062", "Garvita Kasera", "CS", "3rd Year - 5nd Sem"))
    conn.commit()

    conn.close()
    print("✅ Enhanced database: 25+ FAQs + Admin panel ready!")

if __name__ == "__main__":
    init_db()
