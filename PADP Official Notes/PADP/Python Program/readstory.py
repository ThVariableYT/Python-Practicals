# Open a file
fo = open("story.txt", "r")
#str = fo.read();
#print ("Read String is : ", str)
# Close opend file
#print(fo.readlines())
print(fo.readline())
print(fo.readline(9))
fo.close()
