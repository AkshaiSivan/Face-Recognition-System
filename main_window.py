from tkinter import *
from PIL import Image, ImageTk
from tenant import Tenant
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
import os

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{self.screen_width}x{self.screen_height}+0+0")
        self.root.wm_iconbitmap("appicon.ico")
        self.root.title("Face Recognition Management")

        # Background image
        img = Image.open(r"appImages\residential_district.jpg")
        img = img.resize((self.screen_width, self.screen_height), Image.BICUBIC)
        self.photoimg1 = ImageTk.PhotoImage(img)

        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=self.screen_width, height=self.screen_height)

        # Tenant Button
        tenant_img = Image.open(r"appImages\residents.jpg")
        tenant_img = tenant_img.resize((220, 220), Image.BICUBIC)
        self.photoimg2 = ImageTk.PhotoImage(tenant_img)

        tenant_b1 = Button(self.root, image=self.photoimg2, borderwidth=0, highlightthickness=0, command=self.tenant_button_click, cursor="hand2")
        tenant_b1.place(x=200, y=100, width=220, height=220)

        tenant_b1_1 = Button(self.root, text="Tenant Details", command=self.tenant_button_click, compound="top", cursor="hand2", fg="red", activeforeground="red", font=("Arial", 12, "bold"))
        tenant_b1_1.config(image=self.photoimg2)
        tenant_b1_1.place(x=200, y=100, width=220, height=250)

        # Detect Face Button
        detect_face_img = Image.open(r"appImages\DetectFace.jpg")
        detect_face_img = detect_face_img.resize((220, 220), Image.BICUBIC)
        self.photoimg3 = ImageTk.PhotoImage(detect_face_img)

        detect_face_b1 = Button(self.root, image=self.photoimg3, text="Detect Face", compound="top", command=self.detect_face_button_click, borderwidth=0, highlightthickness=0, cursor="hand2", fg="red", font=("Arial", 12, "bold"))
        detect_face_b1.place(x=500, y=100, width=220, height=250)  # Increased height for the text


        # Attendance Button
        attendance_img = Image.open(r"appImages\attendance.jpg")
        attendance_img = attendance_img.resize((220, 220), Image.BICUBIC)
        self.photoimg4 = ImageTk.PhotoImage(attendance_img)

        attendance_b1 = Button(self.root, image=self.photoimg4, text="Surveillance Data", command=self.attendance_button_click, compound="top", cursor="hand2", fg="red", activeforeground="red", font=("Arial", 12, "bold"), borderwidth=0, highlightthickness=0)
        attendance_b1.place(x=800, y=100, width=220, height=250)  # Increased height to 250

        # Train Data Button
        train_data_img = Image.open(r"appImages\datatrain.jpg")
        train_data_img = train_data_img.resize((220, 220), Image.BICUBIC)
        self.photoimg5 = ImageTk.PhotoImage(train_data_img)

        train_data_b1 = Button(self.root, image=self.photoimg5, text="Train Data", command=self.train_data_button_click, compound="top", cursor="hand2", fg="red", activeforeground="red", font=("Arial", 12, "bold"), borderwidth=0, highlightthickness=0)
        train_data_b1.place(x=300, y=380, width=220, height=250)  # Increased height to 250

        # Photos Button
        photos_img = Image.open(r"appImages\photos.jpg")  # Path to the image for the Photos button
        photos_img = photos_img.resize((220, 220), Image.BICUBIC)
        self.photoimg6 = ImageTk.PhotoImage(photos_img)

        photos_b1 = Button(self.root, image=self.photoimg6, text="Photos", command=self.photos_button_click, compound="top", cursor="hand2", fg="red", activeforeground="red", font=("Arial", 12, "bold"), borderwidth=0, highlightthickness=0)
        photos_b1.place(x=600, y=380, width=220, height=250)

    # Button Functions

    def tenant_button_click(self):
        self.new_window = Toplevel(self.root)
        self.app = Tenant(self.new_window)
        

    def detect_face_button_click(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)


    def attendance_button_click(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)


    def train_data_button_click(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)


    def photos_button_click(self):
        os.startfile("img_data")
        

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()