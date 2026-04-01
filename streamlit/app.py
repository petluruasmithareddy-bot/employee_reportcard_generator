import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Import from logic file
from stu_grade_app import calculate_total, calculate_avg, assign_grade, save_to_file


st.title("🎓 Student Grade Calculator Dashboard")

name = st.text_input("Enter Student Name")

n = st.number_input("Enter number of subjects", min_value=1, step=1)

marks = []
subjects = []

for i in range(n):
    subject = st.text_input(f"Enter name of subject {i+1}", key=f"sub{i}")

    mark = st.number_input(
        f"Enter marks for {subject if subject else f'Subject {i+1}'}",
        min_value=0,
        max_value=100,
        key=f"mark{i}"
    )

    subjects.append(subject if subject else f"Sub {i+1}")
    marks.append(mark)


if st.button("Calculate Result"):

    total = calculate_total(marks)
    average = calculate_avg(total, n)
    grade = assign_grade(average)

    st.subheader("📊 Result")
    st.success(f"Name: {name}")
    st.success(f"Total Marks: {total}")
    st.success(f"Average: {average:.2f}")
    st.success(f"Grade: {grade}")

    # Terminal output
    print("\n📊 Result (Terminal Output)")
    print(f"Name: {name}")
    for sub, mark in zip(subjects, marks):
        print(f"{sub}: {mark}")
    print(f"Total: {total}")
    print(f"Average: {average:}")
    print(f"Grade: {grade}")

    # Save to file
    save_to_file(name, subjects, marks, total, average, grade)
    st.info("💾 Result saved to student_results.txt")

    # Bar Chart
    df = pd.DataFrame({
        "Subjects": subjects,
        "Marks": marks
    })

    st.bar_chart(df.set_index("Subjects"))

    # Pie Chart
    fig, ax = plt.subplots()
    ax.pie(marks, labels=subjects, autopct='%1.1f%%')

    st.pyplot(fig)