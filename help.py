from tkinter import *
from tkinter import ttk
from PIL import Image , ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
        def __init__(self,root):
                self.root=root
                self.root.geometry("1350x687+0+0")
                self.root.title("Face Recognition System")


                title=Label(self.root,text="HELP",font=("times new roman ",35,"bold"),bg="white",fg="blue")
                title.place(x=0,y=0,width=1350,height=45)


                #   top image
                img_top=Image.open(r"C:\Users\hp\Desktop\face_recognition system\college_images\dev.jpeg")
                img_top=img_top.resize((1350,680),Image.ANTIALIAS)
                self.photoimg_top=ImageTk.PhotoImage(img_top)
                f_lbl=Label(self.root,image=self.photoimg_top)
                f_lbl.place(x=0,y=50,width=1350,height=680)

                dep_label=Label(f_lbl,text="Email:xyz@gmail.com",font=("times new roman",25,"bold"),bg="white")
                dep_label.place(x=500,y=200)



if __name__ == "__main__":
        root=Tk()
        obj=Help(root)
        root.mainloop()