from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from db_connection import get_db_connection
from dotenv import load_dotenv
import os
import mysql.connector
import cv2

class Tenant:
    def __init__(self, root):
        self.root = root
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{self.screen_width}x{self.screen_height}+0+0")
        self.root.wm_iconbitmap("appicon.ico")
        self.root.title("Face Recognition Management")

        # Variables
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_phone = StringVar()
        self.var_email = StringVar()
        self.var_apartment = StringVar()
        self.var_room = StringVar()
        self.var_occupancy_period = StringVar()
        self.var_occupancy_number = StringVar()
        self.var_radio1 = StringVar()


        # Background image
        img = Image.open(r"appImages\residential_district.jpg")
        img = img.resize((self.screen_width, self.screen_height), Image.BICUBIC)
        self.photoimg1 = ImageTk.PhotoImage(img)

        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=self.screen_width, height=self.screen_height)

        main_frame = Frame(bg_img,bd=2)
        main_frame.place(x=10,y=55,width=1255,height=600)

        #Left frame
        Left_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Tenant Registration",font=("times new roman",12,"bold"))
        Left_frame.place(x=0,y=10,width=660,height=580)

        #Current Information
        current_information_frame = LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Information",font=("times new roman",12,"bold"))
        current_information_frame.place(x=5,y=135,width=648,height=150)

        #Apartment Selection
        aptmt_label = Label(current_information_frame, text="Apartment", font=("times new roman", 12, "bold"),bg="white")
        aptmt_label.grid(row=0, column=0, padx=10, sticky=W)

        aptmt_combo = ttk.Combobox(current_information_frame, textvariable=self.var_apartment, font=("times new roman", 12, "bold"), width=17, state="readonly")
        aptmt_combo["values"] = ("Select Apartment", "1", "2", "3", "4", "5")
        aptmt_combo.current(0)
        aptmt_combo.grid(row=0, column=1, padx=2,pady=10,sticky=W)

        #Room Number Selection
        room_label = Label(current_information_frame, text="Room", font=("times new roman", 12, "bold"),bg="white")
        room_label.grid(row=0, column=2, padx=10, sticky=W)

        room_combo = ttk.Combobox(current_information_frame, textvariable=self.var_room, font=("times new roman", 12, "bold"), width=17, state="readonly")
        room_combo["values"] = ("Select Room", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
        room_combo.current(0)
        room_combo.grid(row=0, column=3, padx=2,pady=10,sticky=W)

        #Occupancy Period Selection
        year_label = Label(current_information_frame, text="Year", font=("times new roman", 12, "bold"),bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_label = ttk.Combobox(current_information_frame, textvariable=self.var_occupancy_period, font=("times new roman", 12, "bold"), width=17, state="readonly")
        year_label["values"] = ("Select Year", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25", "2025-26", "2026-27", "2027-28", "2028-29", "2029-30")
        year_label.current(0)
        year_label.grid(row=1, column=1, padx=2,pady=10,sticky=W)

        #Occupancy Number Selection
        occupancy_label = Label(current_information_frame, text="Occupancy Number", font=("times new roman", 12, "bold"),bg="white")
        occupancy_label.grid(row=1, column=2, padx=10, sticky=W)

        occupancy_label = ttk.Combobox(current_information_frame, textvariable=self.var_occupancy_number, font=("times new roman", 12, "bold"), width=17, state="readonly")
        occupancy_label["values"] = ("Select Occupancy Number", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
        occupancy_label.current(0)
        occupancy_label.grid(row=1, column=3, padx=2,pady=10,sticky=W)


        #Occupant Information
        occupant_information_frame = LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Occupant Information",font=("times new roman",12,"bold"))
        occupant_information_frame.place(x=5,y=300,width=648,height=250)

        #Occupant ID Entry
        occupantId_label = Label(occupant_information_frame, text="ID", font=("times new roman", 12),bg="white")
        occupantId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        occupantId_entry = ttk.Entry(occupant_information_frame,textvariable=self.var_id,width=20,font=("times new roman", 12))
        occupantId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #Occupant Name Entry
        occupantName_label = Label(occupant_information_frame, text="Name", font=("times new roman", 12),bg="white")
        occupantName_label.grid(row=0, column=2, padx=10, pady=5,sticky=W)

        occupantName_entry = ttk.Entry(occupant_information_frame,textvariable=self.var_name,width=20,font=("times new roman", 12))
        occupantName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #Occupant Phone Entry
        occupantPhno_label = Label(occupant_information_frame, text="Phone Number", font=("times new roman", 12),bg="white")
        occupantPhno_label.grid(row=1, column=0, padx=10, pady=5,sticky=W)

        occupantPhno_entry = ttk.Entry(occupant_information_frame,textvariable=self.var_phone,width=20,font=("times new roman", 12))
        occupantPhno_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Occupant Email Entry
        occupantEmail_label = Label(occupant_information_frame, text="Email", font=("times new roman", 12),bg="white")
        occupantEmail_label.grid(row=1, column=2, padx=10, pady=5,sticky=W)

        occupantEmail_entry = ttk.Entry(occupant_information_frame,textvariable=self.var_email,width=20,font=("times new roman", 12))
        occupantEmail_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        # Radiobutton 1
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(occupant_information_frame, variable=self.var_radio1, text="Photo Sample Taken", value="Yes")
        radiobtn1.grid(row=5, column=0, sticky="w", padx=5, pady=5)
        
        # Radiobutton 2
        radiobtn2 = ttk.Radiobutton(occupant_information_frame, variable=self.var_radio1, text="Photo Sample NOT Taken", value="No")
        radiobtn2.grid(row=5, column=1, sticky="w", padx=5, pady=5)

        #Button Frame
        btn_frame = Frame(occupant_information_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=7,y=150,width=630,height=35)
        
        #Save Button
        save_btn = Button(btn_frame,text="Save",command=self.add_data,font=("times new roman", 12),bg="lightgreen",fg="black",width=16)
        save_btn.grid(row=0,column=0)

        #Update Button
        update_btn = Button(btn_frame,text="Update",command=self.update_data,font=("times new roman", 12),bg="yellow",fg="black",width=16)
        update_btn.grid(row=0,column=1)

        #Delete Button
        delete_btn = Button(btn_frame,text="Delete",command=self.delete_data,font=("times new roman", 12),bg="#FF9999",fg="black",width=16)
        delete_btn.grid(row=0,column=2)

        #Reset Button
        reset_btn = Button(btn_frame,text="Reset",command=self.reset_data,font=("times new roman", 12),bg="lightblue",fg="black",width=17)
        reset_btn.grid(row=0,column=3)

        # Button Frame2
        btn_frame2 = Frame(occupant_information_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame2.place(x=7, y=180, width=630, height=35)
        
        # Photo Take Button
        take_photo_btn = Button(btn_frame2, text="Take Photo Sample",command=self.generate_dataset, font=("times new roman", 12), bg="rosybrown", fg="black", width=33)
        take_photo_btn.grid(row=0, column=0)
        
        # Update Photo Button
        update_photo_btn = Button(btn_frame2, text="Update Photo Sample", font=("times new roman", 12), bg="rosybrown", fg="black", width=34)
        update_photo_btn.grid(row=0, column=1)


        #Right frame
        Right_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Tenant Database",font=("times new roman",12,"bold"))
        Right_frame.place(x=665,y=10,width=580,height=580)


        #Search Information
        #Occupant Information
        search_frame = LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search Information",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=135,width=568,height=70)

        #Search By
        search_label = Label(search_frame, text="Search By", font=("times new roman", 12),bg="lightcyan3")
        search_label.grid(row=0, column=0, padx=10, pady=5,sticky=W)

        #Search Selection
        search_combo = ttk.Combobox(search_frame, font=("times new roman", 12, "bold"), width=15, state="readonly")
        search_combo["values"] = ("Select", "ID", "Name", "Phone No", "Apartment")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2,pady=10,sticky=W)

        #Search Entry
        search_entry = ttk.Entry(search_frame,width=15,font=("times new roman", 12))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        #Search Button
        search_btn = Button(search_frame,text="Search",font=("times new roman", 12),bg="lightblue2",fg="black",width=8)
        search_btn.grid(row=0,column=3,padx=3)

        #Show All Button
        showAll_btn = Button(search_frame,text="Show All",font=("times new roman", 12),bg="lightblue2",fg="black",width=8)
        showAll_btn.grid(row=0,column=4,padx=3)

        #Table Frame
        table_frame = Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=570,height=350)

        #Table Scrollbar
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.tenant_table = ttk.Treeview(table_frame,columns=("ID","Name","Phone Number","Email","Apartment","Room","Occupancy Period","Occupancy Number","Photo Sample"),xscrollcommand=scroll_x,yscrollcommand=scroll_y)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.tenant_table.xview)
        scroll_y.config(command=self.tenant_table.yview)

        self.tenant_table.heading("#1", text="ID")
        self.tenant_table.heading("#2", text="Name")
        self.tenant_table.heading("#3", text="Phone Number")
        self.tenant_table.heading("#4", text="Email")
        self.tenant_table.heading("#5", text="Apartment")
        self.tenant_table.heading("#6", text="Room")
        self.tenant_table.heading("#7", text="Occupancy Period")
        self.tenant_table.heading("#8", text="Occupancy Number")
        self.tenant_table.heading("#9", text="Photo Sample")
        self.tenant_table["show"]="headings"

        # Adjust the width for each column
        self.tenant_table.column("ID", width=100)
        self.tenant_table.column("Name", width=150)
        self.tenant_table.column("Phone Number", width=150)
        self.tenant_table.column("Email", width=200)
        self.tenant_table.column("Apartment", width=100)
        self.tenant_table.column("Room", width=100)
        self.tenant_table.column("Occupancy Period", width=150)
        self.tenant_table.column("Occupancy Number", width=150)
        self.tenant_table.column("Photo Sample", width=150)

        self.tenant_table.pack(fill=BOTH,expand=1)
        self.tenant_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data() # call the function to get db data

    # Database Functions
    def add_data(self):
        if self.var_apartment.get() == "Select Apartment" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror("Error", "Please fill all fields!",parent=self.root)
        else:
            try:
                conn = get_db_connection()
                my_cursor = conn.cursor()
                #messagebox.showinfo("Success","DB Connection Established",parent=self.root)
                my_cursor.execute("insert into tenant values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_id.get(),
                    self.var_name.get(),
                    self.var_phone.get(),
                    self.var_email.get(),
                    self.var_apartment.get(),
                    self.var_room.get(),
                    self.var_occupancy_period.get(),
                    self.var_occupancy_number.get(),
                    self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data() # call the function to get db data
                conn.close()
                messagebox.showinfo("Success","Tenant data has been added",parent=self.root)
            except Exception as ex:
                messagebox.showerror("Error",f"An Error has been occurred due to :{str(ex)}",parent=self.root)

    
    # Fetch data from database
    def fetch_data(self):
        conn = get_db_connection()
        if conn:
            try:
                my_cursor = conn.cursor()
                
                db_name = conn.database
                
                my_cursor.execute(f"SELECT * FROM {db_name}.tenant")
                db_data = my_cursor.fetchall()

                if len(db_data) != 0:
                    self.tenant_table.delete(*self.tenant_table.get_children())
                    for i in db_data:
                        self.tenant_table.insert("", END, values=i)
                    conn.commit()
            except Exception as e:
                print(f"Error fetching data: {e}")
            finally:
                conn.close()
        else:
            print("Failed to connect to the database.")



    # Get cursor
    def get_cursor(self,event=""):
        cursor_focus = self.tenant_table.focus()
        table_content = self.tenant_table.item(cursor_focus)
        data = table_content["values"]

        self.var_id.set(data[0]),
        self.var_name.set(data[1]),
        self.var_phone.set(data[2]),
        self.var_email.set(data[3]),
        self.var_apartment.set(data[4]),
        self.var_room.set(data[5]),
        self.var_occupancy_period.set(data[6]),
        self.var_occupancy_number.set(data[7]),
        self.var_radio1.set(data[8])

    # Update function
    def update_data(self):
        if self.var_apartment.get() == "Select Apartment" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror("Error", "Please fill all fields!",parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update","Do you want to update the tenant details?",parent=self.root)
                if Update>0:
                    conn = get_db_connection()
                    my_cursor = conn.cursor()
                    my_cursor.execute("update tenant set t_name=%s,t_phno=%s,t_email=%s,t_apartment=%s,t_room=%s,t_occupancy_period=%s,t_occupancy_number=%s,t_photo_sample=%s where t_id=%s",(
                        self.var_name.get(),
                        self.var_phone.get(),
                        self.var_email.get(),
                        self.var_apartment.get(),
                        self.var_room.get(),
                        self.var_occupancy_period.get(),
                        self.var_occupancy_number.get(),
                        self.var_radio1.get(),
                        self.var_id.get()
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Tenant data has been successfully updated!",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as ex:
                messagebox.showerror("Error",f"An Error has been occurred due to :{str(ex)}",parent=self.root)

    # Delete function
    def delete_data(self):
        if self.var_id.get() == "":
            messagebox.showerror("Error","Please select a tenant to delete!",parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Tenant Delete Page","Do you want to delete this tenant?",parent=self.root)
                if delete>0:
                    conn = get_db_connection()
                    my_cursor = conn.cursor()
                    delete_query = "delete from tenant where t_id=%s"
                    val = (self.var_id.get(),)
                    my_cursor.execute(delete_query,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Tenant data has been successfully deleted!",parent=self.root)
            except Exception as ex:
                messagebox.showerror("Error",f"An Error has been occurred due to :{str(ex)}",parent=self.root)

    # Reset function
    def reset_data(self):
        self.var_apartment.set("Select Apartment")
        self.var_room.set("Select Room")
        self.var_occupancy_period.set("Select Year")
        self.var_occupancy_number.set("Select Occupancy Number")
        self.var_id.set("")
        self.var_name.set("")
        self.var_phone.set("")
        self.var_email.set("")
        self.var_radio1.set("")

    # Generate Dataset or Take Photo Sample
    def generate_dataset(self):
        if self.var_apartment.get() == "Select Apartment" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror("Error", "Please fill all fields!", parent=self.root)
        else:
            try:
                # Connect to database
                conn = get_db_connection()
                my_cursor = conn.cursor()

                # Directly use the ID from the input fields
                tenant_id = self.var_id.get()

                # Update tenant details in the database
                my_cursor.execute("update tenant set t_name=%s,t_phno=%s,t_email=%s,t_apartment=%s,t_room=%s,t_occupancy_period=%s,t_occupancy_number=%s,t_photo_sample=%s where t_id=%s", (
                    self.var_name.get(),
                    self.var_phone.get(),
                    self.var_email.get(),
                    self.var_apartment.get(),
                    self.var_room.get(),
                    self.var_occupancy_period.get(),
                    self.var_occupancy_number.get(),
                    self.var_radio1.get(),
                    tenant_id
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # Load haarcascade_frontalface_default file from OpenCV
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def crop_face_img(img):
                    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # convert to grayscale image
                    face_img = face_classifier.detectMultiScale(gray_img, 1.3, 5)  # scaling factor=1.3, Minimum Neighbor=5

                    for (x, y, w, h) in face_img:
                        crop_face_img = img[y:y + h, x:x + w]
                        return crop_face_img

                cap = cv2.VideoCapture(0)  # Open the default camera for capturing image
                img_id = 0
                while True:
                    ret, cam_frame = cap.read()
                    if crop_face_img(cam_frame) is not None:
                        img_id += 1
                        face = cv2.resize(crop_face_img(cam_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

                        # Use tenant_id to generate unique filenames
                        face_file_path = f"img_data/user.{tenant_id}.{img_id}.jpg"
                        cv2.imwrite(face_file_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face Image", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 50:  # Capture 50 sample images
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Face Image Capture", "Tenant face images have been captured!", parent=self.root)

            except Exception as ex:
                messagebox.showerror("Error", f"An error occurred due to: {str(ex)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Tenant(root)
    root.mainloop()