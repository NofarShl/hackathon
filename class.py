class Course:
    def __init__(self, type, faculty, course_number, course_name, professor, final, exam_date, nakaz):
        self.type = type
        self.faculty = faculty
        self.course_number = course_number
        self.course_name = course_name
        self.professor = professor
        self.final = final
        self.exam_date = exam_date
        self.nakaz = nakaz

    def gettype(self):
        return self.type

    def getfaculty(self):
        return self.faculty

    def getcourse_number(self):
        return self.course_number

    def getcourse_name(self):
        return self.course_name

    def getprofessor(self):
        return self.professor

    def getfinal(self):
        return self.final

    def getexam_date(self):
        return self.exam_date

    def getnakaz(self):
        return self.nakaz
