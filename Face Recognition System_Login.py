from customtkinter import *
from PIL import Image
import os
from tkinter import messagebox

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("700x480")
        self.root.resizable(0, 0)
        self.root.wm_iconbitmap("appicon.ico")
        self.root.title("Face Recognition Management")

        # Load images
        self.load_images()

        # Build the UI
        self.build_ui()

    def load_images(self):
        # Load and set up icons and images with proper dimensions for CTkImage
        self.side_img = CTkImage(dark_image=Image.open(r"appImages\\side-img.jpg"), light_image=Image.open(r"appImages\\side-img.jpg"), size=(300, 480))
        self.email_icon = CTkImage(dark_image=Image.open(r"appImages\\email-icon.png"), light_image=Image.open(r"appImages\\email-icon.png"), size=(20, 20))
        self.password_icon = CTkImage(dark_image=Image.open(r"appImages\\password-icon.png"), light_image=Image.open(r"appImages\\password-icon.png"), size=(17, 17))
        self.eye_icon_show = CTkImage(dark_image=Image.open(r"appImages\\eye.png"), light_image=Image.open(r"appImages\\eye.png"), size=(15, 15))
        self.eye_icon_hide = CTkImage(dark_image=Image.open(r"appImages\\eye_hide.png"), light_image=Image.open(r"appImages\\eye_hide.png"), size=(15, 15))
        self.google_icon = CTkImage(dark_image=Image.open(r"appImages\\google-icon.png"), light_image=Image.open(r"appImages\\google-icon.png"), size=(17, 17))

    def build_ui(self):
        # Side image label
        CTkLabel(master=self.root, text="", image=self.side_img).pack(expand=True, side="left")

        # Frame for the form
        frame = CTkFrame(master=self.root, width=400, height=480, fg_color="#ffffff")
        frame.pack_propagate(0)
        frame.pack(expand=True, side="right")

        # Sign-in text
        CTkLabel(master=frame, text="Welcome to the\nFace Recognition Management", text_color="#601E88", anchor="w", justify="left",
                 font=("Arial Bold", 24)).pack(anchor="w", pady=(50, 5), padx=(25, 0))
        CTkLabel(master=frame, text="Sign in to your account", text_color="#7E7E7E", anchor="w", justify="left",
                 font=("Arial Bold", 12)).pack(anchor="w", padx=(25, 0))

        # Email label and entry
        CTkLabel(master=frame, text=" Username/Email:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14),
                 image=self.email_icon, compound="left").pack(anchor="w", pady=(38, 0), padx=(25, 0))
        self.email_entry = CTkEntry(master=frame, width=230, height=35, fg_color="#EEEEEE", border_color="#601E88", border_width=1,
                                    text_color="#000000")
        self.email_entry.pack(anchor="w", padx=(25, 0))

        # Password label and entry
        CTkLabel(master=frame, text=" Password:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14),
                 image=self.password_icon, compound="left").pack(anchor="w", pady=(21, 0), padx=(25, 0))
        self.password_entry = CTkEntry(master=frame, width=230, height=35, fg_color="#EEEEEE", border_color="#601E88", border_width=1,
                                       text_color="#000000", show="*")
        self.password_entry.pack(anchor="w", padx=(25, 0))

        # Eye button to toggle password visibility, with resized icon
        self.eye_button = CTkButton(master=frame, text="", width=40, fg_color="#EEEEEE", text_color="#000000",
                                    image=self.eye_icon_show, command=self.toggle_password)
        self.eye_button.place(x=210, y=295)  # Positioned near the password field

        # Login button
        CTkButton(master=frame, text="Login", fg_color="#601E88", hover_color="#E44982", font=("Arial Bold", 12),
                  text_color="#ffffff", width=225, command=self.authenticate).pack(anchor="w", pady=(40, 0), padx=(25, 0))

        # Google sign-in button
        CTkButton(master=frame, text="Continue With Google", fg_color="#EEEEEE", hover_color="#EEEEEE",
                  font=("Arial Bold", 9), text_color="#601E88", width=225, image=self.google_icon).pack(anchor="w", pady=(20, 0),
                                                                                                        padx=(25, 0))

    def authenticate(self):
        username = self.email_entry.get()
        password = self.password_entry.get()
        
        if username == "admin" and password == "password": # Basic authentication
            messagebox.showinfo("Login Success", "Authentication Successful")
            self.root.destroy()
            os.system("python main_window.py")
        else:
            messagebox.showerror("Login Failed", "Invalid Credentials")

    def toggle_password(self):
        if self.password_entry.cget("show") == "*":
            self.password_entry.configure(show="")
            self.eye_button.configure(image=self.eye_icon_hide)
        else:
            self.password_entry.configure(show="*")
            self.eye_button.configure(image=self.eye_icon_show)

if __name__ == "__main__":
    app = CTk()
    login_app = LoginApp(app)
    app.mainloop()