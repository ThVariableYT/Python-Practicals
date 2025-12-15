# open the sample file used 
file = open('story.txt') 
  
# read the content of the file opened 
content = file.readlines()

  
# read 5th line from the file 
print("5th line") 
print(content[4]) 
  
# print 2nd and 3rd lines of file 
print("two lines") 
print(content[1:3]) 
