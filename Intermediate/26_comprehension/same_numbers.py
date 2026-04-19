with open("file1.txt") as f1:
    contents_1 = f1.read().splitlines()
print(contents_1)

with open("file2.txt") as f2:
    contents_2 = f2.read().splitlines()
print(contents_2)

result = [int(x) for x in contents_1 if x in contents_2]

print(result)