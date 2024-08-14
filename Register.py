from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import re
from tkinter import ttk
import tkinter  as tk 
import os
# from Home import Dashboard

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1530x768+0+0")
        self.root.state('zoomed')

        

        # ============ Variables =================
        self.var_fname=StringVar()
        self.var_Enroll=StringVar()
        self.var_cnum=StringVar()
        self.var_email=StringVar()
        self.var_ssq=StringVar()
        self.var_sa=StringVar()
        self.var_pwd=StringVar()
        self.var_cpwd=StringVar()
        self.var_check=IntVar()

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\JOGENDRA\Desktop\Face Attendance\college_images\images-removebg-preview.png")
        
        lb1_bg=Label(self.root,image=self.bg)
        lb1_bg.place(x=0,y=0, relwidth=1,relheight=1)

        frame= Frame(self.root,bg="#F2F2F2")
        frame.place(x=300,y=80,width=900,height=580)
        


         
        get_str = Label(frame,text="Registration",font=("times new roman",30,"bold"),fg="#002B53",bg="#F2F2F2")
        get_str.place(x=350,y=110)


        sframe= Frame(frame,bg="#F2F2F2")
        sframe.place(x=10,y=175,width=880,height=275)  

        Name = Label(sframe,text="First Name:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        Name.grid(row=0,column=0,padx=87,pady=5,sticky=W)
        username_entry=ttk.Entry(sframe,textvariable=self.var_fname,width=27,font=("times new roman",15,"bold"))
        username_entry.grid(row=1,column=0,padx=87,pady=0,sticky=W)

        # callback and validation register
        validate_name=self.root.register(self.checkname)
        username_entry.config(validate='key',validatecommand=(validate_name,'%P'))

        lastname = Label(sframe,text="Last Name:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        lastname.grid(row=2,column=0,padx=87,pady=5,sticky=W)
        lastname_entry=ttk.Entry(sframe,textvariable=self.var_Enroll,width=27,font=("times new roman",15,"bold"))
        lastname_entry.grid(row=3,column=0,padx=87,pady=0,sticky=W)

        Question = Label(sframe,text="Select Security Question:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        Question.grid(row=4,column=0,padx=87,pady=5,sticky=W)
        self.combo_security = ttk.Combobox(sframe,textvariable=self.var_ssq,font=("times new roman",15,"bold"),width=25,state="readonly")
        self.combo_security["values"]=("Select","Your Date of Birth","Your Nick Name","Your Favorite Book")
        self.combo_security.current(0)
        self.combo_security.grid(row=5,column=0,padx=87,pady=0)

        Answer = Label(sframe,text="Question Answer:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        Answer.grid(row=6,column=0,padx=87,pady=5,sticky=W)
        Answer_entry=ttk.Entry(sframe,textvariable=self.var_sa,width=27,font=("times new roman",15,"bold"))
        Answer_entry.grid(row=7,column=0,padx=87,pady=0,sticky=W)




        contact = Label(sframe,text="Contact No:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        contact.grid(row=0,column=1,padx=60,pady=5,sticky=W)
        contact_entry=ttk.Entry(sframe,textvariable=self.var_cnum,width=27,font=("times new roman",15,"bold"))
        contact_entry.grid(row=1,column=1,padx=60,pady=0,sticky=W)

         # callback and validation register
        validate_contact=self.root.register(self.checkcontact)
        contact_entry.config(validate='key',validatecommand=(validate_contact,'%P'))


        Email = Label(sframe,text="Email:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        Email.grid(row=2,column=1,padx=60,pady=5,sticky=W)
        Email_entry=ttk.Entry(sframe,textvariable=self.var_email,width=27,font=("times new roman",15,"bold"))
        Email_entry.grid(row=3,column=1,padx=60,pady=0,sticky=W)

        password = Label(sframe,text="Password:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        password.grid(row=4,column=1,padx=60,pady=5,sticky=W)
        password_entry=ttk.Entry(sframe,textvariable=self.var_pwd,width=27,font=("times new roman",15,"bold"))
        password_entry.grid(row=5,column=1,padx=60,pady=0,sticky=W)

        Cpassword= Label(sframe,text="Confirm Password:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        Cpassword.grid(row=6,column=1,padx=60,pady=5,sticky=W)
        Cpassword_entry=ttk.Entry(sframe,textvariable=self.var_cpwd,width=27,font=("times new roman",15,"bold"))
        Cpassword_entry.grid(row=7,column=1,padx=60,pady=0,sticky=W)

        

        checkframe= Frame(frame,bg="#F2F2F2")
        checkframe.place(x=100,y=450,width=270,height=58)

        checkbtn = Checkbutton(checkframe,variable=self.var_check,text="Agree the Terms & Conditions",font=("times new roman",13,"bold"),fg="#002B53",bg="#F2F2F2",onvalue=1,offvalue=0)
        checkbtn.grid(row=0,column=0,padx=0,sticky=W)

        self.check_lbl=Label(checkframe,text='',font=("arial",10),fg="red")
        self.check_lbl.grid(row=1,column=0,padx=10,sticky=W)

        # Creating Button Register
        Registerbtn=Button(frame,command=self.reg,text="Register",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
        Registerbtn.place(x=100,y=510,width=270,height=35)

        Loginbtn=Button(frame,command=self.login_window,text="Login",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
        Loginbtn.place(x=525,y=510,width=270,height=35)
    
    def login_window(self):
        self.root.destroy()
        import Face_Recognition_System


        


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
        if len(email)<=30:
            pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            if re.match(pattern,email):
                return True
            else:
                messagebox.showerror("Alert",'invalide email enter valid email',parent=self.root)
                return False
        else:
            messagebox.showerror("invalid",'Enter valid email',parent=self.root)
            return False

    
    def checkpass(self,password):

        msg = ""

        if len(password) == 0:
            msg = 'Password can\'t be empty'
        else:
            try:
                special_ch = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', '\\', '/', ':', ';', '"', "'", '<', '>', ',', '.', '?']
                if not any(ch in special_ch for ch in password):
                    messagebox.showerror("Alert",'Atleast 1 special character required!')
                elif not any(ch.isupper() for ch in password):
                    messagebox.showerror("Alert",'Atleast 1 uppercase character required!')
                elif not any(ch.islower() for ch in password):
                    messagebox.showerror("Alert",'Atleast 1 lowercase character required!')
                elif not any(ch.isdigit() for ch in password):
                   messagebox.showerror("Alert",'Atleast 1 number required!')
                elif len(password) < 8:
                    messagebox.showerror("Alert",'Password must be minimum of 8 characters!')
                else:
                    return True
            except Exception as ep:
                messagebox.showerror('error', ep,parent= self.root)
        messagebox.showinfo('message', msg,parent=self.root)







    def reg(self):
        if self.var_fname.get()=='':
            messagebox.showerror("Error","Please enter your name",parent=self.root)
        
        

        elif self.var_Enroll.get()=='':
            messagebox.showerror("Error","Please enter your Enrollment No",parent=self.root)

        elif self.var_cnum.get()=='' or len(self.var_cnum.get())!=10:
            messagebox.showerror("Error","Please enter your valid contact no",parent=self.root)
        
        elif self.var_email.get()=='':
            messagebox.showerror("Error","Please enter your Email Id",parent=self.root)

        elif self.var_pwd.get()=='':
            messagebox.showerror("Error","Please enter your Password",parent=self.root)
        elif self.var_cpwd.get()=='':
            messagebox.showerror("Error","Please enter your Confirm Password",parent=self.root)

      
        elif self.var_ssq.get()=='Select':
            messagebox.showerror("Error","Please Select Security Question",parent=self.root)

        elif self.var_sa.get()=='':
            messagebox.showerror("Error","Please enter Security Answer",parent=self.root)

        elif(self.var_pwd.get() != self.var_cpwd.get()):
            messagebox.showerror("Error","Please Enter Password & Confirm Password are Same!",parent=self.root)


        elif self.var_email.get()!=None and self.var_pwd.get()!=None:
            x= self.checkemail(self.var_email.get())
            y= self.checkpass(self.var_pwd.get())
        

        if (x == True) and (y == True) :
            if self.var_check.get()==0:
                self.check_lbl.config(text='Please Agree the Terms & Conditions',fg='red')
                  
            else:
                self.check_lbl.config(text='checked',fg='green')
            
                try:
                    conn = mysql.connector.connect(host='localhost',username='root', password='@Jk9649510979',database='studentdetail',port=7773)
                    mycursor = conn.cursor()
                    mycursor1 = conn.cursor()
                    query=("select * from register where email=%s")
                    value=(self.var_email.get(),)
                    mycursor.execute(query,value)
                    row=mycursor.fetchone()
                  
                    if row!=None:
                        messagebox.showerror("Error","User already exist,please try another email",parent=self.root)
                  
                    else:
                        mycursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                        self.var_fname.get(),
                        self.var_Enroll.get(),
                        self.var_cnum.get(),
                        self.var_email.get(),
                        self.var_ssq.get(),
                        self.var_sa.get(),
                        self.var_pwd.get()
                        ))
                        self.root.destroy()
                        import Home
                        conn.commit()
                        conn.close()

                except Exception as es:
                    messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

           

root = Tk()
obj = Register(root)
root.mainloop()   