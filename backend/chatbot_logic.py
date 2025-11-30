import sqlite3
import random

def find_response(user_message):
    """Enhanced rule-based matching with categories"""
    user_lower = user_message.lower().strip()
    
    conn = sqlite3.connect('../database/college.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT keywords, question, answer FROM faqs")
    faqs = cursor.fetchall()
    conn.close()
    
    # Multiple keyword matching
    for keywords, question, answer in faqs:
        keyword_list = keywords.split()
        if sum(1 for word in keyword_list if word in user_lower) >= 1:
            return answer
    
    # Fallback responses by category
    responses = {
        "schedule": "Try asking about class timetable, semester dates",
        "exams": "Ask about exam schedule, results, attendance",
        "faculty": "Need professor details or HOD location?",
        "library": "Library timings or rules?",
        "academics": "Assignment deadlines or syllabus?",
        "admin": "Fees, ID card, certificates?",
        "campus": "Canteen, hostel, WiFi?",
        "events": "Fest dates or holidays?"
    }
    
    fallback = random.choice([
        "I can help with academics, exams, faculty, library, fees, hostel, events. What do you need?",
        "Try: 'class schedule', 'exam dates', 'library timing', 'faculty details', 'fee payment'",
        "Available 24/7 for college info! Ask about schedules, exams, or campus facilities."
    ])
    
    return fallback
