# Step 1: Create and write a story
with open("story.txt", "w") as f:
    f.write("The Honest Woodcutter\n")
    f.write("Once upon a time, there lived a poor woodcutter.\n")
    f.write("He was very honest and kind.\n")
    f.write("One day, his axe fell into the river.\n")
    
# Step 2: Display the name of the file and the mode    
f = open("story.txt", "r")
print("File name:", f.name)
print("File mode:", f.mode)
f.close()

# Step 3: Append a Moral at the end of the file
with open("story.txt", "a") as f:
    f.write("Moral: Honesty is always rewarded.\n")
    
# Step 4: Display the story line by line    
with open("story.txt", "r") as f:
    print("\nStory content:")
    for line in f:
        print(line.strip())
        
# Step 5: Retrieve the position of the line where Moral starts
with open("story.txt", "r") as f:
    position = 0
    for line in f:
        if line.startswith("Moral"):
            break
        position += 1

print("Moral starts at line number:", position + 1)

# Step 6: Rename the file to the name of the story
import os

os.rename("story.txt", "The_Honest_Woodcutter.txt")

# Step 7: Delete the contents of the file
open("The_Honest_Woodcutter.txt", "w").close()

# Step 8: Delete the file
os.remove("The_Honest_Woodcutter.txt")
print("File deleted successfully")
