# Creating Execuatable File of the code
from cx_Freeze import setup, Executable

setup(executables=[Executable("myCode.py")])    # give the path of file to make it Executable
