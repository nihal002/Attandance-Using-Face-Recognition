from tkinter import *
from tkinter import ttk
from PIL import Image , ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy  as np


class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x687+0+0")
        self.root.title("Face Recognition System")


        title=Label(self.root,text="TRAIN DATA SET",font=("times new roman ",35,"bold"),bg="white",fg="darkgreen")
        title.place(x=0,y=0,width=1350,height=45)


        #   top image
        img_top=Image.open(r"C:\Users\hp\Desktop\face_recognition system\college_images\facialrecognition.png")
        img_top=img_top.resize((1350,230),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=50,width=1350,height=230)

        # buttun of train dataset
        b1_2=Button(self.root,text="TRAIN DATA",command=self.train_classifier ,cursor="hand2",font=("times new roman ",35,"bold"),bg="darkblue",fg="white")
        b1_2.place(x=0,y=270,width=1350,height=70)

        #botttom image 
        img_top1=Image.open(r"C:\Users\hp\Desktop\face_recognition system\college_images\peoples.jpg")
        img_top1=img_top1.resize((1350,350),Image.ANTIALIAS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)
        
        f_lbl=Label(self.root,image=self.photoimg_top1)
        f_lbl.place(x=0,y=340,width=1350,height=350)
    

    def train_classifier(self):
        data_dir=(r"C:\Users\hp\Desktop\face_recognition system\data") #want data to be trained

        #list comprehension 
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')      # gray scale image converted
            imageNp=np.array(img,'uint8')           # numpy array to convert to grid   
            id=int(os.path.split(image)[1].split(".")[1])
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("training",imageNp)
            if(cv2.waitKey(1)==13):
                break
        ids=np.array(ids)


        ########train the classifier and save 
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")

        cv2.destroyAllWindows()
        messagebox.showinfo("Result","training data set completed",parent=self.root)




    



if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()
