import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import sqlite3

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("925x500+300+200")
        self.root.config(bg="#333")
        self.root.overrideredirect(True)
        self.img = PhotoImage(file="C:\\Users\\Srinath\\OneDrive\\Others\\Desktop\\ENMS\\login.png")
        self.lalelimg = tk.Label(self.root, image=self.img, bg='#333').place(x=50, y=50)
        self.aframe = tk.Frame(self.root, width=350, height=350, bg='#333').place(x=480, y=70)
        self.login = ttk.Label(self.aframe, text="Login", foreground="#57a1f8", background='#333',
                                font=('Calibri', 30, 'bold')).place(x=500, y=70)
        self.label_username = ttk.Label(self.aframe, text="Username:", font=('Calibri', 12,'bold'), background="#333",foreground="#57a1f8")
        self.label_username.place(x=560, y=140)

        self.entry_username = ttk.Entry(self.root, text="username")
        self.entry_username.insert(0, 'admin')
        self.entry_username.place(x=640, y=140)

        self.label_password = ttk.Label(self.root, text="Password:", font=('Calibri', 12,'bold'), background="#333",foreground="#57a1f8")
        self.label_password.place(x=560, y=200)

        self.entry_password = ttk.Entry(self.root, show="*")
        self.entry_password.place(x=640, y=200)
        self.style = ttk.Style()
        self.style.configure('Custom.TLabel', background='#57a1f8',font=('Calibri', 13))
        self.login_button = ttk.Button(self.root, text="Login", style='Custom.TLabel',command=self.authenticate)
        self.login_button.place(x=570, y=270)

    def authenticate(self):
        print("Authenticating...")
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username == "admin" and password == "admin":
            print("Login successful.")
            self.root.destroy()
            app = EngineeringManagementSystem(tk.Tk())
        else:
            print("Login failed.")
            messagebox.showerror("Login Failed", "Invalid username or password")

class EngineeringManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Engineering Management System")
        self.root.geometry("1000x600+300+200")
        self.root.resizable(0, 0)
        self.root.config(bg="#333")
        self.frame = tk.Frame(root, width=900, height=470,bg="#333")
        self.frame.grid(row=0, column=0)
        
        label_name = ttk.Label(self.frame, text="Engineer Name:",font=("Calibri', 12"),background="#333",foreground="#57a1f8")
        label_name.grid(row=0, column=0, padx=10, pady=10)

        entry_name = ttk.Entry(self.frame)
        entry_name.grid(row=0, column=1, padx=10, pady=10)

        label_role = ttk.Label(self.frame, text="Engineer Role:",font=("Calibri', 12"),background="#333",foreground="#57a1f8")
        label_role.grid(row=1, column=0, padx=10, pady=10)

        entry_role = ttk.Entry(self.frame)
        entry_role.grid(row=1, column=1, padx=10, pady=10)

        label_age = ttk.Label(self.frame, text="Age:",font=("Calibri', 12"),background="#333",foreground="#57a1f8")
        label_age.grid(row=0, column=2, padx=10, pady=10)

        entry_age = ttk.Entry(self.frame)
        entry_age.grid(row=0, column=3, padx=10, pady=10)

        label_contact_number = ttk.Label(self.frame, text="Contact Number:",font=("Calibri', 12"),background="#333",foreground="#57a1f8")
        label_contact_number.grid(row=2, column=2, padx=5, pady=5)

        entry_contact_number = ttk.Entry(self.frame)
        entry_contact_number.grid(row=2, column=3, padx=5, pady=5) 

        label_gender = ttk.Label(self.frame, text="Gender:",font=("Calibri', 12"),background="#333",foreground="#57a1f8")
        label_gender.grid(row=1, column=2, padx=10, pady=10)

        n = tk.StringVar()
        monthchoosen = ttk.Combobox(self.frame, width=15, textvariable=n)

        monthchoosen['values'] = ('Male', 'Female', 'Other')

        monthchoosen.grid(row=1, column=3 ,padx=10, pady=10)
        monthchoosen.current()

        label_contact_number1 = ttk.Label(self.frame, text="Qualification:",font=("Calibri', 12"),background="#333",foreground="#57a1f8")
        label_contact_number1.grid(row=2, column=0, padx=10, pady=10)

        entry_contact_number1 = ttk.Entry(self.frame)
        entry_contact_number1.grid(row=2, column=1, padx=10, pady=10) 
       
        submit_button = ttk.Button(self.frame, text="Submit", command=lambda: self.insert_engineer_data(
            entry_name.get(), entry_role.get(), entry_age.get(), entry_contact_number.get(),monthchoosen.get(), entry_contact_number1.get()))
        submit_button.grid(row=5, column=0, columnspan=2, pady=10)

        delete_label = ttk.Label(self.frame, text="Delete Engineer (Enter ID):",font=("Calibri', 12"),background="#333",foreground="#57a1f8")
        delete_label.grid(row=6, column=0, padx=10, pady=10)

        delete_entry = ttk.Entry(self.frame)
        delete_entry.grid(row=6, column=1, padx=10, pady=10)

        delete_button = ttk.Button(self.frame, text="Delete", command=lambda: self.delete_engineer_data(delete_entry.get()))
        delete_button.grid(row=7, column=0, columnspan=2, pady=10)

        clear_button = ttk.Button(self.frame, text="Clear", command=lambda: self.clear_entries(
            entry_name, entry_role, entry_age, entry_contact_number, monthchoosen, delete_entry))
        clear_button.grid(row=5, column=1, columnspan=2, pady=10)

        list_all_button = ttk.Button(self.frame, text="List All Profiles",
                                     command=lambda: self.display_all_engineer_data(results_text))
        list_all_button.grid(row=7, column=1, columnspan=2, pady=10)

        
        label_search = ttk.Label(self.frame, text="Search Engineer:",font=("Calibri', 12"),background="#333",foreground="#57a1f8")
        label_search.grid(row=6, column=2, padx=10, pady=10)

        entry_search = ttk.Entry(self.frame)
        entry_search.grid(row=6, column=3, padx=10, pady=10)

        search_button = ttk.Button(self.frame, text="Search",
                                   command=lambda: self.display_search_results(results_text, entry_search.get()))
        search_button.grid(row=6, column=4, pady=10)

        results_text = tk.Text(self.frame, wrap=tk.WORD, width=60, height=15, state=tk.DISABLED)
        results_text.grid(row=10, column=1, columnspan=3, padx=10, pady=10)
       

        try:
            print("Connecting to the database...")
            self.conn = sqlite3.connect('engineer_data.db')
            self.create_table()
        except Exception as e:
            print(f"Error connecting to the database: {e}")

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def create_table(self):
        try:
            with self.conn:
                cursor = self.conn.cursor()
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS engineers (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        role TEXT NOT NULL,
                        age INTEGER,
                        contact_number TEXT,
                        gender TEXT,
                        Qualification TEXT
                    )
                ''')
        except Exception as e:
            print(f"Error creating table: {e}")

    def insert_engineer_data(self, name, role, age, contact_number, gender,Qualification):
        try:
            with self.conn:
                cursor = self.conn.cursor()
                cursor.execute("INSERT INTO engineers (name, role, age, contact_number, gender,Qualification) VALUES (?, ?, ?, ?, ?,?)",
                               (name, role, age, contact_number, gender,Qualification))
        except Exception as e:
            print(f"Error inserting data: {e}")

    def delete_engineer_data(self, engineer_id):
        try:
            with self.conn:
                cursor = self.conn.cursor()
                cursor.execute("DELETE FROM engineers WHERE id=?", (engineer_id,))
        except Exception as e:
            print(f"Error deleting data: {e}")

    def fetch_all_engineer_data(self):
        try:
            with self.conn:
                cursor = self.conn.cursor()
                cursor.execute("SELECT * FROM engineers")
                return cursor.fetchall()
        except Exception as e:
            print(f"Error fetching all data: {e}")
            return []

    def display_all_engineer_data(self, results_text):
        try:
            results_text.config(state=tk.NORMAL)
            results_text.delete(1.0, tk.END)

            data = self.fetch_all_engineer_data()
            if data:
                for entry in data:
                    results_text.insert(tk.END, f"ID: {entry[0]}, Name: {entry[1]}, Role: {entry[2]}, Age: {entry[3]}, "
                                                f"Contact Number: {entry[4]}, Gender: {entry[5]},Qualification:{entry[6]}\n")
            else:
                results_text.insert(tk.END, "No engineer profiles found.")

            results_text.config(state=tk.DISABLED)
        except Exception as e:
            print(f"Error displaying all data: {e}")

    def fetch_engineer_data(self, search_term):
        try:
            with self.conn:
                cursor = self.conn.cursor()
                cursor.execute("SELECT name FROM engineers WHERE name LIKE ? OR role LIKE ? ORDER BY name",
                               ('%' + search_term + '%', '%' + search_term + '%'))
                return cursor.fetchall()
        except Exception as e:
            print(f"Error fetching data: {e}")
            return []

    def display_search_results(self, results_text, search_term):
        try:
            results_text.config(state=tk.NORMAL)
            results_text.delete(1.0, tk.END)

            data = self.fetch_engineer_data(search_term)
            if data:
                for entry in data:
                    results_text.insert(tk.END, f"Name: {entry[0]}\n")
            else:
                results_text.insert(tk.END, "No matching results found.")

            results_text.config(state=tk.DISABLED)
        except Exception as e:
            print(f"Error displaying search results: {e}")

    def init_tasks_tab(self):
        print("Initializing Tasks Tab...")
        label_search = ttk.Label(self.tab2, text="Search Engineer:")
        label_search.grid(row=0, column=0, padx=10, pady=10)

        entry_search = ttk.Entry(self.tab2)
        entry_search.grid(row=0, column=1, padx=10, pady=10)

        search_button = ttk.Button(self.tab2, text="Search",
                                   command=lambda: self.display_search_results(results_text, entry_search.get()))
        search_button.grid(row=0, column=2, pady=10)

        results_text = tk.Text(self.tab2, wrap=tk.WORD, width=60, height=15, state=tk.DISABLED)
        results_text.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        # Add a vertical scrollbar
        scrollbar = tk.Scrollbar(self.tab2, command=results_text.yview)
        scrollbar.grid(row=1, column=3, sticky='ns')
        results_text.config(yscrollcommand=scrollbar.set)

    def on_closing(self):
        try:
            self.conn.close()
            self.root.destroy()
        except Exception as e:
            print(f"Error closing the application: {e}")

    def clear_entries(self, *entries):
        for entry in entries:
            entry.delete(0, tk.END)


login_window = tk.Tk()
login_app = LoginWindow(login_window)

login_window.mainloop()
