import matplotlib.pyplot as plt
students = ['S1', 'S2', 'S3', 'S4', 'S5']
subjects = ['Digital Electronics', 'Probability', 'Python', 'Full Stack', 'IELTS', 'Data Structure']
marks = [
    [85, 70, 90, 60, 75], # Digital Electronics
    [78, 85, 80, 70, 88], # Probability
    [95, 90, 92, 88, 98], # Python
    [80, 75, 85, 90, 82], # Full Stack
    [7, 8, 6, 7.5, 9],    # IELTS (Reading)
    [88, 72, 95, 80, 85]  # Data Structure
]
plt.figure(figsize=(12, 8))
plt.suptitle("Student Marks Analysis", fontsize=16)
for i in range(6):
    plt.subplot(2, 3, i + 1)   
    plt.bar(students, marks[i], color='skyblue')
    plt.title(subjects[i])  
    plt.ylim(0, 100)              
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()