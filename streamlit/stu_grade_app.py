def calculate_total(marks):
    return sum(marks)


def calculate_avg(total, no_of_sub):
    return total / no_of_sub


def assign_grade(average):
    if average >= 90:
        return "Grade A"
    elif average >= 80:
        return "Grade B"
    elif average >= 75:
        return "Grade C"
    elif average >= 60:
        return "Improvement"
    else:
        return "Fail"


def save_to_file(name, subjects, marks, total, average, grade):
    with open("student_results.txt", "a") as file:
        file.write(f"Name: {name}\n")
        for sub, mark in zip(subjects, marks):
            file.write(f"{sub}: {mark}\n")
        file.write(f"Total: {total}\n")
        file.write(f"Average: {average:}\n")
        file.write(f"Grade: {grade}\n")
        file.write("-" * 30 + "\n")