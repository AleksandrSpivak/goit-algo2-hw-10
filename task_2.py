# Визначення класу Teacher
class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = can_teach_subjects
        self.assigned_subjects = set()


def create_schedule(subjects, teachers):
    schedule = []
    uncovered_subjects = subjects.copy()

    while uncovered_subjects:
        # Знаходимо викладача, який покриває найбільше ще не призначених предметів
        best_teacher = max(
            teachers,
            key=lambda teacher: (
                len(teacher.can_teach_subjects & uncovered_subjects),
                -teacher.age,
            ),
            default=None,
        )

        if not best_teacher or not (
            best_teacher.can_teach_subjects & uncovered_subjects
        ):
            print("Неможливо покрити всі предмети наявними викладачами.")
            return None

        # Призначаємо викладачу предмети, які ще не були покриті
        assigned = best_teacher.can_teach_subjects & uncovered_subjects
        best_teacher.assigned_subjects = assigned
        schedule.append(best_teacher)

        # Видаляємо покриті предмети
        uncovered_subjects -= assigned

    return schedule


if __name__ == "__main__":
    # Множина предметів
    subjects = {"Математика", "Фізика", "Хімія", "Інформатика", "Біологія"}

    # Створення списку викладачів
    teachers = [
        Teacher(
            "Олександр",
            "Іваненко",
            45,
            "o.ivanenko@example.com",
            {"Математика", "Фізика"},
        ),
        Teacher("Марія", "Петренко", 38, "m.petrenko@example.com", {"Хімія"}),
        Teacher(
            "Сергій",
            "Коваленко",
            50,
            "s.kovalenko@example.com",
            {"Інформатика", "Математика"},
        ),
        Teacher(
            "Наталія", "Шевченко", 29, "n.shevchenko@example.com", {"Біологія", "Хімія"}
        ),
        Teacher(
            "Дмитро",
            "Бондаренко",
            35,
            "d.bondarenko@example.com",
            {"Фізика", "Інформатика"},
        ),
        Teacher("Олена", "Гриценко", 42, "o.grytsenko@example.com", {"Біологія"}),
    ]

    # Виклик функції створення розкладу
    schedule = create_schedule(subjects, teachers)

    # Виведення розкладу
    if schedule:
        print("Розклад занять:")
        for teacher in schedule:
            print(
                f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}"
            )
            print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}")
