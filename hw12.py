# Создайте класс студента.
# ○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и
# наличие только букв.
# ○ Названия предметов должны загружаться из файла CSV при создании
# экземпляра. Другие предметы в экземпляре недопустимы.
# ○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты
# тестов (от 0 до 100).
# ○ Также экземпляр должен сообщать средний балл по тестам для каждого
# предмета и по оценкам всех предметов вместе взятых.

import csv
from statistics import mean


class Name:
    def __set_name__(self, owner, name):
        self.private_name = f'_{name}'

    def __get__(self, instance, owner):
        return getattr(instance, self.private_name)

    def __set__(self, instance, value):
        if not value.isalpha():
            raise ValueError('Имя должно состоять из букв')
        if not value.istitle():
            raise ValueError('Имя должно начинаться с заглавной буквы')
        setattr(instance, self.private_name, value)


class Value:

    def __init__(self, min_value: int = None, max_value: int = None):
        self._min_value = min_value
        self._max_value = max_value


class Student:
    _first_name = Name()
    _last_name = Name()
    _grade = Value(2, 5)
    _test = Value(0, 100)

    def __init__(self, first_name: str, second_name: str, last_name: str, grade: dict[str: tuple], test: dict[str: tuple]):
        self._first_name = first_name
        self.second_name = second_name
        self._last_name = last_name
        self._grades = grade
        self._tests = test

    def __str__(self):
        grades = ' '.join(f'{key}: {value}' for key, value in self._grades.items())
        tests = ' '.join(f'{key}: {value}' for key, value in self._tests.items())
        test_result = '\n'.join(f'{key}: {value}' for key, value in self.arithmetic_tests().items())
        grades_result = '\n'.join(f'{key}: {value}' for key, value in self.arithmetic_grades().items())
        return f'ФИО студента: {self._last_name} {self._first_name} {self.second_name} \nОценки:\n{grades}, \nБаллы за тесты:\n{tests}, \nСредний балл за тесты:\n{test_result}, \nСредняя оценка по предметам:\n{grades_result}'

    def db(self):
        data = {}
        with open('items.csv', 'r', encoding='utf-8') as f:
            csv_reader = csv.reader(f)
            for _ in csv_reader:
                return data

    def arithmetic_grades(self):
        result = {}
        for key, value in self._grades.items():
            result[key] = round(mean(value), 2)
        return result

    def arithmetic_tests(self):
        result = {}
        for key, value in self._tests.items():
            result[key] = round(mean(value), 2)
        return result


if __name__ == '__main__':
    student1 = Student('Иван', 'Иванович', 'Иванов', {'История': (5, 5, 5), 'Испанский': (4, 5, 5)}, {'Литература': (90, 85, 88), 'Английский': (90, 86, 80) })
    print(student1)
