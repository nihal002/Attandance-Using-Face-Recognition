from tkinter import *
from tkinter import ttk
from PIL import Image , ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]

class Attendance:
        def __init__(self,root):
                self.root=root
                self.root.geometry("1350x687+0+0")
                self.root.title("Face Recognition System")


                # variable
                self.var_atten_id=StringVar()
                self.var_atten_roll=StringVar()
                self.var_atten_name=StringVar()
                self.var_atten_dep=StringVar()
                self.var_atten_time=StringVar()
                self.var_atten_date=StringVar()
                self.var_atten_attendance=StringVar()



        #first image
                img1=Image.open(r"C:\Users\hp\Desktop\face_recognition system\college_images\clg.jpg")
                img1=img1.resize((670,200),Image.ANTIALIAS)
                self.photoimg1=ImageTk.PhotoImage(img1)
                f_lbl=Label(self.root,image=self.photoimg1)
                f_lbl.place(x=0,y=0,width=670,height=200)
                
                #second image
                img2=Image.open(r"C:\Users\hp\Desktop\face_recognition system\college_images\girl.jpeg")
                img2=img2.resize((680,200),Image.ANTIALIAS)
                self.photoimg2=ImageTk.PhotoImage(img2)
                f_lbl=Label(self.root,image=self.photoimg2)
                f_lbl.place(x=670,y=0,width=680,height=200)

                 #background image
                img4=Image.open(r"C:\Users\hp\Desktop\face_recognition system\college_images\img1.jpeg")
                img4=img4.resize((1350,610),Image.ANTIALIAS)
                self.photoimg4=ImageTk.PhotoImage(img4)
                bg_img=Label(self.root,image=self.photoimg4)
                bg_img.place(x=0,y=130,width=1350,height=610)

                #main frame
                title=Label(bg_img,text="Attendance SYSTEM",font=("times new roman ",35,"bold"),bg="green",fg="white")
                title.place(x=0,y=0,width=1350,height=45)
                
                main_frame=Frame(bg_img,bd=2,bg="white")
                main_frame.place(x=2,y=50,width=1343,height=530)


                #left lebel
                left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="STUDENT Attendance DETAILS",font=("times new roman",12,"bold"))
                left_frame.place(x=5,y=5,width=660,height=495)
                
                img_left=Image.open(r"C:\Users\hp\Desktop\face_recognition system\college_images\student.jpg")
                img_left=img_left.resize((650,100),Image.ANTIALIAS)
                self.photoimg_left=ImageTk.PhotoImage(img_left)
                f_lbl=Label(left_frame,image=self.photoimg_left)
                f_lbl.place(x=2,y=0,width=655,height=100)

                left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text=" DETAILS",font=("times new roman",12,"bold"))
                left_frame.place(x=10,y=125,width=650,height=370)

                #attendance id
                student_id_label=Label(left_frame,text="AttendanceID:", font=("times new roman",12,"bold"),bg="white",width=12)
                student_id_label.grid(row=0,column=0,padx=5)

                student_id_entry=ttk.Entry(left_frame,textvariable=self.var_atten_id,width=20,font=("times new roman",12,"bold"))
                student_id_entry.grid(row=0,column=1,padx=10,sticky=W)


                #roll
                student_roll_label=Label(left_frame,text="Roll:",font=("times new roman",12,"bold"),bg="white",width=12)
                student_roll_label.grid(row=0,column=2,padx=5)

                student_roll_entry=ttk.Entry(left_frame,textvariable=self.var_atten_roll,width=20,font=("times new roman",12,"bold"))
                student_roll_entry.grid(row=0,column=3,padx=10,sticky=W)

                #Name 
                student_name_label=Label(left_frame,text="Name:",font=("times new roman",12,"bold"),bg="white",width=12)
                student_name_label.grid(row=1,column=0,padx=5)

                student_name_entry=ttk.Entry(left_frame,textvariable=self.var_atten_name,width=20,font=("times new roman",12,"bold"))
                student_name_entry.grid(row=1,column=1,padx=10,sticky=W)


                #department
                student_dep_label=Label(left_frame,text="Department:",font=("times new roman",12,"bold"),bg="white",width=12)
                student_dep_label.grid(row=1,column=2,padx=5)

                student_dep_entry=ttk.Entry(left_frame,textvariable=self.var_atten_dep,width=20,font=("times new roman",12,"bold"))
                student_dep_entry.grid(row=1,column=3,padx=10,sticky=W)

                #time
                student_time_label=Label(left_frame,text="Time:",font=("times new roman",12,"bold"),bg="white",width=12)
                student_time_label.grid(row=2,column=0,padx=5)

                student_time_entry=ttk.Entry(left_frame,textvariable=self.var_atten_time,width=20,font=("times new roman",12,"bold"))
                student_time_entry.grid(row=2,column=1,padx=10,sticky=W)
                

                #Date 
                student_date_label=Label(left_frame,text="Date:",font=("times new roman",12,"bold"),bg="white",width=12)
                student_date_label.grid(row=2,column=2,padx=5)

                student_date_entry=ttk.Entry(left_frame,textvariable=self.var_atten_date,width=20,font=("times new roman",12,"bold"))
                student_date_entry.grid(row=2,column=3,padx=10,sticky=W)


                #class division
                attendance_label=Label(left_frame,textvariable=self.var_atten_attendance,text="Attendance:",font=("times new roman",12,"bold"),bg="white",width=12)
                attendance_label.grid(row=3,column=0,padx=5)

                att_combo=ttk.Combobox(left_frame,font=("times new roman",12,"bold"),state="readonly",width=12)
                att_combo['values']=("Present","Absent")
                att_combo.current(0)
                att_combo.grid(row=3,column=1,padx=10,pady=5,sticky=W)


                #button frame
                btn_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
                btn_frame.place(x=10,y=300,width=620,height=30)
                
                import_btn=Button(btn_frame,text="IMPORT",command=self.importCsv,width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
                import_btn.grid(row=0,column=0)
                
                export_btn=Button(btn_frame,text="EXPORT",command=self.exportCsv,width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
                export_btn.grid(row=0,column=1)
                
                update_btn=Button(btn_frame,text="UPDATE",width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
                update_btn.grid(row=0,column=2)
                
                reset_btn=Button(btn_frame,text="RESET",command=self.reset_data,width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
                reset_btn.grid(row=0,column=3)


                #right frame 
                right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="  ATTENDANCE DETAILS",font=("times new roman",12,"bold"))
                right_frame.place(x=675,y=5,width=660,height=495)
                
                table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
                table_frame.place(x=5,y=5,width=648,height=465)

                # ----------------scroll bar---------------------
                scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
                scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
                
                self.AttendancereportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
                
                scroll_x.pack(side=BOTTOM,fill=X)
                scroll_y.pack(side=RIGHT,fill=Y)

                scroll_x.config(command=self.AttendancereportTable.xview)
                scroll_y.config(command=self.AttendancereportTable.yview)


                self.AttendancereportTable.heading("id",text="Attendance ID")
                self.AttendancereportTable.heading("roll",text="Roll ")
                self.AttendancereportTable.heading("name",text="Name")
                self.AttendancereportTable.heading("department",text="Department")
                self.AttendancereportTable.heading("time",text="Time")
                self.AttendancereportTable.heading("date",text="Date")
                self.AttendancereportTable.heading("attendance",text="Attendance")

                self.AttendancereportTable["show"]="headings"


                self.AttendancereportTable.column("id",width=150)
                self.AttendancereportTable.column("roll",width=150)
                self.AttendancereportTable.column("name",width=150)
                self.AttendancereportTable.column("department",width=150)
                self.AttendancereportTable.column("time",width=150)
                self.AttendancereportTable.column("date",width=150)
                self.AttendancereportTable.column("attendance",width=150)


                self.AttendancereportTable.pack(fill=BOTH,expand=1)
                self.AttendancereportTable.bind("<ButtonRelease>",self.get_cursor)
        

        #   fetch data
        def fetch_data(self,rows):
                self.AttendancereportTable.delete(*self.AttendancereportTable.get_children())
                for i in rows:
                        self.AttendancereportTable.insert("",END,values=i)
        
        #import csv
        def importCsv(self):
                global mydata
                mydata.clear()
                fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
                with open(fln) as myfile:
                        csvread=csv.reader(myfile,delimiter=',')
                        for i in csvread:
                                mydata.append(i)
                        self.fetch_data(mydata)

        # export function
        def exportCsv(self):
                try:
                        if len(mydata)<1:
                                messagebox.showerror("No data","no data found",parent=self.root)
                                return False
                        fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
                        with open(fln,mode="w",newline="") as myfile:
                                exp_write=csv.writer(myfile,delimiter=',')
                                for i in mydata:
                                        exp_write.writerow(i)
                                messagebox.showinfo("exported","your data exported to "+os.path.basename(fln)+"successfully")
                except Exception as es:
                                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)



        def get_cursor(self,event=""):
                cursor_row=self.AttendancereportTable.focus()
                contents=self.AttendancereportTable.item(cursor_row)
                rows=contents['values']
                self.var_atten_id.set(rows[0])
                self.var_atten_roll.set(rows[1])
                self.var_atten_name.set(rows[2])
                self.var_atten_dep.set(rows[3])
                self.var_atten_time.set(rows[4])
                self.var_atten_date.set(rows[5])
                self.var_atten_attendance.set(rows[6])

        def reset_data(self):
                self.var_atten_id.set("")
                self.var_atten_roll.set("")
                self.var_atten_name.set("")
                self.var_atten_dep.set("")
                self.var_atten_time.set("")
                self.var_atten_date.set("")
                self.var_atten_attendance.set("")






                        







if __name__ == "__main__":
        root=Tk()
        obj=Attendance(root)
        root.mainloop()
