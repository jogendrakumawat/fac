from logging import root
from email.mime import image
from logging import root
from PIL import Image,ImageTk
import re
from time import sleep
from tkinter import*
import tkinter
import tkinter
from turtle import title, width
from PIL import Image,ImageTk
import cv2
import mysql.connector
import os
from tkinter import messagebox
import numpy as np
from Addstudent import Studentinfo
from tkinter import font
import time
import datetime
from datetime import datetime, timedelta
from time import strftime
import tkinter  as tk
from tkinter import Message, Text
import pandas as pd
import face_recognition as face_rec
import numpy as np
from datetime import datetime
from imutils.video import VideoStream

import time

import imutils
import numpy as np







class Dashboard:
    def __init__(self,window):
        self.window= window
        self.window.title("Face Recognition Attendance  System")
        self.window.geometry('1366x700')
        self.window.state('zoomed')
        # self.window.resizable(0,600)
        self.window.config(background='#CDCDC0')
        #window Iconeff5f6
        icon = PhotoImage(file='college_images\icon.png')
        

        




        # ===============HEADER===========
        self.header =Frame(self.window,bg='#9400D3')
        self.header.place(x=250,y=0,width=1300,height=80)

        


        self.headerimg=Image.open(r'college_images\360_F_408791486_sc9aKN6ATz06tiSYIC4VfwaSX7ErPnP7-removebg-preview.png')
        self.headerimg=self.headerimg.resize((125,80),Image.Resampling.LANCZOS)
        photo011=ImageTk.PhotoImage(self.headerimg)

        self.logo=Label(self.header,image=photo011,bg='#9400D3')
        self.logo.image=photo011
        self.logo.place(x=0,y=0,width=100,height=80)

        self.heading=Label(self.header ,text='Face Recognition Attendance System',font=("",20,"bold"),fg='#F0F8FF',bg='#9400D3')
        self.heading.place(x=100,y=25)


        




        # ======SideBar==========
        self.sidebar=Frame(self.window,bg='#FFFFEF')
        self.sidebar.place(x=0,y=0, width=250,height=795)


        self.logoImage=Image.open('college_images\clocktime-logo-icon-illustration-design-vector-template_598213-2171-removebg-preview (2).png')
        self.logoImage=self.logoImage.resize((150,120),Image.Resampling.LANCZOS)
        photo012=ImageTk.PhotoImage(self.logoImage)

        self.logo=Label(self.sidebar,image=photo012,bg='#ffffff')
        self.logo.image=photo012
        self.logo.place(x=50,y=500,width=150,height=100)

        def my_time():
            time_string = strftime('%H:%M:%S %p \n %A \n %x') # time format 
            l1.config(text=time_string)
            l1.after(1000,my_time) # time delay of 1000 milliseconds 
            
        my_font=('times',30,'bold') # display size and style

        l1=tk.Label(self.sidebar,font=my_font,bg='#ffffff')
        l1.place(x=10,y=600)

        my_time()

        # # Logo=======
        self.logoImage=Image.open('college_images\icon.png')
        self.logoImage=self.logoImage.resize((150,100),Image.Resampling.LANCZOS)
        photo012=ImageTk.PhotoImage(self.logoImage)

        self.logo=Label(self.sidebar,image=photo012,bg='#ffffff')
        self.logo.image=photo012
        self.logo.place(x=50,y=70,width=150,height=100)

        self.heading=Label(self.sidebar ,text='Face Recognition',font=("",15,"bold"),fg='#000000',bg='#ffffff')
        self.heading.place(x=40,y=170)











# =================Dashboard Button===============
        self.dashimg=Image.open(r'college_images\Dashboard1-removebg-preview.png')
        self.dashimg=self.dashimg.resize((35,35),Image.Resampling.LANCZOS)
        photo01=ImageTk.PhotoImage(self.dashimg)

        self.logo=Label(self.sidebar,image=photo01,bg='#ffffff')
        self.logo.image=photo01
        self.logo.place(x=35,y=300,width=30,height=35)

        manage_button = Button(self.sidebar, text='Dashboard', bg='#DC143C', font=("", 13, "bold"), bd=0, fg='#000000',
                               cursor='hand2', activebackground='#DC143C', activeforeground='#ffffff')
        manage_button.place(x=80, y=300)

# ================Photo Button====================
        self.photoimg=Image.open(r'college_images\images-removebg-preview.png')
        self.photoimg=self.photoimg.resize((30,30),Image.Resampling.LANCZOS)
        photophto=ImageTk.PhotoImage(self.photoimg)

        self.photo=Label(self.sidebar,image=photophto,bg='#ffffff')
        self.photo.image=photophto
        self.photo.place(x=35,y=350,width=30,height=30)
        

        manage_button = Button(self.sidebar,command=self.open_img, text='Photo', bg='#ffffff', font=("", 13, "bold"), bd=0, fg='#000000',
                               cursor='hand2', activebackground='#fd6a36', activeforeground='#ffffff')
        manage_button.place(x=80, y=350)





        



        # ======BODY====


# =====Body frame1===
        self.bodyframe1= Frame(self.window,bg='#9400D3')
        self.bodyframe1.place(x=270,y=105,width=1245,height=665)





# detect Face
        self.detectImage=Image.open(r'college_images\facereco.png')
        self.detectImage=self.detectImage.resize((200,200),Image.Resampling.LANCZOS)
        photo1=ImageTk.PhotoImage(self.detectImage)

        self.logo=Button(self.bodyframe1,command=self.face_recog,image=photo1,cursor="hand2",bd=0,bg='#9400D3',activebackground='#9400D3', activeforeground='#9400D3')
        self.logo.image=photo1
        self.logo.place(x=300,y=80,width=200,height=200)

        b2_1= Button(self.bodyframe1,text="Face Detector",command=self.face_recog,cursor='hand2',font=("time new roman",15, "bold"),bg="darkblue",fg="white")
        b2_1.place(x=300,y=280,width=200,height=40)


 # Attendace button
        self.attendImage=Image.open(r'college_images\attendance.png')
        self.attendImage=self.attendImage.resize((210,200),Image.Resampling.LANCZOS)
        photo2=ImageTk.PhotoImage(self.attendImage)

        self.attend=Button(self.bodyframe1,command=self.open_attend,image=photo2,cursor="hand2",bd=0,bg='#9400D3',activebackground='#9400D3', activeforeground='#9400D3')
        self.attend.image=photo2
        self.attend.place(x=800,y=80,width=200,height=200)

        b3_1= Button(self.bodyframe1,text="Attendance",command=self.open_attend,cursor='hand2',font=("time new roman",15, "bold"),bg="darkblue",fg="white")
        b3_1.place(x=800,y=280,width=200,height=40)


# Student Button

        self.addimg=Image.open(r'college_images\Add.png')
        self.addimg=self.addimg.resize((200,200),Image.Resampling.LANCZOS)
        photo3=ImageTk.PhotoImage(self.addimg)

        self.add=Button(self.bodyframe1,command=self.student_detail,image=photo3,cursor="hand2",bd=0,bg='#9400D3',activebackground='#9400D3', activeforeground='#9400D3')
        self.add.image=photo3
        self.add.place(x=300,y=400,width=200,height=200)

        b1_1= Button(self.bodyframe1,text="ADD STUDENT",command=self.student_detail,cursor='hand2',font=("time new roman",15, "bold"),bg="darkblue",fg="white")
        b1_1.place(x=300,y=600,width=200,height=40)





# Exit
        self.exitimg=Image.open(r'college_images\exit.png')
        self.exitimg=self.exitimg.resize((210,200),Image.Resampling.LANCZOS)
        photo4=ImageTk.PhotoImage(self.exitimg)

        self.exit=Button(self.bodyframe1,command=self.iExit,image=photo4,cursor="hand2",bd=0,bg='#9400D3',activebackground='#9400D3', activeforeground='#9400D3')
        self.exit.image=photo4
        self.exit.place(x=800,y=400,width=200,height=200)

        b4_1= Button(self.bodyframe1,command=self.iExit,text="Exit",cursor='hand2',font=("time new roman",15, "bold"),bg="darkblue",fg="white")
        b4_1.place(x=800,y=600,width=200,height=40)




    #=====================Attendance===================



# =============face recognition=======
    def face_recog(self):
        path = 'photodata'
        studentImg = []
        studentName = []
        myList = os.listdir(path)
        for cl in myList :
            curimg = cv2.imread(f'{path}/{cl}')
            studentImg.append(curimg)
            studentName.append(os.path.splitext(cl)[0])

        def findEncoding(images) :
            imgEncodings = []
            for img in images :
                # img = resize(img, 0.50)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                encodeimg = face_rec.face_encodings(img)[0]
                imgEncodings.append(encodeimg)
            return imgEncodings

        def mark_attendance(name):
            with open("attendance.csv","r+",newline="\n") as f:
                myDatalist=f.readlines()
                name_list=[]
                for line in myDatalist:
                    entry=line.split((","))
                    name_list.append(entry[0])

                if((name not in name_list)):
                    now=datetime.now()
                    d1=now.strftime("%d/%m/%Y")
                    dtString=now.strftime("%H:%M:%S")
                    f.writelines(f"\n{name}, {dtString}, {d1}, Present")


        EncodeList = findEncoding(studentImg)
        

        capture = cv2.VideoCapture(0)

        while(True):
            ret,frame=capture.read()
            Smaller_frames = cv2.resize(frame, (0,0), None, 0.25, 0.25)
            # Smaller_frames=cv2.cvtColor(Smaller_frames,cv2.COLOR_BGR2RGB)

            facesInFrame = face_rec.face_locations(Smaller_frames)
            encodeFacesInFrame = face_rec.face_encodings(Smaller_frames, facesInFrame)

            for encodeFace, faceloc in zip(encodeFacesInFrame, facesInFrame) :
                    matches = face_rec.compare_faces(EncodeList, encodeFace)
                    facedis = face_rec.face_distance(EncodeList, encodeFace)
                
                    matchIndex = np.argmin(facedis)

                    if matches[matchIndex] :
                        name = studentName[matchIndex].upper()
                        y1, x2, y2, x1 = faceloc
                        y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)
                        cv2.rectangle(frame, (x1, y2-25), (x2, y2), (0, 255, 0), cv2.FILLED)
                        cv2.putText(frame, name, (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                        mark_attendance(name)
                    else:
                        y1, x2, y2, x1 = faceloc
                        y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)
                        cv2.rectangle(frame, (x1, y2-25), (x2, y2), (0, 255, 0), cv2.FILLED)
                        cv2.putText(frame,"Unknown Face",(x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            
            cv2.imshow('capture',frame)

            if cv2.waitKey(1) == 13:
                break
        capture.release()
        cv2.destroyAllWindows()




#  =========function Button=========


    def open_attend(self):
        os.startfile("attendance.csv")
    
    def open_img(self):
        os.startfile("photodata")




    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition", "Are you sure exit this Page", parent =self.window)
        if self.iExit>0:
                self.window.destroy()
        else:
                return

   
    def student_detail(self):
        self.new_window=Toplevel(self.window)
        self.app=Studentinfo(self.new_window)










window=Tk()
obj =Dashboard(window)
window.mainloop()

    



          