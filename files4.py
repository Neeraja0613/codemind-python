# File in write mode
f = open("abcd.txt", "w")
f.write("Hello, I wrote this from a python program")
f.writelines(["\nPython\n", "Programming\n", "Language\n"])
f.close()
