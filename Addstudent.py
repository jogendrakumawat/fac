
from logging import exception, root
import string
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from turtle import color, width
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import numpy as np
import mysql
import cv2
import os
import tkinter  as tk 
from tkcalendar import DateEntry
import re





class Studentinfo:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1350x765+100+0')
        self.root.resizable(0,0)
        self.root.title("Add Student Pannel")
        self.root.config(background='#CDCDC0')


# ============Variable==============
        self.var_id=StringVar()
        self.var_Name=StringVar()
        self.var_Enroll=StringVar()
        self.var_Branch=StringVar()
        self.var_Semester=StringVar()
        self.var_DOB=StringVar()
        self.var_Gender=StringVar()
        self.var_Email=StringVar()
        self.var_Mobile=StringVar()
        self.var_Address=StringVar()


        self.header =Frame(self.root,bg='#9400D3')
        self.header.place(x=0,y=0,width=1350,height=80)


        #title section
        title_lb1 = Label(self.header,text="Welcome to Student Pannel",font=("verdana",30,"bold"),bg="#9400D3",fg="white")
        title_lb1.place(x=205,y=15,width=900,height=50)

        # Creating Frame 
        main_frame = LabelFrame(self.root,bd=0,bg="#9400D3",relief=RIDGE,text="Student Details:",font=("verdana",15,"bold"),fg="white") 
        main_frame.place(x=35,y=120,width=1280,height=615)

    

        # Left Label Frame 
        left_frame = LabelFrame(main_frame,bd=0,bg="white")
        left_frame.place(x=20,y=15,width=610,height=555)

       
   # Student Id
        Id_label=Label(left_frame,text="Student Id:",font=("verdana",12,"bold"),bg="white",fg="navyblue")
        Id_label.grid(row=0,column=0,padx=40,pady=0,sticky=W)

        Enroll_entry = ttk.Entry(left_frame,textvariable=self.var_id,width=25,font=("verdana",12,"bold"))
        Enroll_entry.grid(row=0,column=1,padx=30,pady=5,sticky=W)
   
   
    #label Name
        name_label=Label(left_frame,text="Student Name:",font=("verdana",12,"bold"),bg="white",fg="navyblue")
        name_label.grid(row=1,column=0,padx=40,pady=10,sticky=W)

        student_name_entry = ttk.Entry(left_frame,textvariable=self.var_Name,width=25,font=("verdana",12,"bold"))
        student_name_entry.grid(row=1,column=1,padx=30,pady=10,sticky=W)



# Enrollment No
        Enroll_label=Label(left_frame,text="Enrollment No:",font=("verdana",12,"bold"),bg="white",fg="navyblue")
        Enroll_label.grid(row=2,column=0,padx=40,pady=10,sticky=W)

        Enroll_entry = ttk.Entry(left_frame,textvariable=self.var_Enroll,width=25,font=("verdana",12,"bold"))
        Enroll_entry.grid(row=2,column=1,padx=30,pady=10,sticky=W)


        # Branch
        Branch_label=Label(left_frame,text="Branch Name:",font=("verdana",12,"bold"),bg="white",fg="navyblue")
        Branch_label.grid(row=3,column=0,padx=40,pady=10,sticky=W)

        branch_combo=ttk.Combobox(left_frame,textvariable=self.var_Branch,width=23,font=("verdana",12,"bold"),state="readonly")
        branch_combo["values"]=("Select Branch","IT","CE","CSE","CIVIL")
        branch_combo.current(0)
        branch_combo.grid(row=3,column=1,padx=30,pady=10,sticky=W)


        # DOB
        Dob_label=Label(left_frame,text="Date Of Birth:",font=("verdana",12,"bold"),bg="white",fg="navyblue")
        Dob_label.grid(row=4,column=0,padx=40,pady=10,sticky=W)

        cal=DateEntry(left_frame,selectmode='day',width=23,textvariable=self.var_DOB,font=("verdana",12,"bold"))
        cal.grid(row=4,column=1,padx=30,pady=10)

        # Semester

        sem_label1=Label(left_frame,text="Semester: ",font=("verdana",12,"bold"),bg="white",fg="navyblue")
        sem_label1.grid(row=5,column=0,padx=40,pady=10,sticky=W)

        year_combo=ttk.Combobox(left_frame,textvariable=self.var_Semester,width=23,font=("verdana",12,"bold"),state="readonly")
        year_combo["values"]=("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6","Semester-7","Semester-8")
        year_combo.current(0)
        year_combo.grid(row=5,column=1,padx=30,pady=10,sticky=W)


        # #Gender
        student_gender_label = Label(left_frame,text="Gender:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_gender_label.grid(row=6,column=0,padx=40,pady=10,sticky=W)

        #combo box 
        gender_combo=ttk.Combobox(left_frame,textvariable=self.var_Gender,width=23,font=("verdana",12,"bold"),state="readonly")
        gender_combo["values"]=("Male","Female","Others")
        gender_combo.current(0)
        gender_combo.grid(row=6,column=1,padx=30,pady=10,sticky=W)



        # #Email
        student_email_label = Label(left_frame,text="Email Id:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_email_label.grid(row=7,column=0,padx=40,pady=5,sticky=W)

        student_email_entry = ttk.Entry(left_frame,textvariable=self.var_Email,width=25,font=("verdana",12,"bold"))
        student_email_entry.grid(row=7,column=1,padx=30,pady=10,sticky=W)

        # #Phone Number
        student_mob_label = Label(left_frame,text="Mobile No:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_mob_label.grid(row=8,column=0,padx=40,pady=10,sticky=W)

        student_mob_entry = ttk.Entry(left_frame,textvariable=self.var_Mobile,width=25,font=("verdana",12,"bold"))
        student_mob_entry.grid(row=8,column=1,padx=30,pady=10,sticky=W)


        # #Address
        student_address_label = Label(left_frame,text="Address:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_address_label.grid(row=9,column=0,padx=40,pady=10,sticky=W)

        student_address_entry = ttk.Entry(left_frame,textvariable=self.var_Address,width=25,font=("verdana",12,"bold"))
        student_address_entry.grid(row=9,column=1,padx=30,pady=10,sticky=W)






        #Button Frame
        btn_frame = Frame(left_frame,bd=0,bg="white",relief=RIDGE)
        btn_frame.place(x=0,y=475,width=610,height=40)

        #save button
        save_btn=Button(btn_frame,text="Save",cursor="hand2",command=self.add_data,width=15,font=("verdana",14,"bold"),fg="black",bg="#DC143C")
        save_btn.grid(row=0,column=0,sticky=W)

        #update button
        update_btn=Button(btn_frame,text="Update",cursor="hand2",command=self.update_data,width=15,font=("verdana",14,"bold"),fg="black",bg="#DC143C")
        update_btn.grid(row=0,column=1,sticky=W)

        #reset button
        reset_btn=Button(btn_frame,text="Reset",cursor="hand2",command=self.reset_data,width=15,font=("verdana",14,"bold"),fg="black",bg="#DC143C")
        reset_btn.grid(row=0,column=2,sticky=W)

        btn_frame1 = Frame(left_frame,bd=0,bg="white",cursor="hand2",relief=RIDGE)
        btn_frame1.place(x=0,y=515,width=700,height=40)

        #take photo button
        take_photo_btn=Button(btn_frame1,text="Take Pic",cursor="hand2",command=self.generate_dataset,width=23,font=("verdana",14,"bold"),fg="black",bg="#DC143C")
        take_photo_btn.grid(row=0,column=0,sticky=W)

        #delete button
        del_btn=Button(btn_frame1,text="Delete",cursor="hand2",command=self.delete_data,width=23,font=("verdana",14,"bold"),fg="black",bg="#DC143C")
        del_btn.grid(row=0,column=2,sticky=W)



# ======================Right Label Frame======================== 
# ===============================================================

        right_frame = LabelFrame(main_frame,bd=0,bg="white",relief=RIDGE,)
        right_frame.place(x=650,y=15,width=610,height=555)


  
        # -----------------------------Table Frame-------------------------------------------------
        #Table Frame 
        #Searching System in Right Label Frame 
        table_frame = Frame(right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=10,y=10,width=590,height=540)

        #scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame,column=("id","Name","Enroll","Branch","Dob","Sem","Gender","Email","Mobile","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("id",text="Student_id")
        self.student_table.heading("Name",text="Student Name")
        self.student_table.heading("Enroll",text="Enrollment No")
        self.student_table.heading("Branch",text="Branch Name")
        self.student_table.heading("Dob",text="Date of Birth")
        self.student_table.heading("Sem",text="Semeter")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("Email",text="Email Id")
        self.student_table.heading("Mobile",text="Mobile No")
        self.student_table.heading("Address",text="Address")
        self.student_table["show"]="headings"


        #         # Set Width of Colums 
        self.student_table.column("id",width=100)
        self.student_table.column("Name",width=200)   
        self.student_table.column("Enroll",width=100)
        self.student_table.column("Branch",width=100)
        self.student_table.column("Dob",width=100)
        self.student_table.column("Sem",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Mobile",width=100)
        self.student_table.column("Address",width=100)




        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

# ====callback function====
    def checkname(self,name):
        if name.isalpha():
            return True
        if name=='':
            return True
        else:
            messagebox.showerror('Invalid','Not Allowed',+name[-1],parent=self.root)


    def checkcontact(self,contact):
        if contact.isdigit():
            return True
        if len(str(contact))==0:
            return True
        else:
            messagebox.showerror("invalid","Invalid Entry",parent=self.root)



    def checkemail(self,email):
        if len(email)<=35:
            pattern = r'\b[19+-]+[be|BE+-]+[a-z|A-Z+-]+[0-999999+-]+@[vsitr.-]+\.[AC|ac.-]+\.[IN|in]{2,}\b'
            if re.fullmatch(pattern,email):
                return True
            else:
                messagebox.showerror("Alert",'invalide email enter valid email(Example:19bece54018@vsitr.ac.in',parent=self.root)
                return False
        else:
            messagebox.showerror("invalid",'Enter valid email',parent=self.root)
            return False

    


    def checkenroll(self,enroll):
        if len(enroll)<=30:
            pattern = r'\b[19+-]+[be|BE+-]+[a-z|A-Z+-]+[0-9+-]+[0-9+-]+[0-9+-]+[0-999+-]{2,}\b'
            if re.match(pattern,enroll):
                return True
            else:
                messagebox.showerror("Alert",'invalide enrollmrnt enter valid enrollment no(Example:19bece54018',parent=self.root)
                return False
        else:
            messagebox.showerror("invalid",'Enter valid Enrollment no',parent=self.root)
            return False



    def add_data(self):

        if self.var_id.get()=='':
            messagebox.showerror("Error","Please enter your Id",parent=self.root)
                
        elif self.var_Name.get()=='':
            messagebox.showerror("Error","Please enter your Name",parent=self.root)

        elif self.var_Enroll.get()=='':
            messagebox.showerror("Error","Please enter your valid Enrollment No",parent=self.root)
        
        elif self.var_Branch.get()=='Select Branch':
            messagebox.showerror("Error","Select your Branch",parent=self.root)

        elif self.var_DOB.get()=='Select Semester':
            messagebox.showerror("Error","Please enter your DOB",parent=self.root)
        elif self.var_Semester.get()=='':
            messagebox.showerror("Error","select your semester",parent=self.root)

      
        elif self.var_Gender.get()=='Select':
            messagebox.showerror("Error","Select Your Gender",parent=self.root)

        elif self.var_Email.get()=='':
            messagebox.showerror("Error","Enter your Email",parent=self.root)

        elif self.var_Mobile.get()=='' or len(self.var_Mobile.get())!=10:
            messagebox.showerror("Error","Please Enter valid Mobile no",parent=self.root)
        elif self.var_Address.get()=='':
            messagebox.showerror("Error","Please Enter your Address",parent=self.root)



        elif self.var_Email.get()!=None and self.var_Enroll.get()!=None:
            # self.checkname(self.var_Name.get())
            x=self.checkemail(self.var_Email.get())
            y=self.checkenroll(self.var_Enroll.get())

        if (x == True) and (y == True) :
            if self.var_Name.get()=='':   
                return        
          
            else:
                
                try:
                    conn = mysql.connector.connect(host='localhost',username='root', password='@Jk9649510979',database='studentdetail',port=7773)
                    mycursor = conn.cursor()
                    mycursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                self.var_id.get(),
                                self.var_Name.get(),
                                self.var_Enroll.get(),
                                self.var_Branch.get(),
                                self.var_DOB.get(),
                                self.var_Semester.get(),
                                self.var_Gender.get(),
                                self.var_Email.get(),
                                self.var_Mobile.get(),
                                self.var_Address.get()
                                
                    
                                                                                                                ))

                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success","All Records are Saved!",parent=self.root)
                except Exception as es:
                    messagebox.showerror("Error",f"Due To: {str(es)}",parent=self.root)
    
    def fetch_data(self):
            conn = mysql.connector.connect(host='localhost',username='root', password='@Jk9649510979',database='studentdetail',port=7773)
            mycursor = conn.cursor()

            mycursor.execute("select * from student")
            data=mycursor.fetchall()

            if len(data)!= 0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                    self.student_table.insert("",END,values=i)
            conn.commit()
            conn.close() 

        # ===============get cursor========
    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_id.set(data[0]),
        self.var_Name.set(data[1]),
        self.var_Enroll.set(data[2]),
        self.var_Branch.set(data[3]),
        self.var_DOB.set(data[4]),
        self.var_Semester.set(data[5]),
        self.var_Gender.set(data[6]),
        self.var_Email.set(data[7]),
        self.var_Mobile.set(data[8]),
        self.var_Address.set(data[9]),



# update data
    def update_data(self):
        if self.var_id.get()=='':
            messagebox.showerror("Error","Please enter your Id",parent=self.root)
                
        elif self.var_Name.get()=='':
            messagebox.showerror("Error","Please enter your Name",parent=self.root)

        elif self.var_Enroll.get()=='':
            messagebox.showerror("Error","Please enter your valid Enrollment No",parent=self.root)
        
        elif self.var_Branch.get()=='Select Branch':
            messagebox.showerror("Error","Select your Branch",parent=self.root)

        elif self.var_DOB.get()=='Select Semester':
            messagebox.showerror("Error","Please enter your DOB",parent=self.root)
        elif self.var_Semester.get()=='':
            messagebox.showerror("Error","select your semester",parent=self.root)

      
        elif self.var_Gender.get()=='Select':
            messagebox.showerror("Error","Select Your Gender",parent=self.root)

        elif self.var_Email.get()=='':
            messagebox.showerror("Error","Enter your Email",parent=self.root)

        elif self.var_Mobile.get()=='' or len(self.var_Mobile.get())!=10:
            messagebox.showerror("Error","Please Enter valid Mobile no",parent=self.root)
        elif self.var_Address.get()=='':
            messagebox.showerror("Error","Please Enter your Address",parent=self.root)



        elif self.var_Email.get()!=None and self.var_Enroll.get()!=None:
            # self.checkname(self.var_Name.get())
            x=self.checkemail(self.var_Email.get())
            y=self.checkenroll(self.var_Enroll.get())

        if (x == True) and (y == True) :
            if self.var_Name.get()=='':   
                return  
            else:
                try:
                    update=messagebox.askyesno("Update","Do you want to Update this Student Details!",parent=self.root)
                    if update>0:
                        conn = mysql.connector.connect(host='localhost',username='root', password='@Jk9649510979',database='studentdetail',port=7773)
                        mycursor = conn.cursor()
                        mycursor.execute("update student set Name=%s,EnrollmentNo=%s,Branch=%s,Dob=%s,Sem=%s,Gender=%s,Email=%s,Mobile=%s,Address=%s where Student_id=%s",(
                                    
                                    self.var_Name.get(),
                                    self.var_Enroll.get(),
                                    self.var_Branch.get(),
                                    self.var_DOB.get(),
                                    self.var_Semester.get(),
                                    self.var_Gender.get(),
                                    self.var_Email.get(),
                                    self.var_Mobile.get(),
                                    self.var_Address.get(),
                                    self.var_id.get()
                        
                                                        ))

                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success","All Records are Saved!",parent=self.root)
                except Exception as es:
                    messagebox.showerror("Error",f"Due To: {str(es)}",parent=self.root)


# delete data
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Student Id Must be Required!",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to Delete?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host='localhost',username='root', password='@Jk9649510979',database='studentdetail',port=7773)
                    mycursor = conn.cursor() 
                    sql="delete from student where Student_id=%s"
                    val=(self.var_id.get(),)
                    mycursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deleted!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)


    def reset_data(self):
                self.var_id.set(""),
                self.var_Name.set(""),
                self.var_Enroll.set(""),
                self.var_Branch.set("Select Branch"),
                self.var_Semester.set("Select Semester"),
                self.var_Gender.set("Male"),
                self.var_DOB.set(""),
                self.var_Email.set(""),
                self.var_Mobile.set(""),
                self.var_Address.set(""),



# data genrate video capture
    def generate_dataset(self):
        if self.var_Name.get()=="" or self.var_Enroll.get()=="" or self.var_Semester.get()=="Select Semester" or self.var_Branch.get()=="Select Branch"  or self.var_DOB.get()==" " or self.var_Gender.get()=="" or self.var_Email.get()=="" or self.var_Mobile.get()=="" or self.var_Address.get()==""  :
           messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            
            try:
                conn = mysql.connector.connect(host='localhost',username='root', password='@Jk9649510979',database='studentdetail',port=7773)
                mycursor = conn.cursor()
                mycursor.execute("select * from student")
                myresult=mycursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                    mycursor.execute("update student set Name=%s,EnrollmentNo=%s,Branch=%s,Dob=%s,Sem=%s,Gender=%s,Email=%s,Mobile=%s,Address=%s where Student_id=%s",(
                              
                                self.var_Name.get(),
                                self.var_Enroll.get(),
                                self.var_Branch.get(),
                                self.var_DOB.get(),
                                self.var_Semester.get(),
                                self.var_Gender.get(),
                                self.var_Email.get(),
                                self.var_Mobile.get(),
                                self.var_Address.get(),

                                self.var_id.get()==id+1
                                ))
                conn.commit()
                self.fetch_data()
                
                conn.close

# ==============load predifiend data ========

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_croped(img):
                    # conver gary sacle
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    #Scaling factor 1.3
                    # Minimum naber 5
                    for (x,y,w,h) in faces:
                        face_croped=img[y:y+h,x:x+w]
                        return face_croped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_croped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_croped(my_frame),(200,200))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="photodata/"+str(self.var_Name.get())+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)        
                        cv2.imshow("Capture Images",face)

                    if cv2.waitKey(1)==13 or int(img_id)==5:
                        break
                cap.release()
                cv2.destroyAllWindows()
                
                self.reset_data()
                messagebox.showinfo("Result","Genereting data set Completed!!!",parent=self.root)
            
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

                # file_name_path="photodata/"+str(self.var_Name.get())+".jpg"










if __name__ == "__main__":
    root = Tk()
    obj = Studentinfo(root)
    root.mainloop()        