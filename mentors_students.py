# superclass Mentors
class Mentors:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

# class Reviewer
class Reviewer(Mentors):
    role = 'Эксперт, проверяющий домашние задание'
    def __str__(self):
        # collect reviewer info
        reviewer_info = 'Роль: ' + self.role + '\n' + 'Имя: ' + self.name + '\n' + 'Фамилия: ' + self.surname 
        return f"{reviewer_info}"

    # rate home work
    def rate_homework(self, student, course, estimation):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.courses_estimations:
                student.courses_estimations[course] += estimation
            else:
                student.courses_estimations[course] = estimation


# class Lecturer
class Lecturer(Mentors):       
    role = 'Лектор'
    def __init__(self, name, surname):
        super().__init__(name, surname)
        # list of estimations for lectures
        self.estimations_for_lectures = {}

    # count avarage of estimation
    def count_avarage(self):
        all_estimations = []
        for lst in self.estimations_for_lectures.values():
            all_estimations += lst
        avg = sum(all_estimations) / len(all_estimations)
        return avg 

    def __str__(self):
        # collect avarage
        avg = 'Средняя оценка за лекции: ' + str(self.count_avarage())
        # collect sudent info
        lecturer_info = 'Роль: ' + self.role + '\n' + 'Имя: ' + self.name + '\n' + 'Фамилия: ' + self.surname + '\n' + avg 
        return f"{lecturer_info}"

    # compare
    # less than
    def __lt__(self, other):
        if isinstance(other,Lecturer):
            self_avg = self.count_avarage()
            other_avg = other.count_avarage()
            return self_avg < other_avg
   
    # more then
    def __gt__(self, other):
        if isinstance(other,Lecturer):
            self_avg = self.count_avarage()
            other_avg = other.count_avarage()
            return self_avg > other_avg
    # equal
    def __eq__(self, other):
        if isinstance(other,Lecturer):
            self_avg = self.count_avarage()
            other_avg = other.count_avarage()
            return self_avg == other_avg


# class Student
class Student:
    role = 'Студент'
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_in_progress = []
        self.finished_courses = []
        self.courses_estimations = {}
    
    def count_avarage(self):
        avg = sum(self.courses_estimations.values()) / len(self.courses_estimations.values())
        return avg 

    def __str__(self):
        # collect finished courses
        finished = "Завершенные курсы: "
        for course in self.finished_courses:
            finished += ' ' + course
        # collect courses in progress
        in_progress = "Курсы в процессе изучения: "
        for course in self.courses_in_progress:
            in_progress += ' ' + course
        # collect avarage
        avg = 'Средняя оценка за домашние задания: ' + str(self.count_avarage())
        # collect sudent info
        sudent_info = 'Роль: ' + self.role + '\n' + 'Имя: ' + self.name + '\n' + 'Фамилия: ' + self.surname + '\n' + avg + '\n' + in_progress + '\n'+ finished 
        return f"{sudent_info}"

    # finish_course
    def finish_course(self, course):
        if course in self.courses_in_progress and course in self.courses_estimations.keys() and course not in self.finished_courses:
            self.finished_courses.append(course)
            self.courses_in_progress.remove(course)

    # estimate Lecturer 
    def give_estimation(self, lecturer, course, estimation):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.estimations_for_lectures.keys() and 0 < estimation <= 10:
                lecturer.estimations_for_lectures[course].append(estimation)
            else:
                lecturer.estimations_for_lectures[course] = [estimation]
    # compare
    # less than
    def __lt__(self, other):
        if isinstance(other,Student):
            self_avg = self.count_avarage()
            other_avg = other.count_avarage()
            return self_avg < other_avg
   
    # more then
    def __gt__(self, other):
        if isinstance(other,Student):
            self_avg = self.count_avarage()
            other_avg = other.count_avarage()
            return self_avg > other_avg
    # equal
    def __eq__(self, other):
        if isinstance(other,Student):
            self_avg = self.count_avarage()
            other_avg = other.count_avarage()
            return self_avg == other_avg


def total_avg( lst, course ):
    std_estimations = []
    lct_estimations = []
    for item in lst:
        if isinstance(item, Student):
            std_estimations.append(item.courses_estimations[course])
        elif isinstance(item, Lecturer):
            lct_estimations += item.estimations_for_lectures[course]
    if len(std_estimations) > 0 and len(lct_estimations) == 0:
        avg = sum(std_estimations) / len(std_estimations)
    elif len(lct_estimations) > 0 and len(std_estimations) == 0:  
        avg = sum(lct_estimations) / len(lct_estimations)   
    return avg 

# create Reviewer object
reviewer = Reviewer('Ivan','Ivanov')
reviewer.courses_attached.append('python')
reviewer.courses_attached.append('c#')

# create Lecturer object
lecturer = Lecturer('Piotr','Petrov')
lecturer.courses_attached.append('python')
lecturer.courses_attached.append('c#')

# create Lecturer object
lecturer1 = Lecturer('Piotr1','Petrov1')
lecturer1.courses_attached.append('python')
lecturer1.courses_attached.append('c#')

# create Student object
student = Student('Sydor','Sydorov')
student.courses_in_progress.append('python')
student.courses_in_progress.append('c#')
# create Student object
student1 = Student('Sydor1','Sydorov1')
student1.courses_in_progress.append('python')
student1.courses_in_progress.append('c#')

reviewer.rate_homework(student,'python',5)
reviewer.rate_homework(student,'c#',4)

reviewer.rate_homework(student1,'python',3)
reviewer.rate_homework(student1,'c#',5)

student.give_estimation(lecturer,'python',10)
student1.give_estimation(lecturer,'c#',9)
student1.give_estimation(lecturer1,'python',8)
student.give_estimation(lecturer1,'c#',10)

student.finish_course('python')

print( student.courses_in_progress)
print( student.finished_courses)
print( student.courses_estimations)
print( lecturer.estimations_for_lectures)

print(lecturer)
print(lecturer1)
print(reviewer)
print(student)

print(lecturer<lecturer1)
print(lecturer>lecturer1)
print(lecturer==lecturer1)

print(student<student1)
print(student>student1)
print(student==student1)

print( total_avg( [student,student1], 'c#') )
print( total_avg( [student,student1], 'python') )

print( total_avg( [lecturer,lecturer1], 'c#') )
print( total_avg( [lecturer,lecturer1], 'python') )