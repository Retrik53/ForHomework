class Teacher:
    all_teachers = []

    def __init__(self, name, education, experience):
        self._name = name
        self._education = education
        self._experience = experience

        Teacher.all_teachers.append(self)

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

    def fire_teacher(self):
        try:
            for i, teacher in enumerate(Teacher.all_teachers):
                if teacher is self:
                    del Teacher.all_teachers[i]
                    break
            print(f"Учитель {self.name} уволен.")
        except ValueError as e:
            print(f"Произошла ошибка при увольнении учителя: {e}")

    def __repr__(self):
        return f"{self.name!r}"


class DisciplineTeacher(Teacher):
    def __init__(self, name, education, experience, discipline, job_title):
        super().__init__(name, education, experience)
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

    def __repr__(self):
        return f"{self.name!r}, {self.discipline!r}"


first_teacher = DisciplineTeacher(name="Анна Иванова", education="МГУ", experience=10, discipline="Физика", job_title="Старший преподаватель")
second_teacher = DisciplineTeacher(name="Алексей Смирнов", education="СПбГУ", experience=8, discipline="Математика", job_title="Преподаватель")
third_teacher = DisciplineTeacher("Максим Гавриленко", "ЗабГУ", 7, "Русский язык", "Запасной преподаватель")

print(Teacher.all_teachers)

first_teacher.fire_teacher()
third_teacher.fire_teacher()

print(Teacher.all_teachers)