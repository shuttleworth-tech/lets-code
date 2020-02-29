from lets_code.tools import read_yaml


def get_students():
    students: dict
    students_file_name: str = "resources/students.yaml"
    students = read_yaml()

    return students