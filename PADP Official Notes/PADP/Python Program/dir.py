


import os
import shutil
os.mkdir("test")
print("New Directory created")
print("Path ",os.getcwd())
print(os.listdir())
os.renames("test","C:/Users/Vishakha/Desktop/VISHAKHA/VB PD/PP/ntest")
os.chdir("C:/Users/Vishakha/Desktop/")
print(os.listdir())


shutil.rmtree("C:/Users/Vishakha/Desktop/VISHAKHA/VB PD/PP/ntest")
#os.listdir()
print("Folder removed")
