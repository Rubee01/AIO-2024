class Ward:
    def __init__(self, name: str):
        self.name = name
        self.record = []

    def add_person(self, person):
        self.record.append(person)

    def describe(self):
        print(f"Ward Name: {self.name}")
        for p in self.record:
            p.describe()

    def count_doctor(self):
        count = 0
        for p in self.record:
            if isinstance(p, Doctor):
                count += 1
        return count

    def sort_age(self):
        self.record.sort(key=lambda x: x.yob, reverse=True)

    def compute_average(self):
        total = 0
        count = 0
        for p in self.record:
            if isinstance(p, Teacher):
                total += p.yob
                count += 1
        return total/count


class Student:
    def __init__(self, name: str, yob: int, grade: str):
        self.name = name
        self.yob = yob
        self.grade = grade

    def describe(self):
        print(
            f"Student - Name: {self.name} - YoB: {self.yob} - Grade: {self.grade}")


class Teacher:
    def __init__(self, name: str, yob: int, subject: str):
        self.name = name
        self.yob = yob
        self.subject = subject

    def describe(self):
        print(
            f"Teacher - Name: {self.name} - YoB: {self.yob} - Subject: {self.subject}")


class Doctor:
    def __init__(self, name: str, yob: int, specialist: str):
        self.name = name
        self.yob = yob
        self.specialist = specialist

    def describe(self):
        print(
            f"Doctor - Name: {self.name} - YoB: {self.yob} - Specialist: {self.specialist}")


student1 = Student(name="studentA", yob=2010, grade="7")
teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")
ward1 = Ward(name="Ward1")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)
print(ward1.count_doctor())
