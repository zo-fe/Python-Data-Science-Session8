import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Dataset creation
data = {
    'Student Name': ['Amelie', 'Edgar', 'Jordi', 'Marçal', 'Pep', 'Jaume', 'Marco',
                     'Ludmila', 'Bastian', 'Marc', 'Gerardo', 'Javier', 'Frank', 'Julia'],
    'Course': ['Artificial Intelligence', 'Python for Data Science', 'Cloud Computing', 'Computer Vision',
               'Artificial Intelligence', 'Python for Data Science', 'Cloud Computing', 'Computer Vision',
               'Artificial Intelligence', 'Python for Data Science', 'Cloud Computing', 'Computer Vision',
               'Artificial Intelligence', 'Python for Data Science'],
    'Grade': [85, 92, 78, 88, 91, 84, 73, 95, 90, 80, 85, 87, 89, 92],
    'Gender': ['Female', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Female', 'Male', 'Male', 'Male', 'Male', 'Male', 'Female'],
    'Study Time': [15, 20, 10, 8, 18, 14, 11, 16, 19, 13, 16, 12, 17, 15],
    'Age': [22, 21, 23, 22, 20, 24, 22, 21, 23, 21, 22, 22, 21, 20]
}

df = pd.DataFrame(data)

# 1. Lineplot for Study Time by Student Name
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='Student Name', y='Study Time', marker='o')
plt.title('Study Time by Student Name', fontsize=14)
plt.xlabel('Student Name', fontsize=12)
plt.ylabel('Study Time (hours)', fontsize=12)
plt.xticks(rotation=45)
plt.show()

# Identifying the student with the highest study time
highest_study_time_student = df.loc[df['Study Time'].idxmax(), 'Student Name']
print(f"The student with the highest study time is: {highest_study_time_student}")

# 2. Histogram of Grade
plt.figure(figsize=(8, 6))
sns.histplot(data=df, x='Grade', bins=5, kde=True)
plt.title('Grade Distribution', fontsize=14)
plt.xlabel('Grade', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.show()

# 3. ECDF plot for Grade
plt.figure(figsize=(8, 6))
sns.ecdfplot(data=df, x='Grade')
plt.title('ECDF of Grade', fontsize=14)
plt.xlabel('Grade', fontsize=12)
plt.ylabel('ECDF', fontsize=12)
plt.show()

# Percentage of students scoring less than 85
students_below_85 = (df['Grade'] < 85).sum() / len(df) * 100
print(f"Percentage of students scoring less than 85: {students_below_85:.2f}%")

# 4. Stripplot for Grade distribution by Course
plt.figure(figsize=(10, 6))
sns.stripplot(data=df, x='Course', y='Grade', jitter=True)
plt.title('Grade Distribution by Course', fontsize=14)
plt.xlabel('Course', fontsize=12)
plt.ylabel('Grade', fontsize=12)
plt.xticks(rotation=45)
plt.show()

# 5. Swarmplot for Study Time by Gender
plt.figure(figsize=(8, 6))
sns.swarmplot(data=df, x='Gender', y='Study Time')
plt.title('Study Time by Gender', fontsize=14)
plt.xlabel('Gender', fontsize=12)
plt.ylabel('Study Time (hours)', fontsize=12)
plt.show()

# Average study time by gender
avg_study_time_gender = df.groupby('Gender')['Study Time'].mean()
print(avg_study_time_gender)

# 6. Pointplot for Average Grade by Course
plt.figure(figsize=(10, 6))
sns.pointplot(data=df, x='Course', y='Grade', ci=None)
plt.title('Average Grade by Course', fontsize=14)
plt.xlabel('Course', fontsize=12)
plt.ylabel('Average Grade', fontsize=12)
plt.xticks(rotation=45)
plt.show()

# Identifying the course with the highest average grade
highest_avg_grade_course = df.groupby('Course')['Grade'].mean().idxmax()
print(f"The course with the highest average grade is: {highest_avg_grade_course}")