from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter
from PIL import Image , ImageTk
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance_page import Attendance
from developer import Developer
from help import Help
from time import strftime
from datetime import datetime





class face_recognition_system:
        def __init__(self,root):
                self.root=root
                self.root.geometry("1350x690+0+0")
                self.root.title("Face Recognition System")
                
                #first
                img1=Image.open(r"C:\Users\hp\Desktop\face_recognition system\college_images\university.jpg")
                img1=img1.resize((450,120),Image.ANTIALIAS)
                self.photoimg1=ImageTk.PhotoImage(img1)

                f_lbl=Label(self.root,image=self.photoimg1)
                f_lbl.place(x=0,y=0,width=450,height=120)
                
                #second image
                img2=Image.open(r"C:\Users\hp\Desktop\face_recognition system\college_images\facialrecognition.png")
                img2=img2.resize((450,120),Image.ANTIALIAS)
                self.photoimg2=ImageTk.PhotoImage(img2)
                
                f_lbl=Label(self.root,image=self.photoimg2)
                f_lbl.place(x=450,y=0,width=450,height=120)
                
                #third image
                img3=Image.open(r"C:\Users\hp\Desktop\face_recognition system\college_images\university.jpg")
                img3=img3.resize((450,100),Image.ANTIALIAS)
                self.photoimg3=ImageTk.PhotoImage(img3)
                f_lbl=Label(self.root,image=self.photoimg3)
                f_lbl.place(x=900,y=0,width=450,height=120)
                
                
                #background image
                img4=Image.open(r"C:\Users\hp\Desktop\face_recognition system\college_images\img1.jpeg")
                img4=img4.resize((1350,610),Image.ANTIALIAS)
                self.photoimg4=ImageTk.PhotoImage(img4)
                bg_img=Label(self.root,image=self.photoimg4)
                bg_img.place(x=0,y=130,width=1350,height=610)
                
                title=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman ",30,"bold"),bg="white",fg="red")
                title.place(x=0,y=0,width=1350,height=45)

                def time():
                        string=strftime('%H:%m:%S %p')
                        lbl.config(text=string)    #pack with label
                        lbl.after(1000,time)            #1000 millisecond

                lbl=Label(title,font=("times new roman ",13,"bold"),bg="white",fg="blue")
                lbl.place(x=0,y=0,width=110,height=50)
                time()
                
                
                #student 
                img5=Image.open(r"C:\Users\hp\Desktop\face_recognition system\college_images\student.jpg")
                img5=img5.resize((200,200),Image.ANTIALIAS)
                self.photoimg5=ImageTk.PhotoImage(img5)

                b1=Button(bg_img,image=self.photoimg5,command=self.student_details,cursor="hand2")
                b1.place(x=150,y=80,width=200,height=200)
                
                b1_1=Button(bg_img,text="student details",command=self.student_details,cursor="hand2",font=("times new roman ",15,"bold"),bg="darkblue",fg="white")
                b1_1.place(x=150,y=270,width=200,height=40)
                
                
                #detect face 
                img6=Image.open(r"C:\Users\hp\Desktop\face_recognition system\college_images\face_detector1.jpg")
                img6=img6.resize((200,200),Image.ANTIALIAS)
                self.photoimg6=ImageTk.PhotoImage(img6)
                b1=Button(bg_img,image=self.photoimg6,command=self.face_data ,cursor="hand2")
                b1.place(x=450,y=80,width=200,height=200)

                b1_2=Button(bg_img,text="face detector",command=self.face_data ,cursor="hand2",font=("times new roman ",15,"bold"),bg="darkblue",fg="white")
                b1_2.place(x=450,y=270,width=200,height=40)


                #attendance face 
                img7=Image.open(r"C:\Users\hp\Desktop\face_recognition system\college_images\smart-attendance.jpg")
                img7=img7.resize((200,200),Image.ANTIALIAS)
                self.photoimg7=ImageTk.PhotoImage(img7)
                b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.attendance_data)
                b1.place(x=750,y=80,width=200,height=200)
                
                b1_2=Button(bg_img,text="Attendace",cursor="hand2",command=self.attendance_data,font=("times new roman ",15,"bold"),bg="darkblue",fg="white")
                b1_2.place(x=750,y=270,width=200,height=40)


                #help button
                img8=Image.open(r"C:\Users\hp\Desktop\face_recognition system\college_images\help.jpg")
                img8=img8.resize((200,200),Image.ANTIALIAS)
                self.photoimg8=ImageTk.PhotoImage(img8)
                b1=Button(bg_img,image=self.photoimg8,command=self.help,cursor="hand2")
                b1.place(x=1050,y=80,width=200,height=200)
                
                b1_2=Button(bg_img,text="HELP",cursor="hand2",command=self.help,font=("times new roman ",15,"bold"),bg="darkblue",fg="white")
                b1_2.place(x=1050,y=270,width=200,height=40)


                #train button 
                img9=Image.open(r"C:\Users\hp\Desktop\face_recognition system\college_images\di.jpg")
                img9=img9.resize((200,200),Image.ANTIALIAS)
                self.photoimg9=ImageTk.PhotoImage(img9)
                b1=Button(bg_img,image=self.photoimg9,command=self.train_data ,cursor="hand2")
                b1.place(x=150,y=330,width=200,height=200)
                
                b1_2=Button(bg_img,text="Train",cursor="hand2",command=self.train_data ,font=("times new roman ",15,"bold"),bg="darkblue",fg="white")
                b1_2.place(x=150,y=510,width=200,height=40)
                
                #photos button
                img10=Image.open(r"C:\Users\hp\Desktop\face_recognition system\college_images\clg.jpg")
                img10=img10.resize((200,200),Image.ANTIALIAS)
                self.photoimg10=ImageTk.PhotoImage(img10)
                b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.open_img)
                b1.place(x=450,y=330,width=200,height=200)
                
                b1_2=Button(bg_img,text="photos",cursor="hand2",command=self.open_img,font=("times new roman ",15,"bold"),bg="darkblue",fg="white")
                b1_2.place(x=450,y=510,width=200,height=40)
                
                #developer button
                img11=Image.open(r"C:\Users\hp\Desktop\face_recognition system\college_images\dev.jpg")
                img11=img11.resize((200,200),Image.ANTIALIAS)
                self.photoimg11=ImageTk.PhotoImage(img11)
                b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.developer_data)
                b1.place(x=750,y=330,width=200,height=200)
                
                b1_2=Button(bg_img,text="developer",cursor="hand2",command=self.developer_data,font=("times new roman ",15,"bold"),bg="darkblue",fg="white")
                b1_2.place(x=750,y=510,width=200,height=40)
                
                
                #exit  button
                img12=Image.open(r"C:\Users\hp\Desktop\face_recognition system\college_images\exit.jpg")
                img12=img12.resize((200,200),Image.ANTIALIAS)
                self.photoimg12=ImageTk.PhotoImage(img12)
                b1=Button(bg_img,image=self.photoimg12,cursor="hand2",command=self.win_Exit)
                b1.place(x=1050,y=330,width=200,height=200)
                
                b1_2=Button(bg_img,text="exit",cursor="hand2",command=self.win_Exit, font=("times new roman ",15,"bold"),bg="darkblue",fg="white")
                b1_2.place(x=1050,y=510,width=200,height=40)
                
                
        #********function button***************
        def student_details(self):
                self.new_window=Toplevel(self.root)
                self.app=Student(self.new_window)

        def train_data(self):
                self.new_window=Toplevel(self.root)
                self.app=Train(self.new_window)\

        def face_data(self):
                self.new_window=Toplevel(self.root)
                self.app=Face_Recognition(self.new_window)


        def attendance_data(self):
                self.new_window=Toplevel(self.root)
                self.app=Attendance(self.new_window)

        def developer_data(self):
                self.new_window=Toplevel(self.root)
                self.app=Developer(self.new_window)


        def help(self):
                self.new_window=Toplevel(self.root)
                self.app=Help(self.new_window)

        

        ######## 
        def open_img(self):
                os.startfile("data")

        def win_Exit(self):
                self.win_Exit=tkinter.messagebox.askyesno("face recognition","are u sure to exit",parent=self.root)
                if self.win_Exit>0:
                        self.root.destroy()
                else:
                        return


if __name__ == "__main__":
    root=Tk()
    obj=face_recognition_system(root)
    root.mainloop()
