# Opening the file
# open("file_path", "mode")
# only when file that you want to open
# and source file are in the same folder
# open("file_name", "mode")

f = open("example.txt", "r")
#content = f.read()  # a string
#print(content)

# List of strings where each string
# is each line in the text file
# contents = f.readlines()
# print(contents)

string=f.read()
nums=list(map(int, string.split()))
print(sum(nums))
f.close() 
