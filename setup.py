import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Python310\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Python310\tcl\tk8.6"

executables = [cx_Freeze.Executable("Face_Recognition_System.py", base=base, icon="face_recognition-icon.ico")]


cx_Freeze.setup(
    name = "Facial Recognition Software",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["face_recognition-icon.ico",'tcl86t.dll','tk86t.dll', 'college_images','photodata','database','attendance.csv','haarcascade_frontalface_default.xml','Home.py','AddStudent.py','Register.py']}},
    version = "1.0",
    description = "Face Recognition Automatic Attendace System",
    executables = executables
    )
