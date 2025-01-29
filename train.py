from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np

class Train:
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

        # Train Data Button
        train_data_b1 = Button(self.root, text="Train Data", command=self.training_classifier, compound="top", cursor="hand2", fg="red", activeforeground="red", font=("Arial", 12, "bold"), borderwidth=0, highlightthickness=0, bg="#87CEFA")
        train_data_b1.place(x=100, y=300, width=1000, height=60)

    def training_classifier(self):
        data_dir = ("img_data")
        path = [ os.path.join(data_dir,file) for file in os.listdir(data_dir) ]

        face_list = []
        id_list = []

        for image in path:
            img = Image.open(image).convert('L') # Convert to grayscale image
            image_np = np.array(img,'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            face_list.append(image_np)
            id_list.append(id)
            cv2.imshow("Data Training...",image_np)
            cv2.waitKey(1) == 13
        id_list = np.array(id_list)

        # Train Classifier and Save
        train_classifier = cv2.face.LBPHFaceRecognizer_create()
        train_classifier.train(face_list,id_list)
        train_classifier.write("classifier_data.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Training Result","Data Training Completed!",parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()