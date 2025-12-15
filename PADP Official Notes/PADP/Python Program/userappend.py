fname = input("Enter file name: ")
file=open(fname,"a")
c=input("Enter string to append: \n");
file.write(c)
file.close()
print("Contents of appended file:");
file1=open(fname,'r')
print(file1.readlines())   
file1.close()
