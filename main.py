import sqlite3
import tkinter as tk
from tkinter import messagebox

# Function to create student database
def create_db():
    conn = sqlite3.connect('student.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS student 
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    birth_date TEXT NOT NULL,
                    grade TEXT NOT NULL,
                    reg_no TEXT NOT NULL,
                    email_id TEXT NOT NULL,
                    gender TEXT NOT NULL,
                    father_name TEXT NOT NULL,
                    mother_name TEXT NOT NULL,
                    address TEXT NOT NULL,
                    phone_no TEXT NOT NULL,
                    religion TEXT NOT NULL)''')
    conn.commit()
    conn.close()

# Function to create passwords database
def passworddata():
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS passwords
                   (username TEXT NOT NULL,
                   password TEXT NOT NULL)''')
    conn.commit()
    conn.close()

# Function to initialize default password if passwords database is empty
def initialize_password():
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM passwords")
    count = cursor.fetchone()[0]
    if count == 0:
        cursor.execute("INSERT INTO passwords(username, password) VALUES ('admin', 'admin')")
        conn.commit()
    conn.close()

# Function to update password
def update_password():
    def save_new_password():
        username = label_entry.get()
        password = label1_entry.get()

        conn = sqlite3.connect('passwords.db')
        cursor = conn.cursor()
        cursor.execute("REPLACE INTO passwords(username,password) VALUES (?,?)",(username,password))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Password updated successfully")
        root.destroy()

    passworddata()

    root = tk.Tk()
    root.title("Update Password")
    root.geometry("300x200")
    nfont = ("Arial", 20)

    label = tk.Label(root, text="Enter username")
    label.grid(row=1, column=0, padx=10, pady=5)
    label_entry = tk.Entry(root, font=nfont)
    label_entry.grid(row=1, column=1, padx=10, pady=5)

    label1 = tk.Label(root, text="Enter password")
    label1.grid(row=2, column=0, padx=10, pady=5)
    label1_entry = tk.Entry(root, font=nfont, show="*")
    label1_entry.grid(row=2, column=1, padx=10, pady=5)

    save_button = tk.Button(root, text="Save", command=save_new_password)
    save_button.grid(row=3, column=1, pady=10)

    root.mainloop()

# Function to handle login
def login():
    def check_credentials():
        username = user_entry.get()
        password = pass_entry.get()

        conn = sqlite3.connect('passwords.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM passwords WHERE username=? AND password=?", (username, password))
        result = cursor.fetchone()
        conn.close()

        if result:
            login_window.destroy()
            main_window()
        else:
            messagebox.showerror("Error", "Invalid username or password")

    login_window = tk.Tk()
    login_window.title("Login")
    login_window.geometry("300x200")
    nfont = ("Arial", 20)

    user_label = tk.Label(login_window, text="Username")
    user_label.grid(row=0, column=0, padx=10, pady=5)
    user_entry = tk.Entry(login_window, font=nfont)
    user_entry.grid(row=0, column=1, padx=10, pady=5)

    pass_label = tk.Label(login_window, text="Password")
    pass_label.grid(row=1, column=0, padx=10, pady=5)
    pass_entry = tk.Entry(login_window, font=nfont, show="*")
    pass_entry.grid(row=1, column=1, padx=10, pady=5)

    login_button = tk.Button(login_window, text="Login", command=check_credentials)
    login_button.grid(row=2, column=1, pady=10)

    login_window.mainloop()

# Function to display main window for managing student information
def main_window():
    root = tk.Tk()
    root.title("Student Information Management System")
    root.geometry('800x600')
    font = ("Arial", 18)

    tk.Label(root, text="Student Information", font=font).grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    # Labels and entry fields for student information
    tk.Label(root, text="Name", font=font).grid(row=1, column=0, padx=10, pady=5)
    name_entry = tk.Entry(root, font=font)
    name_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(root, text="Birth date", font=font).grid(row=2, column=0, padx=10, pady=5)
    birth_date_entry = tk.Entry(root, font=font)
    birth_date_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(root, text="Grade", font=font).grid(row=3, column=0, padx=10, pady=5)
    grade_entry = tk.Entry(root, font=font)
    grade_entry.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(root, text="Reg No", font=font).grid(row=4, column=0, padx=10, pady=5)
    reg_no_entry = tk.Entry(root, font=font)
    reg_no_entry.grid(row=4, column=1, padx=10, pady=5)

    tk.Label(root, text="Email", font=font).grid(row=5, column=0, padx=10, pady=5)
    email_id_entry = tk.Entry(root, font=font)
    email_id_entry.grid(row=5, column=1, padx=10, pady=5)

    tk.Label(root, text="Gender", font=font).grid(row=6, column=0, padx=10, pady=5)
    gender_entry = tk.Entry(root, font=font)
    gender_entry.grid(row=6, column=1, padx=10, pady=5)

    tk.Label(root, text="Father's name", font=font).grid(row=7, column=0, padx=10, pady=5)
    father_name_entry = tk.Entry(root, font=font)
    father_name_entry.grid(row=7, column=1, padx=10, pady=5)

    tk.Label(root, text="Mother's name", font=font).grid(row=8, column=0, padx=10, pady=5)
    mother_name_entry = tk.Entry(root, font=font)
    mother_name_entry.grid(row=8, column=1, padx=10, pady=5)

    tk.Label(root, text="Address", font=font).grid(row=9, column=0, padx=10, pady=5)
    address_entry = tk.Entry(root, font=font)
    address_entry.grid(row=9, column=1, padx=10, pady=5)

    tk.Label(root, text="Phone number", font=font).grid(row=10, column=0, padx=10, pady=5)
    phone_no_entry = tk.Entry(root, font=font)
    phone_no_entry.grid(row=10, column=1, padx=10, pady=5)

    tk.Label(root, text="Religion", font=font).grid(row=11, column=0, padx=10, pady=5)
    religion_entry = tk.Entry(root, font=font)
    religion_entry.grid(row=11, column=1, padx=10, pady=5)

    # Function to insert student information into database
    def insert_student():
        name = name_entry.get()
        birth_date = birth_date_entry.get()
        grade = grade_entry.get()
        reg_no_value = reg_no_entry.get()
        email_id_value = email_id_entry.get()
        gender_value = gender_entry.get()
        father_name_value = father_name_entry.get()
        mother_name_value = mother_name_entry.get()
        address_value = address_entry.get()
        phone_no_value = phone_no_entry.get()
        religion_value = religion_entry.get()

        if not (name and birth_date and grade and reg_no_value and email_id_value and gender_value and
                father_name_value and mother_name_value and address_value and phone_no_value and religion_value):
            messagebox.showerror("Error", "Please fill in all fields")
        else:
            conn = sqlite3.connect('student.db')
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO student (name, birth_date, grade, reg_no, email_id, gender, father_name, mother_name, address, phone_no, religion) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (name, birth_date, grade, reg_no_value, email_id_value, gender_value, father_name_value, mother_name_value, address_value, phone_no_value, religion_value))
            conn.commit()
            conn.close()

            messagebox.showinfo("Success", "Student inserted successfully")

            # Clear entry fields after insert
            name_entry.delete(0, tk.END)
            birth_date_entry.delete(0, tk.END)
            grade_entry.delete(0, tk.END)
            reg_no_entry.delete(0, tk.END)
            email_id_entry.delete(0, tk.END)
            gender_entry.delete(0, tk.END)
            father_name_entry.delete(0, tk.END)
            mother_name_entry.delete(0, tk.END)
            address_entry.delete(0, tk.END)
            phone_no_entry.delete(0, tk.END)
            religion_entry.delete(0, tk.END)

    # Button to insert student details
    insert_button = tk.Button(root, text="Insert Student", font=font, command=insert_student)
    insert_button.grid(row=12, column=0, padx=10, pady=10)

    # Function to fetch student information from database
    def fetch_student():
        reg_no = reg_no_entry.get()

        conn = sqlite3.connect('student.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM student WHERE reg_no=?", (reg_no,))
        student = cursor.fetchone()
        conn.close()

        if student:
            # Populate entry fields with fetched student details
            name_entry.delete(0, tk.END)
            birth_date_entry.delete(0, tk.END)
            grade_entry.delete(0, tk.END)
            email_id_entry.delete(0, tk.END)
            gender_entry.delete(0, tk.END)
            father_name_entry.delete(0, tk.END)
            mother_name_entry.delete(0, tk.END)
            address_entry.delete(0, tk.END)
            phone_no_entry.delete(0, tk.END)
            religion_entry.delete(0, tk.END)

            name_entry.insert(tk.END, student[1])
            birth_date_entry.insert(tk.END, student[2])
            grade_entry.insert(tk.END, student[3])
            email_id_entry.insert(tk.END, student[5])
            gender_entry.insert(tk.END, student[6])
            father_name_entry.insert(tk.END, student[7])
            mother_name_entry.insert(tk.END, student[8])
            address_entry.insert(tk.END, student[9])
            phone_no_entry.insert(tk.END, student[10])
            religion_entry.insert(tk.END, student[11])
        else:
            messagebox.showerror("Error", "Student not found")

    # Button to fetch student details
    fetch_button = tk.Button(root, text="Fetch Student", font=font, command=fetch_student)
    fetch_button.grid(row=12, column=1, padx=10, pady=10)

    # Function to update student details
    def update_student():
        reg_no = reg_no_entry.get()

        conn = sqlite3.connect('student.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM student WHERE reg_no=?", (reg_no,))
        student = cursor.fetchone()
        conn.close()

        if student:
            # Populate entry fields with current student details
            name_entry.delete(0, tk.END)
            birth_date_entry.delete(0, tk.END)
            grade_entry.delete(0, tk.END)
            email_id_entry.delete(0, tk.END)
            gender_entry.delete(0, tk.END)
            father_name_entry.delete(0, tk.END)
            mother_name_entry.delete(0, tk.END)
            address_entry.delete(0, tk.END)
            phone_no_entry.delete(0, tk.END)
            religion_entry.delete(0, tk.END)

            name_entry.insert(tk.END, student[1])
            birth_date_entry.insert(tk.END, student[2])
            grade_entry.insert(tk.END, student[3])
            email_id_entry.insert(tk.END, student[5])
            gender_entry.insert(tk.END, student[6])
            father_name_entry.insert(tk.END, student[7])
            mother_name_entry.insert(tk.END, student[8])
            address_entry.insert(tk.END, student[9])
            phone_no_entry.insert(tk.END, student[10])
            religion_entry.insert(tk.END, student[11])

            # Function to save updated student details
            def save_updated_student():
                updated_name = name_entry.get()
                updated_birth_date = birth_date_entry.get()
                updated_grade = grade_entry.get()
                updated_email_id = email_id_entry.get()
                updated_gender = gender_entry.get()
                updated_father_name = father_name_entry.get()
                updated_mother_name = mother_name_entry.get()
                updated_address = address_entry.get()
                updated_phone_no = phone_no_entry.get()
                updated_religion = religion_entry.get()

                conn = sqlite3.connect('student.db')
                cursor = conn.cursor()
                cursor.execute("""
                    UPDATE student 
                    SET name=?, birth_date=?, grade=?, email_id=?, gender=?, 
                        father_name=?, mother_name=?, address=?, phone_no=?, religion=?
                    WHERE reg_no=?
                    """, (updated_name, updated_birth_date, updated_grade, updated_email_id, updated_gender,
                          updated_father_name, updated_mother_name, updated_address, updated_phone_no,
                          updated_religion, reg_no))
                conn.commit()
                conn.close()

                messagebox.showinfo("Success", "Student details updated successfully")

                # Clear entry fields after update
                name_entry.delete(0, tk.END)
                birth_date_entry.delete(0, tk.END)
                grade_entry.delete(0, tk.END)
                email_id_entry.delete(0, tk.END)
                gender_entry.delete(0, tk.END)
                father_name_entry.delete(0, tk.END)
                mother_name_entry.delete(0, tk.END)
                address_entry.delete(0, tk.END)
                phone_no_entry.delete(0, tk.END)
                religion_entry.delete(0, tk.END)

            # Button to save updated student details
            save_button = tk.Button(root, text="Save Updated Details", font=font, command=save_updated_student)
            save_button.grid(row=13, column=1, columnspan=2, padx=10, pady=10)

        else:
            messagebox.showerror("Error", "Student not found")

    # Button to update student details
    update_button = tk.Button(root, text="Update Student Details", font=font, command=update_student)
    update_button.grid(row=12, column=2, padx=10, pady=10)

    # Function to delete student details
    def delete_student():
        reg_no = reg_no_entry.get()

        conn = sqlite3.connect('student.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM student WHERE reg_no=?", (reg_no,))
        student = cursor.fetchone()

        if student:
            confirm = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this student?")
            if confirm:
                cursor.execute("DELETE FROM student WHERE reg_no=?", (reg_no,))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Student deleted successfully")
                # Clear entry fields after deletion
                name_entry.delete(0, tk.END)
                birth_date_entry.delete(0, tk.END)
                grade_entry.delete(0, tk.END)
                email_id_entry.delete(0, tk.END)
                gender_entry.delete(0, tk.END)
                father_name_entry.delete(0, tk.END)
                mother_name_entry.delete(0, tk.END)
                address_entry.delete(0, tk.END)
                phone_no_entry.delete(0, tk.END)
                religion_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Student not found")

    # Button to delete student details
    delete_button = tk.Button(root, text="Delete Student", font=font, command=delete_student)
    delete_button.grid(row=12, column=3, padx=10, pady=10)

    root.mainloop()

# Function calls to initialize the application
create_db()
initialize_password()
login()
