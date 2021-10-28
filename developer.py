from tkinter import *
from tkinter import ttk
from PIL import Image , ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
        def __init__(self,root):
                self.root=root
                self.root.geometry("1350x687+0+0")
                self.root.title("Face Recognition System")


                title=Label(self.root,text="DEVELOPER",font=("times new roman ",35,"bold"),bg="white",fg="darkgreen")
                title.place(x=0,y=0,width=1350,height=45)


                #   top image
                img_top=Image.open(r"C:\Users\hp\Desktop\face_recognition system\college_images\dev.jpg")
                img_top=img_top.resize((1350,680),Image.ANTIALIAS)
                self.photoimg_top=ImageTk.PhotoImage(img_top)
                f_lbl=Label(self.root,image=self.photoimg_top)
                f_lbl.place(x=0,y=50,width=1350,height=680)


                main_frame=Frame(f_lbl,bd=2,bg="white")
                main_frame.place(x=830,y=10,width=500,height=600)


                img_top1=Image.open(r"C:\Users\hp\Desktop\face_recognition system\college_images\pic.jpg")
                img_top1=img_top1.resize((100,100),Image.ANTIALIAS)
                self.photoimg_top1=ImageTk.PhotoImage(img_top1)
                f_lb2=Label(main_frame,image=self.photoimg_top1)
                f_lb2.place(x=300,y=10,width=100,height=100)


                dep_label=Label(main_frame,text="hello my name is NA",font=("times new roman",12,"bold"),bg="white")
                dep_label.place(x=10,y=5)

                img_top2=Image.open(r"C:\Users\hp\Desktop\face_recognition system\college_images\images.jpg")
                img_top2=img_top2.resize((500,400),Image.ANTIALIAS)
                self.photoimg_top2=ImageTk.PhotoImage(img_top2)
                f_lb3=Label(main_frame,image=self.photoimg_top2)
                f_lb3.place(x=10,y=150,width=500,height=400)



if __name__ == "__main__":
        root=Tk()
        obj=Developer(root)
        root.mainloop()
