class Teacher:
    def __init__(self, name, education, experience):
        self._name = name
        self._education = education
        self._experience = experience

    @property
    def name(self):
        return self._name

    @property
    def education(self):
        return self._education

    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, new_experience):
        if isinstance(new_experience, int) and new_experience > 0:
            self._experience = new_experience
        else:
            raise ValueError("Опыт должен быть положительным целым числом")

    def get_teacher_data(self):
        return f"{self.name}, образование {self.education}, опыт работы {self.experience} года."

    def add_mark(self, student_name, mark):
        return f"{self.name} поставил оценку {mark} студенту {student_name}."

    def remove_mark(self, student_name, mark):
        return f"{self.name} удалил оценку {mark} у студента {student_name}."

    def give_a_consultation(self, classroom):
        return f"{self.name} провел консультацию в классе {classroom}."

teacher = Teacher("Николай Захаров", "БГПУ", 4)
print(teacher.get_teacher_data())
print(teacher.add_mark("Петр Сидоров", 5))
print(teacher.remove_mark("Петр Сидоров", 4))
print(teacher.give_a_consultation("11А"))
print(f"Задача 1^\n===========================\nЗадача 2")

class DisciplineTeacher:
    def __init__(self, name, education, experience, discipline, job_title):
        self.name = name
        self.education = education
        self.experience = experience
        self.discipline = discipline
        self.job_title = job_title

    def get_teacher_data(self):
        return f"{self.name}, {self.job_title}, предмет {self.discipline}, образование {self.education}, опыт работы {self.experience} лет."

    def add_mark(self, student_name, mark):
        return f"{self.name} поставил оценку {mark} студенту {student_name}. Предмет: {self.discipline}."

    def remove_mark(self, student_name, mark):
        return f"{self.name} удалил оценку {mark} у студента {student_name}. Предмет: {self.discipline}."

    def give_a_consultation(self, classroom):
        return f"{self.name} провел консультацию в классе {classroom}, по предмету: {self.discipline}, как {self.job_title}."


disciplined_teacher = DisciplineTeacher(
    name="Иван Петров",
    education="БГПУ",
    experience=4,
    discipline="Химия",
    job_title="Учитель"
)
print(f"{disciplined_teacher.get_teacher_data()}")

print(f"{disciplined_teacher.add_mark(student_name="Николай Иванов", mark=11)}")

print(f"{disciplined_teacher.remove_mark(student_name="Николай Иванов", mark=12)}")

print(f"{disciplined_teacher.give_a_consultation(classroom="11А")}")

print("===============================")
Name = input("Введите ваше имя:")
Education = input("Введите в каком заведении вы обучались:")
Experience = int(input("Введите ваш опыт работы в годах:"))
Discipline = input("Введите какой предмет вы ведете:")
Job_Title = input("Введите вашу должность:")
discipline_teacher = DisciplineTeacher(
    name=Name,
    education=Education,
    experience=Experience,
    discipline=Discipline,
    job_title=Job_Title
)

Student = input("Введите имя студента")
Mark_add = int(input("Введите какую оценку вы хотите поставить"))

print(f"{discipline_teacher.add_mark(student_name=Student, mark=Mark_add)}")

Student_2 = input("Введите имя студента")
Mark_delete = int(input("Введите какую оценку вы хотите удалить"))

print(f"{discipline_teacher.remove_mark(student_name=Student_2, mark=Mark_delete)}")

Classroom = input("Введите в каком классе вы желаете провести консультацию")

print(f"{discipline_teacher.give_a_consultation(classroom=Classroom)}")