from db import connect_db

def add_student():
    conn = connect_db()
    cursor = conn.cursor()

    name = input("Enter name: ")
    age = int(input("Enter age: "))
    marks = float(input("Enter marks: "))

    query = "INSERT INTO students (name, age, marks) VALUES (%s, %s, %s)"
    values = (name, age, marks)

    cursor.execute(query, values)
    conn.commit()

    print("Student added successfully!")

    cursor.close()
    conn.close()


def view_students():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    results = cursor.fetchall()

    print("\n--- Student Records ---")
    for row in results:
        print(row)

    cursor.close()
    conn.close()


def delete_student():
    conn = connect_db()
    cursor = conn.cursor()

    student_id = int(input("Enter student ID to delete: "))

    query = "DELETE FROM students WHERE id = %s"
    cursor.execute(query, (student_id,))
    conn.commit()

    print("Student deleted successfully!")

    cursor.close()
    conn.close()

def update_student():
    conn = connect_db()
    cursor = conn.cursor()

    student_id = int(input("Enter student ID to update: "))
    new_marks = float(input("Enter new marks: "))

    query = "UPDATE students SET marks = %s WHERE id = %s"
    cursor.execute(query, (new_marks, student_id))
    conn.commit()

    print("Student updated successfully!")

    cursor.close()
    conn.close()

def search_student():
    conn = connect_db()
    cursor = conn.cursor()

    name = input("Enter student name to search: ")

    query = "SELECT * FROM students WHERE name LIKE %s"
    cursor.execute(query, ('%' + name + '%',))

    results = cursor.fetchall()

    if results:
        for row in results:
            print(row)
    else:
        print("No student found")

    cursor.close()
    conn.close()

def show_topper():
    conn = connect_db()
    cursor = conn.cursor()

    query = "SELECT * FROM students ORDER BY marks DESC LIMIT 1"
    cursor.execute(query)

    result = cursor.fetchone()

    if result:
        print("Topper:", result)
    else:
        print("No data available")

    cursor.close()
    conn.close()

def average_marks():
    conn = connect_db()
    cursor = conn.cursor()

    query = "SELECT AVG(marks) FROM students"
    cursor.execute(query)

    result = cursor.fetchone()

    print("Average Marks:", result[0])

    cursor.close()
    conn.close()


def menu():
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Update Student")
    print("5. Search Student")
    print("6. Show Topper")
    print("7. Average Marks")
    print("8. Exit")


def main():
    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            search_student()
        elif choice == "6":
            show_topper()
        elif choice == "7":
            average_marks()
        elif choice == "8":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()

