from tkinter import *
from tkinter import ttk
from PIL import Image , ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy  as np
from time import strftime
from datetime import datetime


class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x687+0+0")
        self.root.title("Face Recognition System")

        title=Label(self.root ,text="FACE RECOGNITION",font=("times new roman ",35,"bold"),bg="white",fg="green")
        title.place(x=0,y=0,width=1350,height=55)


        #left img 
        img_left=Image.open(r"C:\Users\hp\Desktop\face_recognition system\college_images\face_detector1.jpg")
        img_left=img_left.resize((675,645),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(self.root,image=self.photoimg_left)
        f_lbl.place(x=0,y=55,width=675,height=645)

        #right img
        img_right=Image.open(r"C:\Users\hp\Desktop\face_recognition system\college_images\fp.jpg")
        img_right=img_right.resize((675,645),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        f_lb2=Label(self.root,image=self.photoimg_right)
        f_lb2.place(x=675,y=55,width=675,height=645)

        b1_2=Button(f_lb2,text="FACE RECOGNITION",command=self.face_recog, cursor="hand2",font=("times new roman ",14,"bold"),bg="red",fg="white")
        b1_2.place(x=240,y=570,width=200,height=40)



        # attendance
    def mark_attendance(self,i,r,n,d):
        with open("attendance.csv","a+",newline="\n") as f:
            myDatalist=f.readlines()
            name_list=[]
            for line in myDatalist:
                entry=line.split((","))
                name_list.append(entry[0])
                #to prevent multiple attendance of same student
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtstring=now.strftime("%H:%M:%M")
                f.writelines(f"\n{i},{r},{n},{d},{dtstring},{d1},Present ")







    ##  ########        FACe RECOGNITION FUNCTION       ######
    def face_recog(self):
        #draw boundary acrosss face after recognition
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            #feature  contain the required   feature we will need in future
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            
            #cord to draw rectangle on the face
            cord=[]

            
            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",user="root",password="12345",database="face_recognizer")
                my_cursor=conn.cursor()

                my_cursor.execute("select Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)


                if confidence>77:
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-35),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Dep:{d}",(x,y-15),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i, r, n, d)

                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                cord=[x,y,w,y]
            return cord
        
        #
        def recognize(img,clf,faceCascade):
            cord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        facecascade=cv2.CascadeClassifier(r"C:\Users\hp\Desktop\face_recognition system\haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read(r"C:\Users\hp\Desktop\face_recognition system\classifier.xml")

        video_cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,facecascade)
            cv2.imshow("Welcome to face recognizer",img)
            if((cv2.waitKey(1))==13):                
                break
        video_cap.release()
        cv2.destroyAllWindows()
        

                    



if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()
