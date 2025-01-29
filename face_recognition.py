from tkinter import *
from tkinter import ttk
from db_connection import get_db_connection
from PIL import Image, ImageTk
from tkinter import messagebox
from datetime import datetime
from threading import Thread
import mysql.connector
import numpy as np
import cv2

# Threaded VideoStream Class for better performance
class VideoStream:
    def __init__(self, src=0):
        self.stream = cv2.VideoCapture(src)
        self.grabbed, self.frame = self.stream.read()
        self.stopped = False

    def start(self):
        # Start the thread to read frames from the video stream
        Thread(target=self.update, args=()).start()
        return self

    def update(self):
        # Keep looping infinitely until the thread is stopped
        while True:
            if self.stopped:
                return
            self.grabbed, self.frame = self.stream.read()

    def read(self):
        # Return the frame most recently read
        return self.frame

    def stop(self):
        # Indicate that the thread should be stopped
        self.stopped = True
        self.stream.release()

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{self.screen_width}x{self.screen_height}+0+0")
        self.root.wm_iconbitmap("appicon.ico")
        self.root.title("Face Recognition Management")

        # Background image
        img = Image.open(r"appImages/residential_district.jpg")
        img = img.resize((self.screen_width, self.screen_height), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img)

        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=self.screen_width, height=self.screen_height)

        # Face Recognition Button
        train_data_b1 = Button(self.root, text="Face Recognition", command=self.face_recog, compound="top", cursor="hand2", fg="red", activeforeground="red", font=("Arial", 12, "bold"), borderwidth=0, highlightthickness=0, bg="#87CEFA")
        train_data_b1.place(x=100, y=300, width=1000, height=60)

    # Attendance Monitoring
    def attendance_monitoring(self, id, name, apartment, room):
        conn = get_db_connection()
        my_cursor = conn.cursor()

        # Collect the data to insert
        current_time = datetime.now()
        date = current_time.strftime("%Y-%m-%d")
        time = current_time.strftime("%H:%M:%S")
        status = "Detected"

        # Insert data into the attendance table
        insert_query = """
            INSERT INTO attendance (surv_name, surv_apartment, surv_room, surv_date, surv_time, surv_status)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        try:
            my_cursor.execute(insert_query, (name, apartment, room, date, time, status))
            conn.commit()
        except mysql.connector.Error as error:
            print(f"Error inserting data: {error}")
        finally:
            my_cursor.close()
            conn.close()

    # Face Recognition Function
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbors)

            coordinates = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
                id, predict = clf.predict(gray_img[y:y+h, x:x+w])  # Use clf (the LBPHFaceRecognizer) for prediction
                confidence = int((100 * (1 - predict / 300)))

                conn = get_db_connection()
                my_cursor = conn.cursor()

                # Fetch ID
                my_cursor.execute(f"select t_id from tenant where t_id={id}")
                i = my_cursor.fetchone()
                i = "+".join([str(x) for x in i]) if i else "Unknown"

                # Fetch Name
                my_cursor.execute(f"select t_name from tenant where t_id={id}")
                j = my_cursor.fetchone()
                j = "+".join([str(x) for x in j]) if j else "Unknown"

                # Fetch Apartment
                my_cursor.execute(f"select t_apartment from tenant where t_id={id}")
                k = my_cursor.fetchone()
                k = "+".join([str(x) for x in k]) if k else "Unknown"

                # Fetch Room
                my_cursor.execute(f"select t_room from tenant where t_id={id}")
                l = my_cursor.fetchone()
                l = "+".join([str(x) for x in l]) if l else "Unknown"

                if confidence > 80:
                    cv2.putText(img, f"id: {i}", (x, y-75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 2)
                    cv2.putText(img, f"Name: {j}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 2)
                    cv2.putText(img, f"Apartment: {k}", (x, y-35), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 2)
                    cv2.putText(img, f"Room: {l}", (x, y-15), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 2)
                    self.attendance_monitoring(i, j, k, l)
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 4)
                    cv2.putText(img, "Unknown Person", (x, y-15), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 2)
                coordinates = [x, y, w, h]
            return coordinates

        
        def recognize(img, classifier, faceCascade):
            coordinates = draw_boundary(img, faceCascade, 1.1, 10, (0, 255, 0), "Face", classifier) # Green
            return img
        
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        classifier = cv2.face.LBPHFaceRecognizer_create()
        classifier.read("classifier_data.xml")  # Loading trained classifier data

        # Use Threaded Video Capture
        video_stream = VideoStream().start()

        while True:
            img = video_stream.read()  # Read the frame from the video stream
            if img is None:  # Safety check to prevent crashing if no frame is available
                print("Error: Unable to capture video frame")
                break

            img = recognize(img, classifier, faceCascade)
            cv2.imshow("Face Recognition Window", img)

            if cv2.waitKey(1) == 13:  # Break when Enter is pressed
                print("Exit signal received, releasing video capture...")
                break

        video_stream.stop()  # Stop the video stream
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()