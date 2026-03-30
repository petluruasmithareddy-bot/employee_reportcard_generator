import streamlit as st


# Functions
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


# UI
st.title(" Student Grade Calculator")

# Input: number of subjects
n = st.number_input("Enter number of subjects", min_value=1, step=1)

marks = []

# Dynamic input fields
for i in range(n):
    mark = st.number_input(f"Enter marks for subject {i+1}", min_value=0.0, max_value=100.0)
    marks.append(mark)

# Button
if st.button("Calculate Result"):
    total = calculate_total(marks)
    average = calculate_avg(total, n)
    grade = assign_grade(average)

    st.subheader(" Result")
    st.success(f"Total Marks: {total}")
    st.success(f"Average: {average:.2f}")
    st.success(f"Grade: {grade}")