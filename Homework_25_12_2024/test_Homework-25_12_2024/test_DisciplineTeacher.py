import pytest
from Homework_25_12_2024.Homework_25_12_2024 import DisciplineTeacher


@pytest.fixture
def create_discipline_teacher():
    """Создание экземпляра класса DisciplineTeacher."""
    return DisciplineTeacher(
        name='Марина Сидорова',
        education='МФТИ',
        experience=15,
        discipline='Химия',
        job_title='Доцент'
    )


def test_init(create_discipline_teacher):
    """Тестирование инициализации объекта DisciplineTeacher."""
    assert create_discipline_teacher.name == 'Марина Сидорова'
    assert create_discipline_teacher.education == 'МФТИ'
    assert create_discipline_teacher.experience == 15
    assert create_discipline_teacher.discipline == 'Химия'
    assert create_discipline_teacher.job_title == 'Доцент'


def test_get_teacher_data(create_discipline_teacher):
    """Тестирование метода get_teacher_data()."""
    expected_result = "Марина Сидорова, Доцент, предмет Химия, образование МФТИ, опыт работы 15 лет."
    assert create_discipline_teacher.get_teacher_data() == expected_result


def test_add_mark(create_discipline_teacher):
    """Тестирование метода add_mark()."""
    result = create_discipline_teacher.add_mark('Студент В', 3)
    assert result == 'Марина Сидорова поставил оценку 3 студенту Студент В. Предмет: Химия.'


def test_remove_mark(create_discipline_teacher):
    """Тестирование метода remove_mark()."""
    result = create_discipline_teacher.remove_mark('Студент Г', 2)
    assert result == 'Марина Сидорова удалил оценку 2 у студента Студент Г. Предмет: Химия.'


def test_give_a_consultation(create_discipline_teacher):
    """Тестирование метода give_a_consultation()."""
    result = create_discipline_teacher.give_a_consultation(202)
    assert result == 'Марина Сидорова провел консультацию в классе 202, по предмету: Химия, как Доцент.'