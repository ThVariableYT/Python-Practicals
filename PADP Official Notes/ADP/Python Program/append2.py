file1 = open("myfile.txt", "a")  # append mode
#print(file1.tell())
#file1.seek(0)
file1.write("Today \n")
file1.close()
