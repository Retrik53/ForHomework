import pytest
from Homework_25_12_2024.Homework_25_12_2024 import Teacher


@pytest.fixture
def create_teacher():
    """Создание экземпляра класса Teacher."""
    return Teacher('Иван Петров', 'МГТУ', 12)


def test_init(create_teacher):
    """Тестирование инициализации объекта Teacher."""
    assert create_teacher.name == 'Иван Петров'
    assert create_teacher.education == 'МГТУ'
    assert create_teacher.experience == 12


def test_get_teacher_data(create_teacher):
    """Тестирование метода get_teacher_data()."""
    expected_result = "Иван Петров, образование МГТУ, опыт работы 12 года."
    assert create_teacher.get_teacher_data() == expected_result


def test_add_mark(create_teacher):
    """Тестирование метода add_mark()."""
    result = create_teacher.add_mark('Студент А', 5)
    assert result == 'Иван Петров поставил оценку 5 студенту Студент А.'


def test_remove_mark(create_teacher):
    """Тестирование метода remove_mark()."""
    result = create_teacher.remove_mark('Студент Б', 4)
    assert result == 'Иван Петров удалил оценку 4 у студента Студент Б.'


def test_give_a_consultation(create_teacher):
    """Тестирование метода give_a_consultation()."""
    result = create_teacher.give_a_consultation(101)
    assert result == 'Иван Петров провел консультацию в классе 101.'


def test_fire_teacher(create_teacher):
    """Тестирование метода fire_teacher()."""
    Teacher.all_teachers.append(create_teacher)
    assert len(Teacher.all_teachers) == 1

    create_teacher.fire_teacher()
    assert len(Teacher.all_teachers) == 0

    create_teacher.fire_teacher()
    assert len(Teacher.all_teachers) == 0


def test_experience_setter_invalid_value(create_teacher):
    """Проверка set-метода experience на недопустимые значения."""
    with pytest.raises(ValueError):
        create_teacher.experience = -1