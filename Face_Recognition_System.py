from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import re
from tkinter import ttk
import tkinter  as tk 
import os





class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1530x768+0+0")
        self.root.state('zoomed')
     


        # variables 
        self.var_ssq=StringVar()
        self.var_sa=StringVar()
        self.var_pwd=StringVar()



# ================================Background Image======================
        self.bg_image =Image.open(r'college_images\vista_styled_hd_background_by_jcsawyer_d25w0pz.jpg')
        photo=ImageTk.PhotoImage(self.bg_image)
        self.bg_image=self.bg_image.resize((1530,768),Image.Resampling.LANCZOS)
        self.bg_panel = Label(self.root,image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(expand='Yes')


# =====================Login Frame=================

        self.lgn_frame = Frame(self.root,bg='#040405',width='950',height=600)
        self.lgn_frame.place(x=310,y=100)

        self.txt ='WELCOME'
        self.heading = Label(self.lgn_frame,text=self.txt,font=('yu gothic ui',25,'bold'),bg='#040405',fg='white')
        self.heading.place(x=80,y=30,width=300,height=30)


# =============left side image=================

        self.side_image =Image.open(r'college_images\sideimage.png')
        photo=ImageTk.PhotoImage(self.side_image)
        self.side_panel = Label(self.lgn_frame,image=photo,bg='#040405')
        self.side_panel.image = photo
        self.side_panel.place(x=5,y=100)

        # =============sign in  image=================

        self.logoImage=Image.open(r'college_images\306473.png')
        self.logoImage=self.logoImage.resize((100,100),Image.Resampling.LANCZOS)
        photo012=ImageTk.PhotoImage(self.logoImage)

        self.logo=Label(self.lgn_frame,image=photo012,bg='#040405')
        self.logo.image=photo012
        self.logo.place(x=640,y=100,width=100,height=100)

        self.heading=Label(self.lgn_frame ,text='Sign In',font=("",20,"bold"),fg='white',bg='#040405')
        self.heading.place(x=640,y=210)

# ================Username======================
        self.username_laber=Label(self.lgn_frame,text='Email',bg='#040405',font=('yu gothic ui',13,'bold'),fg='#4f4e4d')
        self.username_laber.place(x=550,y=300)

        self.username_entry = Entry(self.lgn_frame,highlightthickness=0,relief=FLAT,bg='white',fg='black',
                                                font=('yu gothic ui',13,'bold'))

        self.username_entry.place(x=590,y=333,width=270)

        self.usename_line = Canvas(self.lgn_frame, width=308, height=2.0, bg='#bdb9b1',highlightthickness=0)
        self.usename_line.place(x=550,y=359)

# =============Username Icon==========

        self.username_icon=Image.open(r'college_images\usernamelogo-removebg-preview.png')
        self.username_icon=self.username_icon.resize((30,25),Image.Resampling.LANCZOS)
        photo012=ImageTk.PhotoImage(self.username_icon)

        self.icon_label=Label(self.lgn_frame,image=photo012,bg='#040405')
        self.icon_label.image=photo012
        self.icon_label.place(x=545,y=330)


        # ================password======================
        self.password_laber=Label(self.lgn_frame,text='Password',bg='#040405',font=('yu gothic ui',13,'bold'),fg='#4f4e4d')
        self.password_laber.place(x=550,y=380)

        self.password_entry =Entry(self.lgn_frame,highlightthickness=0,relief=FLAT,bg='white',fg='black',
                                                font=('yu gothic ui',13,'bold'),show='*')

        self.password_entry.place(x=590,y=414,width=270)

        self.password_line = Canvas(self.lgn_frame, width=308, height=2.0, bg='#bdb9b1',highlightthickness=0)
        self.password_line.place(x=550,y=440)

# =============password Icon==========

        self.password_icon=Image.open(r'college_images\passwordicon-removebg-preview.png')
        self.password_icon=self.password_icon.resize((35,30),Image.Resampling.LANCZOS)
        photo013=ImageTk.PhotoImage(self.password_icon)

        self.password_icon_label=Label(self.lgn_frame,image=photo013,bg='#040405')
        self.password_icon_label.image=photo013
        self.password_icon_label.place(x=545,y=405)


# =====================login buttton=========



        self.lgn_button_icon_label=Label(self.lgn_frame,bg='#3047ff')

        self.lgn_button_icon_label.place(x=550,y=460,width=300,height=40)


        self.lgn_button = Button(self.lgn_button_icon_label,command=self.login,text='LOGIN',font=('yu gothic ui',13,'bold'),width=30,bd=0,
                                         bg='#3047ff',cursor='hand2',activebackground='#3047ff',fg='white')
        self.lgn_button.place(x=0,y=0)
        

        # ==============forgot password=============
        self.forgot_button=Button(self.lgn_frame,command=self.forget_pwd,text='Forgpt Password ?',
                                    font=('yu gothic ui',13,'bold underline'),fg='white',width=25,bd=0,
                                     bg='#040405',cursor='hand2')
        self.forgot_button.place(x=580,y=510)    

# ==================sign up button==============

        self.signup_Label = Label(self.lgn_frame,text='No account yet?',font=('yu gothic ui',13,'bold'),
                                                        background='#040405',fg='white')   

        self.signup_Label.place(x=550,y=560)

        
        self.signup_label=Label(self.lgn_frame,bg='#3047ff')

        self.signup_label.place(x=690,y=555,width=100,height=30)

 
        self.signup_button = Button(self.signup_label,command=self.register_window,text='Sign Up Now',font=('yu gothic ui',10,'bold'),width=12,bd=0,
                                         bg='#3047ff',cursor='hand2',activebackground='#3047ff',fg='white')
        self.signup_button.place(x=0,y=0)




# ===========================show/hide password============
                
        self.show_image=Image.open(r'college_images\show.png')
        self.show_image=self.show_image.resize((30,30),Image.Resampling.LANCZOS)
        self.photo1 = ImageTk.PhotoImage(self.show_image)

        self.show_button= Button(self.lgn_frame,image=self.photo1,
                                         bg='white',cursor='hand2',activebackground='white',bd=0,command=self.show)
        
        self.show_button.image=self.photo1
        self.show_button.place(x=870,y=410)

        self.hide_image=Image.open(r'college_images\Hide.png')
        self.hide_image=self.hide_image.resize((30,30),Image.Resampling.LANCZOS)
        self.photo2 = ImageTk.PhotoImage(self.hide_image)


    def show(self): 
        self.hide_Button = Button(self.lgn_frame,image=self.photo2,
                                         bg='white',cursor='hand2',activebackground='white',bd=0,command=self.hide)
        self.hide_Button.image=self.photo2
        self.hide_Button.place(x=870,y=410)
        self.password_entry.config(show='')
    
    def hide(self):
        self.show_button= Button(self.lgn_frame,image=self.photo1,
                                         bg='white',cursor='hand2',activebackground='white',bd=0,command=self.show)
        
        self.show_button.image=self.photo1
        self.show_button.place(x=870,y=410)
        self.password_entry.config(show='*')

    def register_window(self):
        self.root.destroy()
        import Register

# ==============RegisterButton=======


    def login(self):
        if (self.username_entry.get()=="" or self.password_entry.get()==""):
            messagebox.showerror("Error","All Field Required!")
        elif(self.username_entry.get()=="admin" and self.password_entry.get()=="admin"):
            messagebox.showinfo("Sussessfully","Welcome to Attendance Managment System Using Facial Recognition")
        else:
            # messagebox.showerror("Error","Please Check Username or Password !")
            conn = mysql.connector.connect(host='localhost',username='root', password='@Jk9649510979',database='studentdetail',port=7773)
            mycursor = conn.cursor()
            mycursor.execute("select * from register where email=%s and pwd=%s",(
                self.username_entry.get(),
                self.password_entry.get()
            ))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and Password!",parent= self.root)
            else:
                self.root.destroy()
                import Home
              


            # conn.commit()
            conn.close()
#=======================Reset Passowrd Function=============================
    def reset_pass(self):
        if self.var_ssq.get()=="Select":
            messagebox.showerror("Error","Select the Security Question!",parent=self.root2)
        elif(self.var_sa.get()==""):
            messagebox.showerror("Error","Please Enter the Answer!",parent=self.root2)
        elif(self.var_pwd.get()==""):
            messagebox.showerror("Error","Please Enter the New Password!",parent=self.root2)
        else:
            conn = mysql.connector.connect(host='localhost',username='root', password='@Jk9649510979',database='studentdetail',port=7773)
            mycursor = conn.cursor()
            query=("select * from register where email=%s and ssq=%s and sa=%s")
            value=(self.username_entry.get(),self.var_ssq.get(),self.var_sa.get())
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter the Correct Answer!",parent=self.root2)
            else:
                query=("update register set pwd=%s where email=%s")
                value=(self.var_pwd.get(),self.username_entry.get())
                mycursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Successfully Your password has been rest, Please login with new Password!",parent=self.root2)
                



# =====================Forget window=========================================
    def forget_pwd(self):
        if self.username_entry.get()=="":
            messagebox.showerror("Error","Please Enter the Email ID to reset Password!")
        else:
            conn = mysql.connector.connect(host='localhost',username='root', password='@Jk9649510979',database='studentdetail',port=7773)
            mycursor = conn.cursor()
            query=("select * from register where email=%s")
            value=(self.username_entry.get(),)
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            # print(row)

            if row==None:
                messagebox.showerror("Error","Please Enter the Valid Email ID!")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("400x400+610+170")
                l=Label(self.root2,text="Forget Password",font=("times new roman",30,"bold"),fg="#002B53",bg="#fff")
                l.place(x=0,y=10,relwidth=1)
                # -------------------fields-------------------
                #label1 
                ssq =lb1= Label(self.root2,text="Select Security Question:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                ssq.place(x=70,y=80)

                #Combo Box1
                self.combo_security = ttk.Combobox(self.root2,textvariable=self.var_ssq,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security["values"]=("Select","Your Date of Birth","Your Nick Name","Your Favorite Book")
                self.combo_security.current(0)
                self.combo_security.place(x=70,y=110,width=270)


                #label2 
                sa =lb1= Label(self.root2,text="Security Answer:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                sa.place(x=70,y=150)

                #entry2 
                self.txtpwd=ttk.Entry(self.root2,textvariable=self.var_sa,font=("times new roman",15,"bold"))
                self.txtpwd.place(x=70,y=180,width=270)

                #label2 
                new_pwd =lb1= Label(self.root2,text="New Password:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                new_pwd.place(x=70,y=220)

                #entry2 
                self.new_pwd=ttk.Entry(self.root2,textvariable=self.var_pwd,font=("times new roman",15,"bold"))
                self.new_pwd.place(x=70,y=250,width=270)

                # Creating Button New Password
                loginbtn=Button(self.root2,command=self.reset_pass,text="Reset Password",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
                loginbtn.place(x=70,y=300,width=270,height=35)



root = Tk()
obj = Login(root)
root.mainloop()