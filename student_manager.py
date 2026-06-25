import os

# Path to file
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'resources', 'studentMarks.txt')

# Load student data
def load_students(filename):
    students = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines[1:]:
                parts = line.strip().split(',')
                if len(parts) == 6:
                    code = parts[0].strip()
                    name = parts[1].strip()
                    coursework = list(map(int, parts[2:5]))
                    exam = int(parts[5].strip())
                    students.append({'code': code, 'name': name, 'coursework': coursework, 'exam': exam})
    except FileNotFoundError:
        print("Error: studentMarks.txt not found!")
    return students

# Save students to file
def save_students(filename, students):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(f"{len(students)}\n")
        for s in students:
            line = f"{s['code']}, {s['name']}, {s['coursework'][0]},{s['coursework'][1]},{s['coursework'][2]},{s['exam']}\n"
            file.write(line)

# Calculate total, percentage, grade
def calculate_results(student):
    total_coursework = sum(student['coursework'])
    exam_mark = student['exam']
    overall_percentage = ((total_coursework + exam_mark)/160)*100
    grade = 'F'
    if overall_percentage >= 70: grade = 'A'
    elif overall_percentage >= 60: grade = 'B'
    elif overall_percentage >= 50: grade = 'C'
    elif overall_percentage >= 40: grade = 'D'
    return total_coursework, overall_percentage, grade

# Display a student
def display_student(student):
    total_coursework, overall_percentage, grade = calculate_results(student)
    print(f"Name: {student['name']}")
    print(f"Student Number: {student['code']}")
    print(f"Total Coursework Mark: {total_coursework}")
    print(f"Exam Mark: {student['exam']}")
    print(f"Overall Percentage: {overall_percentage:.2f}%")
    print(f"Grade: {grade}")
    print("-"*40)

# View all students
def view_all_students(students):
    total_percentage = 0
    for s in students:
        display_student(s)
        _, overall_percentage, _ = calculate_results(s)
        total_percentage += overall_percentage
    print(f"Total Students: {len(students)}")
    if students:
        print(f"Average Percentage: {total_percentage/len(students):.2f}%")
    print("="*50)

# View individual student
def view_individual_student(students):
    choice = input("Enter student number or name: ").strip()
    found = None
    for s in students:
        if s['code'] == choice or s['name'].lower() == choice.lower():
            found = s
            break
    if found:
        display_student(found)
    else:
        print("Student not found.")

# Show student with highest/lowest total
def show_extreme_student(students, highest=True):
    if not students:
        print("No students available.")
        return
    key_func = lambda s: sum(s['coursework']) + s['exam']
    s = max(students, key=key_func) if highest else min(students, key=key_func)
    display_student(s)

# Sort students
def sort_students(students):
    order = input("Sort by total score ascending or descending? (asc/desc): ").strip().lower()
    reverse = True if order == 'desc' else False
    students.sort(key=lambda s: sum(s['coursework'])+s['exam'], reverse=reverse)
    print(f"Students sorted {order}.")
    view_all_students(students)

# Add student
def add_student(students):
    code = input("Enter student code: ").strip()
    if any(s['code']==code for s in students):
        print("Student code already exists.")
        return
    name = input("Enter student name: ").strip()
    coursework = []
    for i in range(1,4):
        mark = int(input(f"Enter coursework {i} mark (0-20): "))
        coursework.append(mark)
    exam = int(input("Enter exam mark (0-100): "))
    students.append({'code':code,'name':name,'coursework':coursework,'exam':exam})
    save_students(file_path, students)
    print("Student added successfully.")

# Delete student
def delete_student(students):
    choice = input("Enter student code or name to delete: ").strip()
    for i,s in enumerate(students):
        if s['code']==choice or s['name'].lower()==choice.lower():
            del students[i]
            save_students(file_path, students)
            print("Student deleted.")
            return
    print("Student not found.")

# Update student
def update_student(students):
    choice = input("Enter student code or name to update: ").strip()
    found = None
    for s in students:
        if s['code']==choice or s['name'].lower()==choice.lower():
            found = s
            break
    if not found:
        print("Student not found.")
        return
    print("Select field to update:")
    print("1. Name\n2. Coursework 1\n3. Coursework 2\n4. Coursework 3\n5. Exam")
    field = input("Enter choice: ").strip()
    if field=='1':
        found['name'] = input("Enter new name: ").strip()
    elif field in ['2','3','4']:
        idx = int(field)-2
        found['coursework'][idx] = int(input(f"Enter new mark for coursework {idx+1}: "))
    elif field=='5':
        found['exam'] = int(input("Enter new exam mark: "))
    else:
        print("Invalid choice.")
        return
    save_students(file_path, students)
    print("Student updated successfully.")

# Main menu
def main():
    students = load_students(file_path)
    if not students:
        return
    while True:
        print("\nStudent Manager Menu")
        print("1. View all student records")
        print("2. View individual student record")
        print("3. Show student with highest total score")
        print("4. Show student with lowest total score")
        print("5. Sort student records")
        print("6. Add a student record")
        print("7. Delete a student record")
        print("8. Update a student record")
        print("9. Quit")
        choice = input("Enter your choice: ").strip()
        if choice=='1': view_all_students(students)
        elif choice=='2': view_individual_student(students)
        elif choice=='3': show_extreme_student(students, True)
        elif choice=='4': show_extreme_student(students, False)
        elif choice=='5': sort_students(students)
        elif choice=='6': add_student(students)
        elif choice=='7': delete_student(students)
        elif choice=='8': update_student(students)
        elif choice=='9': break
        else: print("Invalid choice.")

if __name__=="__main__":
    main()
