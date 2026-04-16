# How to open, read, and write to files
# Open the file
with open("my_file.txt") as file:
    # Read the file
    contents = file.read()
    print(contents)

# using the 'with', will auto close at end
#file.close()

# Writing to the file
# 'w' mode overrites the file
# 'a' mode appends to the file.
with open("my_file.txt", mode="a") as file:
    file.write("\nNew text.")

# When a file doesn't exist, this will creat a new one.
with open("new_file.txt", mode="w") as file:
    file.write("\nNew text.")