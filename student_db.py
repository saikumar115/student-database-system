
import mysql.connector

# Connect to MySQL (adjust credentials as needed)
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='your_password',
    database='student_db'
)
cursor = conn.cursor()

def create_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            age INT,
            course VARCHAR(255)
        )
    """)
    print("Table created successfully.")

def add_student(name, age, course):
    cursor.execute("INSERT INTO students (name, age, course) VALUES (%s, %s, %s)", (name, age, course))
    conn.commit()
    print("Student added successfully.")

def get_students():
    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        print(row)

def update_student(student_id, name, age, course):
    cursor.execute("UPDATE students SET name=%s, age=%s, course=%s WHERE id=%s", (name, age, course, student_id))
    conn.commit()
    print("Student updated successfully.")

def delete_student(student_id):
    cursor.execute("DELETE FROM students WHERE id=%s", (student_id,))
    conn.commit()
    print("Student deleted successfully.")

# Example usage
create_table()
add_student('Sai Kumar', 22, 'MCA')
get_students()
# update_student(1, 'Sai Kumar', 23, 'MCA')
# delete_student(1)

cursor.close()
conn.close()
