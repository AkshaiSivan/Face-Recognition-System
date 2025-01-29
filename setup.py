import cx_Freeze
import sys
import os

base = None

# to get the Tcl library path
#from tkinter import Tcl
#print(Tcl().eval("info library"))
#

if sys.platform == 'win32':
    base = "Win32GUI"

# Ensure the paths to Tcl and Tk libraries are correctly set
os.environ['TCL_LIBRARY'] = r"C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0\tcl\tk8.6"

executables = [cx_Freeze.Executable("main_window.py", base=base, icon="appicon.ico")]

cx_Freeze.setup(
    name="Face Recognition System",
    version="17.0",  # Update the version number as needed
    description="Visitor Management System for Gated Communities Using Python and Computer Vision",
    options={
        "build_exe": {
            "packages": ["tkinter", "os", "mysql.connector"],  # Include necessary packages
            "includes": ["mysql.connector._version"],  # Add _version to includes
            "include_files": [
                "appicon.ico",  # Include application icon
                'tcl86t.dll',  # Include the Tcl DLL
                'tk86t.dll',  # Include the Tk DLL
                'appImages',  # Include application images folder
                'img_data',  # Include image data folder
                'appDatabase',  # Include database folder
                '.env', # Include database creds
                'haarcascade_frontalface_default.xml'
            ]
        }
    },
    executables=executables
)
