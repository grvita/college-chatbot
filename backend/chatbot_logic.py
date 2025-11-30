def find_response(user_message):
    """Rule-based keyword matching from synopsis"""
    user_lower = user_message.lower()
    
    faqs = [
        ("schedule class timetable", "What is the class schedule?", "Classes run from 9 AM to 5 PM. Check the notice board or college app for your specific timetable."),
        ("exam timetable dates", "When are the exams?", "Exam timetable is posted 2 weeks before exams start. Check academic section or ask faculty."),
        ("faculty professor details", "Who is my professor?", "Faculty list: Prof. Balram Yadav (Guide), Computer Science Dept. Email available on college portal."),
        ("library hours books", "Library timings?", "Library: 8 AM - 8 PM weekdays, 10 AM - 4 PM weekends. 2 books max for students."),
        ("assignment deadline submission", "Assignment deadlines?", "Assignments due every Friday 5 PM. Submit via college LMS portal."),
        ("notice updates events", "Latest campus notices?", "Check notice board or college website for events, holidays, and updates.")
    ]
    
    for keywords, question, answer in faqs:
        if any(word in user_lower for word in keywords.split()):
            return answer
    
    return "I can help with class schedules, exams, faculty, library, assignments, and notices. Try asking about those!"
