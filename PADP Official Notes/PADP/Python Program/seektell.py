f = open("story.txt", "r") 
# Second parameter is by default 0  sets Reference point to twentieth .index position from
#the beginning 
f.seek(20) 
# prints current postion 
print(f.tell()) 
print(f.readline())
print(f.tell())
f.close() 
