import csv

# Створюємо CSV файл з даними студентів
user_data = [
    ["Ім'я", "Вік", "Оцінка"],
    ["Петро", 21, 90],
    ["Марина", 22, 85],
    ["Андрій", 20, 88]
]

# Відкриваємо файл students.csv для запису (режим 'w') та записуємо дані
with open("students.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(user_data)

print("Файл створено")


def read_and_calculate_average(filename):
    """
    Функція читає дані з CSV-файлу, обчислює і виводить середню оцінку студентів.
    """
    total_score = 0
    student_count = 0

    # Відкриваємо файл для читання (режим 'r')
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            score = int(row[2])
            total_score += score
            student_count += 1

    # Обчислення середньої оцінки
    if student_count > 0:
        average_score = total_score / student_count
        print(f'Середня оцінка студентів: {average_score:.2f}')
    else:
        print("Немає даних про студентів.")


def add_student(filename, student_data):
    """
    Функція додає нового студента до CSV-файлу.
    """
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(student_data)

    print(f"Додано студента: {student_data[0]}")


# Читаємо дані та виводимо середню оцінку
read_and_calculate_average('students.csv')

# Додаємо нового студента
new_student = ['Паша', 20, 60]
add_student('students.csv', new_student)

# Після додавання перевіряємо середню оцінку знову
read_and_calculate_average('students.csv')
