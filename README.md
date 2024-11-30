# Python-Data-Science-Session8

This project contains solutions to a set of visualization exercises using Seaborn and Matplotlib libraries in Python. The exercises involve analyzing a dataset of students, their courses, grades, study times, and other attributes.

## Dataset Description

The dataset contains the following columns:
- **Student Name**: Name of the student.
- **Course**: The course taken by the student.
- **Grade**: Grade received by the student.
- **Gender**: Gender of the student.
- **Study Time**: Number of hours the student studied.
- **Age**: Age of the student.

## Exercises and Visualizations

### 1. Lineplot
- **Objective**: Show how **Study Time** varies by **Student Name**.
- **Key Finding**: Identify the student with the highest study time.

### 2. Histogram
- **Objective**: Plot a histogram of **Grade** to find the grade range with the highest frequency.

### 3. ECDF Plot
- **Objective**: Create an ECDF plot for **Grade** to determine the percentage of students scoring less than 85.

### 4. Stripplot
- **Objective**: Show the **Grade** distribution for each **Course** to identify the course with the most spread in grades.

### 5. Swarmplot
- **Objective**: Visualize the relationship between **Gender** and **Study Time** to determine which gender has a higher average study time.

### 6. Pointplot
- **Objective**: Show the average **Grade** for each **Course** and identify the course with the highest average grade.

## Requirements

To run this project, you need the following:
- Python 3.x
- Required libraries: `pandas`, `seaborn`, `matplotlib`

Install the required libraries using pip:
pip install pandas seaborn matplotlib

## Usage

1. Clone the repository:
   git clone https://github.com/zo-fe/Python-Data-Science-Session8.git
2. Navigate to the project directory:
   cd Python-Data-Science-Session8
3. Run the script:
   python exercise_plotting_seaborn.py
