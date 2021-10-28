from tkinter import *
from tkinter import ttk
from PIL import Image , ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
        def __init__(self,root):
                self.root=root
                self.root.geometry("1350x687+0+0")
                self.root.title("Face Recognition System")

                #   ******* variables
                self.var_dep=StringVar()
                self.var_course=StringVar()
                self.var_year=StringVar()
                self.var_semester=StringVar()
                self.var_std_id=StringVar()
                self.var_std_name=StringVar()
                self.var_div=StringVar()
                self.var_roll=StringVar()
                self.var_gender=StringVar()
                self.var_dob=StringVar()
                self.var_email=StringVar()
                self.var_phone=StringVar()
                self.var_address=StringVar()
                self.var_teacher=StringVar()

                
                #first image
                img1=Image.open(r"C:\Users\hp\Desktop\face_recognition system\college_images\student.jpg")
                img1=img1.resize((450,120),Image.ANTIALIAS)
                self.photoimg1=ImageTk.PhotoImage(img1)
                f_lbl=Label(self.root,image=self.photoimg1)
                f_lbl.place(x=0,y=0,width=450,height=120)
                
                #second image
                img2=Image.open(r"C:\Users\hp\Desktop\face_recognition system\college_images\girl.jpeg")
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
                
                title=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman ",35,"bold"),bg="white",fg="darkgreen")
                title.place(x=0,y=0,width=1350,height=45)
                
                main_frame=Frame(bg_img,bd=2,bg="white")
                main_frame.place(x=5,y=50,width=1340,height=530)
                
                #left lebel
                left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="STUDENT DETAILS",font=("times new roman",12,"bold"))
                left_frame.place(x=10,y=10,width=655,height=490)
                
                img_left=Image.open(r"C:\Users\hp\Desktop\face_recognition system\college_images\student.jpg")
                img_left=img_left.resize((650,100),Image.ANTIALIAS)
                self.photoimg_left=ImageTk.PhotoImage(img_left)
                f_lbl=Label(left_frame,image=self.photoimg_left)
                f_lbl.place(x=5,y=0,width=650,height=100)
                
                #current course inf
                current_course_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,text="current course :",font=("times new roman",12,"bold"))
                current_course_frame.place(x=5,y=100,width=630,height=110)
                
                #deparment
                dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white",width=13)
                dep_label.grid(row=0,column=0,padx=10)
                
                dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly",width=16)
                dep_combo['values']=("select departament","computer","IT","civil","electronics")
                dep_combo.current(0)
                dep_combo.grid(row=0,column=1,padx=2,pady=10)
                
                #course
                dep_label=Label(current_course_frame,text="course",font=("times new roman",12,"bold"),bg="white",width=13)
                dep_label.grid(row=0,column=2,padx=10)
                
                dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly",width=16)
                dep_combo['values']=("select course","FE","SE","TE","BE")
                dep_combo.current(0)
                dep_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
                
                #year
                dep_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white",width=13)
                dep_label.grid(row=1,column=0,padx=10)
                
                dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly",width=16)
                dep_combo['values']=("select year","2018-19","2019-20","2020-21","2021-22")
                dep_combo.current(0)
                dep_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
                
                #semester
                dep_label=Label(current_course_frame,text="sememster",font=("times new roman",12,"bold"),bg="white",width=13)
                dep_label.grid(row=1,column=2,padx=10)
                
                dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly",width=16)
                dep_combo['values']=("select semester","sem1","sem2","sem3","sem4","sem5","sem6","sem7","sem8")
                dep_combo.current(0)
                dep_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
                
                #class student info
                class_student_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,text="class student info :",font=("times new roman",12,"bold"))
                class_student_frame.place(x=5,y=210,width=630,height=250)
                
                #student id
                student_id_label=Label(class_student_frame,text="StudentID:",font=("times new roman",12,"bold"),bg="white",width=12)
                student_id_label.grid(row=0,column=0,padx=5)
                
                studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
                studentID_entry.grid(row=0,column=1,padx=5,sticky=W)
                
                #student name
                student_name_label=Label(class_student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white",width=12)
                student_name_label.grid(row=0,column=2,padx=5)
                
                student_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
                student_name_entry.grid(row=0,column=3,padx=10,sticky=W)
                
                #class division
                class_div_label=Label(class_student_frame,text="Class Division:",font=("times new roman",12,"bold"),bg="white",width=12)
                class_div_label.grid(row=1,column=0,padx=5)
                
                #class_div_entry=ttk.Entry(class_student_frame,textvariable=self.var_div,width=20,font=("times new roman",12,"bold"))
                #class_div_entry.grid(row=1,column=1,padx=10,sticky=W)
                div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),state="readonly",width=12)
                div_combo['values']=("A","B","C")
                div_combo.current(0)
                div_combo.grid(row=1,column=1,padx=5,pady=5,sticky=W)
                
                #roll number
                roll_no_label=Label(class_student_frame,text="Roll No:",font=("times new roman",12,"bold"),bg="white",width=12)
                roll_no_label.grid(row=1,column=2,padx=5)
                
                roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
                roll_no_entry.grid(row=1,column=3,padx=5,sticky=W)
                
                #gender
                gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white",width=12)
                gender_label.grid(row=2,column=0,padx=5)
                
                #gender_entry=ttk.Entry(class_student_frame,textvariable=self.var_gender,width=20,font=("times new roman",12,"bold"))
                #gender_entry.grid(row=2,column=1,padx=10,sticky=W)

                gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly",width=13)
                gender_combo['values']=("Male","Female","Not to disclose")
                gender_combo.current(0)
                gender_combo.grid(row=2,column=1,padx=5,pady=2,sticky=W)
                
                #date of birth
                dob_label=Label(class_student_frame,text="DOB:",font=("times new roman",12,"bold"),bg="white",width=12)
                dob_label.grid(row=2,column=2,padx=5)
                
                dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
                dob_entry.grid(row=2,column=3,padx=5,sticky=W)
                
                #email
                email_label=Label(class_student_frame,text="Email:",font=("times new roman",12,"bold"),bg="white",width=12)
                email_label.grid(row=3,column=0,padx=5)
                
                email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
                email_entry.grid(row=3,column=1,padx=5,sticky=W)
                
                #phone no
                phone_label=Label(class_student_frame,text="Phone No:",font=("times new roman",12,"bold"),bg="white",width=12)
                phone_label.grid(row=3,column=2,padx=5)
                
                phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
                phone_entry.grid(row=3,column=3,padx=5,sticky=W)
                
                #addresss
                address_label=Label(class_student_frame,text="Address:",font=("times new roman",12,"bold"),bg="white",width=12)
                address_label.grid(row=4,column=0,padx=5)
                
                address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
                address_entry.grid(row=4,column=1,padx=5,sticky=W)
                
                #teacher name 
                teacher_label=Label(class_student_frame,text="Teacher Name:",font=("times new roman",12,"bold"),bg="white",width=12)
                teacher_label.grid(row=4,column=2,padx=5)
                
                teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
                teacher_entry.grid(row=4,column=3,padx=5,sticky=W)
                
                #radio buttons
                self.var_radio1=StringVar()
                radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
                radiobtn1.grid(row=5,column=0)
                
                self.var_radio2=StringVar()
                radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio2,text="No Photo Sample",value="No")
                radiobtn2.grid(row=5,column=1)
                
                #button frame
                btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
                btn_frame.place(x=0,y=160,width=620,height=30)
                
                save_btn=Button(btn_frame,text="Save",command=self.add_data,width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
                save_btn.grid(row=0,column=0)
                
                update_btn=Button(btn_frame,text="Update",command=self.update_data,width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
                update_btn.grid(row=0,column=1)
                
                reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
                reset_btn.grid(row=0,column=2)
                
                delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
                delete_btn.grid(row=0,column=3)
                
                #bttn frame 2
                btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
                btn_frame1.place(x=0,y=190,width=620,height=30)
                
                take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo",width=33,font=("times new roman",12,"bold"),bg="blue",fg="white")
                take_photo_btn.grid(row=0,column=0)
                
                update_btn=Button(btn_frame1,text="Update Photo",width=33,font=("times new roman",12,"bold"),bg="blue",fg="white")
                update_btn.grid(row=0,column=2)
                
                
                #right frame 
                right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="STUDENT DETAILS",font=("times new roman",12,"bold"))
                right_frame.place(x=680,y=10,width=655,height=490)
                
                img_right=Image.open(r"C:\Users\hp\Desktop\face_recognition system\college_images\clg.jpg")
                img_right=img_right.resize((650,120),Image.ANTIALIAS)
                self.photoimg_right=ImageTk.PhotoImage(img_right)
                
                f_lbl=Label(right_frame,image=self.photoimg_right)
                f_lbl.place(x=5,y=0,width=650,height=110)
                
                
                #+++++++++++++ SEARCH SYSTEM +++++++++++++++++++
                search_frame=LabelFrame(right_frame,bd=2,relief=RIDGE,text="Search System :",font=("times new roman",12,"bold"))
                search_frame.place(x=5,y=120,width=640,height=70)
                
                search_label=Label(search_frame,text="search by :",font=("times new roman",12,"bold"),bg="red",fg="white",width=10)
                search_label.grid(row=0,column=0,padx=10,sticky=W)
                
                search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="readonly",width=13)
                search_combo['values']=("select","roll no","phone no")
                search_combo.current(0)
                search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
                
                search_entry=ttk.Entry(search_frame,width=13,font=("times new roman",12,"bold"))
                search_entry.grid(row=0,column=2,padx=10,sticky=W)
                
                search_btn=Button(search_frame,text="search",width=13,font=("times new roman",12,"bold"),bg="blue",fg="white")
                search_btn.grid(row=0,column=3)
                
                show_btn=Button(search_frame,text="show all",width=13,font=("times new roman",12,"bold"),bg="blue",fg="white")
                show_btn.grid(row=0,column=4,padx=5)
                
                #table frame 
                table_frame=Frame(right_frame,bd=2,relief=RIDGE)
                table_frame.place(x=5,y=190,width=640,height=275)
                
                scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
                scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
                
                self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
                
                scroll_x.pack(side=BOTTOM,fill=X)
                scroll_y.pack(side=RIGHT,fill=Y)
                
                scroll_x.config(command=self.student_table.xview)
                scroll_y.config(command=self.student_table.yview)
                
                
                self.student_table.heading("dep",text="Department")
                self.student_table.heading("course",text="Course")
                self.student_table.heading("year",text="Year")
                self.student_table.heading("sem",text="Semester")
                self.student_table.heading("id",text="StudentId")
                self.student_table.heading("name",text="Name")
                self.student_table.heading("roll",text="Roll")
                self.student_table.heading("gender",text="Gender")
                self.student_table.heading("div",text="Division")
                self.student_table.heading("dob",text="DOB")
                self.student_table.heading("email",text="Email")
                self.student_table.heading("phone",text="Phone")
                self.student_table.heading("address",text="Address")
                self.student_table.heading("teacher",text="Teacher")
                self.student_table.heading("photo",text="Photo")
                self.student_table["show"]="headings"
                
                
                self.student_table.column("dep",width=150)
                self.student_table.column("course",width=150)
                self.student_table.column("year",width=150)
                self.student_table.column("sem",width=150)
                self.student_table.column("id",width=150)
                self.student_table.column("name",width=150)
                self.student_table.column("roll",width=150)
                self.student_table.column("gender",width=150)
                self.student_table.column("div",width=150)
                self.student_table.column("dob",width=150)
                self.student_table.column("email",width=150)
                self.student_table.column("phone",width=150)
                self.student_table.column("address",width=150)
                self.student_table.column("teacher",width=150)
                self.student_table.column("photo",width=150)
                self.student_table.pack(fill=BOTH,expand=1)
                # to bind data with table 
                self.student_table.bind("<ButtonRelease>",self.get_cursor)
                self.fetch_data()


        #**************function declaration*********************
        
        def add_data(self):
                if((self.var_dep.get()=="Select Department")or(self.var_std_name.get()=="")or(self.var_std_id.get()=="")):
                        messagebox.showerror("error","All fields are required")
                else:
                        try:
                                conn=mysql.connector.connect(host="localhost",user="root",password="12345",database="face_recognizer")
                                my_cursor=conn.cursor()
                                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                        self.var_dep.get(),
                                                                                                                        self.var_course.get(),
                                                                                                                        self.var_year.get(),
                                                                                                                        self.var_semester.get(),
                                                                                                                        self.var_std_id.get(),
                                                                                                                        self.var_std_name.get(),
                                                                                                                        self.var_div.get(),
                                                                                                                        self.var_roll.get(),
                                                                                                                        self.var_gender.get(),
                                                                                                                        self.var_dob.get(),
                                                                                                                        self.var_email.get(),
                                                                                                                        self.var_phone.get(),
                                                                                                                        self.var_address.get(),
                                                                                                                        self.var_teacher.get(),
                                                                                                                        self.var_radio1.get()
                                
                                ))
                                conn.commit()
                                self.fetch_data()
                                conn.close()
                                messagebox.showinfo("success","student details has been addded successfully",parent=self.root)
                        except Exception as es:
                                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


        #***************fetch data *************
        def fetch_data(self):
                conn=mysql.connector.connect(host="localhost",user="root",password="12345",database="face_recognizer")
                my_cursor=conn.cursor()  
                my_cursor.execute("select * from student")
                data=my_cursor.fetchall()
                if(len(data)!=0):
                        self.student_table.delete(*self.student_table.get_children())
                        for i in data:
                                self.student_table.insert("",END,values=i)
                        conn.commit()
                conn.close()


        #**************get cursor***************
        def get_cursor(self,event=""):
                cursor_focus=self.student_table.focus()
                #content is a variable
                content=self.student_table.item(cursor_focus)
                data=content["values"]
                self.var_dep.set(data[0])
                self.var_course.set(data[1])
                self.var_year.set(data[2])
                self.var_semester.set(data[3])
                self.var_std_id.set(data[4])
                self.var_std_name.set(data[5])
                self.var_div.set(data[6])
                self.var_roll.set(data[7])
                self.var_gender.set(data[8])
                self.var_dob.set(data[9])
                self.var_email.set(data[10])
                self.var_phone.set(data[11])
                self.var_address.set(data[12])
                self.var_teacher.set(data[13])
                self.var_radio1.set(data[14])
                
                
        #**************update function************
        def update_data(self):
                if((self.var_dep.get()=="Select Department")or(self.var_std_name.get()=="")or(self.var_std_id.get()=="")):
                        messagebox.showerror("error","All fields are required")
                else:
                        try:
                                Update=messagebox.askyesno("update","do u want to update yhis student details",parent=self.root)
                                if(Update>0):
                                        conn=mysql.connector.connect(host="localhost",user="root",password="12345",database="face_recognizer")
                                        my_cursor=conn.cursor()
                                        my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where student_id=%s",(
                                                                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                                                                        self.var_std_id.get()
                                                                                                                                                                                                                        
                                                                                                                                                                                                                                 ))
                                else:
                                        if not Update:
                                                return
                                messagebox.showinfo("success","student details updated successfully",parent=self.root)
                                conn.commit()
                                self.fetch_data()
                                conn.close()

                        except Exception as es:
                                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


                

                        
        

        #***********delete data ******
        def delete_data(self):
                if(self.var_std_id.get()==""):
                        messagebox.showerror("error","student id must be required",parent=self.root)
                else:
                        try:
                                delete=messagebox.askyesno("delete page","do you want to delete this student data",parent=self.root)
                                if(delete>0):
                                        conn=mysql.connector.connect(host="localhost",user="root",password="12345",database="face_recognizer")
                                        my_cursor=conn.cursor()
                                        sql="delete from student where Student_id=%s"
                                        val=(self.var_std_id.get(),)
                                        my_cursor.execute(sql,val)
                                else:
                                        if not delete:
                                                return
                                conn.commit()
                                self.fetch_data()
                                conn.close()
                                messagebox.showinfo("delete","student details deleted successfully",parent=self.root)

                        except Exception as es:
                                        messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)



        #*******************reset function**************** 
        def reset_data(self):
                self.var_dep.set("select department")
                self.var_course.set("select Course")
                self.var_year.set("select Year")
                self.var_semester.set("select Semester")
                self.var_std_id.set("")
                self.var_std_name.set("")
                self.var_div.set("Select Division")
                self.var_roll.set("")
                self.var_gender.set("Male")
                self.var_dob.set("")
                self.var_email.set("")
                self.var_phone.set("")
                self.var_address.set("")
                self.var_teacher.set("")
                self.var_radio1.set("")
        


        #++++++++++++++++++++ generate data set take  photo samples +++++++++++++++
        def generate_dataset(self):
                if((self.var_dep.get()=="Select Department")or(self.var_std_name.get()=="")or(self.var_std_id.get()=="")):
                        messagebox.showerror("error","All fields are required",parent=self.root)
                else:
                        try:
                                conn=mysql.connector.connect(host="localhost",user="root",password="12345",database="face_recognizer")
                                my_cursor=conn.cursor()
                                my_cursor.execute("select * from student")
                                myresult=my_cursor.fetchall()
                                id=0
                                for x in myresult:
                                        id+=1
                                my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where student_id=%s",(
                                                                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                                                                        self.var_std_id.get()==id+1
                                                                                                                                                                                                                        
                                                                                                                                                                                                                          ))
                                id=self.var_std_id.get()    
                                conn.commit()
                                self.fetch_data()
                                self.reset_data()
                                conn.close()


                                #**********load predefined data on face frontal from opencv******** 
                                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                                def face_cropped(img):
                                        #  to convert images to grey scale
                                        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)                
                                        faces=face_classifier.detectMultiScale(gray,1.3,5)
                                        #sscaling factor=1.3
                                        #minimum neighbour  =5
                                        for (x,y,w,h) in faces:                                                
                                                face_cropped=img[y:y+h,x:x+w]
                                                return face_cropped
                                
                                # camera opened   0 fro web camera anythingelse for other camera and path for some specific images
                                cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
                                img_id=0
                                while True:
                                        ret,my_frame=cap.read()
                                        if face_cropped(my_frame) is not None:
                                                img_id+=1
                                                face=cv2.resize(face_cropped(my_frame),(550,550))
                                                face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                                                #give a name to user file that has to be saved in folder
                                                file_name_path="data/user."+ str(id) +"."+str(img_id)+".jpg"
                                                cv2.imwrite(file_name_path,face)
                                                cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                                                cv2.imshow("cropped face",face)
                                
                                        if cv2.waitKey(1)==13 or int(img_id)==100:
                                                break
                                cap.release()
                                cv2.destroyAllWindows()
                                messagebox.showinfo("result","generating data set completed successfully")
                        
                        except Exception as es:
                                        messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)







                
if __name__ == "__main__":
        root=Tk()
        obj=Student(root)
        root.mainloop()
