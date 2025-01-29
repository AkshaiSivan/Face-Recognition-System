from tkinter import *
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import mysql.connector
import csv
from db_connection import get_db_connection

class Attendance:
    def __init__(self, root):
        self.root = root
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{self.screen_width}x{self.screen_height}+0+0")
        self.root.wm_iconbitmap("appicon.ico")
        self.root.title("Face Recognition Management")

        # Variables
        self.var_surv_id = StringVar()
        self.var_surv_name = StringVar()
        self.var_surv_apartment = StringVar()
        self.var_surv_room = StringVar()
        self.var_surv_date = StringVar()
        self.var_surv_time = StringVar()
        self.var_surv_status = StringVar()

        # Background image
        img = Image.open(r"appImages\residential_district.jpg")
        img = img.resize((self.screen_width, self.screen_height), Image.BICUBIC)
        self.photoimg1 = ImageTk.PhotoImage(img)

        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=self.screen_width, height=self.screen_height)

        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=10, y=55, width=1255, height=600)

        # Left frame
        Left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Tenant Surveillance Data", font=("times new roman", 12, "bold"))
        Left_frame.place(x=0, y=10, width=660, height=580)

        inside_left_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Entry", font=("times new roman", 12, "bold"))
        inside_left_frame.place(x=5, y=135, width=648, height=410)

        # Attendance ID Entry
        attendanceId_label = Label(inside_left_frame, text="ID", font=("times new roman", 12), bg="white")
        attendanceId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        attendanceId_entry = ttk.Entry(inside_left_frame, width=20, textvariable=self.var_surv_id, font=("times new roman", 12))
        attendanceId_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Name Entry
        attendanceName_label = Label(inside_left_frame, text="Name", font=("times new roman", 12), bg="white")
        attendanceName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        attendanceName_entry = ttk.Entry(inside_left_frame, textvariable=self.var_surv_name, width=20, font=("times new roman", 12))
        attendanceName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Apartment Entry
        attendanceApartment_label = Label(inside_left_frame, text="Apartment", font=("times new roman", 12), bg="white")
        attendanceApartment_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        attendanceApartment_entry = ttk.Entry(inside_left_frame, textvariable=self.var_surv_apartment, width=20, font=("times new roman", 12))
        attendanceApartment_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Room Entry
        attendanceRoom_label = Label(inside_left_frame, text="Room", font=("times new roman", 12), bg="white")
        attendanceRoom_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        attendanceRoom_entry = ttk.Entry(inside_left_frame, textvariable=self.var_surv_room, width=20, font=("times new roman", 12))
        attendanceRoom_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Date Entry
        attendanceDate_label = Label(inside_left_frame, text="Date", font=("times new roman", 12), bg="white")
        attendanceDate_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        attendanceDate_entry = ttk.Entry(inside_left_frame, textvariable=self.var_surv_date, width=20, font=("times new roman", 12))
        attendanceDate_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # Time Entry
        attendanceTime_label = Label(inside_left_frame, text="Time", font=("times new roman", 12), bg="white")
        attendanceTime_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        attendanceTime_entry = ttk.Entry(inside_left_frame, textvariable=self.var_surv_time, width=20, font=("times new roman", 12))
        attendanceTime_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Surveillance Status Entry
        surveillance_label = Label(inside_left_frame, text="Surveillance Status", font=("times new roman", 12), bg="white")
        surveillance_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        self.surveillance_status = ttk.Combobox(inside_left_frame, textvariable=self.var_surv_status, font=("times new roman", 12), width=17, state="readonly")
        self.surveillance_status["values"] = ("Status", "Detected", "Not Detected")
        self.surveillance_status.grid(row=3, column=1, padx=10, pady=5, sticky=W)
        self.surveillance_status.current(0)

        # Button Frame
        btn_frame = Frame(inside_left_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=7, y=350, width=630, height=35)

        # Update Button
        update_btn = Button(btn_frame, text="Update", command=self.update_data, font=("times new roman", 12), bg="#FF9999", fg="black", width=16)
        update_btn.grid(row=0, column=2)

        # Reset Button
        reset_btn = Button(btn_frame, text="Reset", command=self.resetData, font=("times new roman", 12), bg="lightblue", fg="black", width=17)
        reset_btn.grid(row=0, column=3)

        # Export Button
        export_btn = Button(btn_frame, text="Export", command=self.export_data, font=("times new roman", 12), bg="#FFCC99", fg="black", width=16)
        export_btn.grid(row=0, column=4)

        # Import Button
        import_btn = Button(btn_frame, text="Import", command=self.import_data, font=("times new roman", 12), bg="#99FFCC", fg="black", width=16)
        import_btn.grid(row=0, column=5)

        # Right frame
        Right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Surveillance Database", font=("times new roman", 12, "bold"))
        Right_frame.place(x=665, y=10, width=580, height=580)

        # Button Frame
        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=570, height=540)

        # Scrollbar for table
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.SurveillanceReportTable = ttk.Treeview(table_frame, columns=("ID", "Name", "Apartment", "Room", "Date", "Time", "Surveillance Status"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.SurveillanceReportTable.xview)
        scroll_y.config(command=self.SurveillanceReportTable.yview)

        self.SurveillanceReportTable.heading("#1", text="Surveillance ID")
        self.SurveillanceReportTable.heading("#2", text="Name")
        self.SurveillanceReportTable.heading("#3", text="Apartment")
        self.SurveillanceReportTable.heading("#4", text="Room")
        self.SurveillanceReportTable.heading("#5", text="Date")
        self.SurveillanceReportTable.heading("#6", text="Time")
        self.SurveillanceReportTable.heading("#7", text="Surveillance Status")
        self.SurveillanceReportTable["show"] = "headings"

        # Adjust the width for each column
        self.SurveillanceReportTable.column("#1", width=100)
        self.SurveillanceReportTable.column("#2", width=100)
        self.SurveillanceReportTable.column("#3", width=100)
        self.SurveillanceReportTable.column("#4", width=100)
        self.SurveillanceReportTable.column("#5", width=100)
        self.SurveillanceReportTable.column("#6", width=100)
        self.SurveillanceReportTable.column("#7", width=150)

        self.SurveillanceReportTable.pack(fill=BOTH, expand=1)
        self.SurveillanceReportTable.bind("<ButtonRelease-1>", self.get_cursor)

        self.load_surveillance_data()

    def load_surveillance_data(self):
        try:
            conn = get_db_connection()
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM attendance")
            rows = my_cursor.fetchall()
            if len(rows) != 0:
                self.SurveillanceReportTable.delete(*self.SurveillanceReportTable.get_children())
                for row in rows:
                    self.SurveillanceReportTable.insert("", END, values=row)
            conn.close()
        except Exception as e:
            messagebox.showerror("Error", f"Could not load data: {str(e)}")

    def export_data(self):
        try:
            # Open a file dialog to choose the location to save the CSV
            file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
            if file_path:
                with open(file_path, mode='w', newline='') as file:
                    writer = csv.writer(file)
                    # Write the header
                    writer.writerow(["ID", "Name", "Apartment", "Room", "Date", "Time", "Surveillance Status"])
                    for row in self.SurveillanceReportTable.get_children():
                        writer.writerow(self.SurveillanceReportTable.item(row)['values'])
                messagebox.showinfo("Success", "Data exported successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Could not export data: {str(e)}")

    def import_data(self):
        try:
            # Open a file dialog to choose a CSV file to import
            file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
            if file_path:
                with open(file_path, mode='r') as file:
                    reader = csv.reader(file)
                    next(reader)  # Skip the header
                    conn = get_db_connection()
                    my_cursor = conn.cursor()
                    for row in reader:
                        my_cursor.execute("""
                            INSERT INTO attendance (surv_name, surv_apartment, surv_room, surv_date, surv_time, surv_status)
                            VALUES (%s, %s, %s, %s, %s, %s)
                        """, row[1:])  # Skip the ID column since it auto-increments
                    conn.commit()
                    conn.close()
                    self.load_surveillance_data()
                messagebox.showinfo("Success", "Data imported successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Could not import data: {str(e)}")


    def get_cursor(self, event):
        cursor_row = self.SurveillanceReportTable.focus()
        contents = self.SurveillanceReportTable.item(cursor_row)
        row = contents['values']
        self.var_surv_id.set(row[0])
        self.var_surv_name.set(row[1])
        self.var_surv_apartment.set(row[2])
        self.var_surv_room.set(row[3])
        self.var_surv_date.set(row[4])
        self.var_surv_time.set(row[5])
        self.var_surv_status.set(row[6])

    def resetData(self):
        self.var_surv_id.set("")
        self.var_surv_name.set("")
        self.var_surv_apartment.set("")
        self.var_surv_room.set("")
        self.var_surv_date.set("")
        self.var_surv_time.set("")
        self.var_surv_status.set("Status")

    def update_data(self):
        if self.var_surv_id.get() == "" or self.var_surv_name.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = get_db_connection()
                my_cursor = conn.cursor()
                my_cursor.execute("""
                    UPDATE attendance
                    SET Name=%s, Apartment=%s, Room=%s, Date=%s, Time=%s, Surveillance_Status=%s
                    WHERE ID=%s
                """, (
                    self.var_surv_name.get(),
                    self.var_surv_apartment.get(),
                    self.var_surv_room.get(),
                    self.var_surv_date.get(),
                    self.var_surv_time.get(),
                    self.var_surv_status.get(),
                    self.var_surv_id.get()
                ))
                conn.commit()
                self.load_surveillance_data()
                self.resetData()
                conn.close()
                messagebox.showinfo("Success", "Data updated successfully")
            except Exception as e:
                messagebox.showerror("Error", f"Could not update data: {str(e)}")

if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()