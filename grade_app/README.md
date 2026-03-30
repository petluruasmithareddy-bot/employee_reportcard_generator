#  Student Grade Calculator (Streamlit Dashboard)

An interactive web-based Student Grade Calculator built using Python and Streamlit. This application allows users to input marks for multiple subjects and instantly calculates total marks, average, and grade.



##  Project Description

This project is an upgraded version of a basic console-based grade calculator. It now includes a **Streamlit-based user interface (UI)** that provides a simple and interactive dashboard experience.

Users can:

* Enter the number of subjects
* Input marks for each subject
* View calculated total, average, and grade

##  Features

*  Dynamic input fields based on number of subjects
*  Automatic total marks calculation
*  Average calculation with formatted output
*  Grade assignment based on performance
*  Interactive dashboard using Streamlit


## Technologies Used

* Python 3
* Streamlit (for UI)
* No external libraries required


##  Sample Output

 Student Grade Calculator

Enter number of subjects: 3

Subject 1: 80
Subject 2: 90
Subject 3: 70

 Result
Total Marks: 240
Average: 80.00
Grade: B


##  Key Concepts Used

###  Functions

* `calculate_total()` → Calculates total marks
* `calculate_avg()` → Computes average
* `assign_grade()` → Assigns grade

###  Data Structures

* List → Stores subject marks

###  Streamlit UI

* `st.title()` → Title display
* `st.number_input()` → User input
* `st.button()` → Action trigger
* `st.success()` → Display results

##  Project Structure

* `app.py` → Main Streamlit application
* Functions → Core logic for calculations
* UI layer → Handles user interaction

##  Future Improvements

* Add grade visualization (charts) 
* Support multiple students
* Export results to file (CSV/PDF)
* Add performance analytics

## Contributing

Contributions are welcome! Feel free to fork and improve the project.

##  License

This project is open-source and free to use.


## Acknowledgements

This project is created as part of learning Python, functions, data structures, and building interactive applications using Streamlit.
