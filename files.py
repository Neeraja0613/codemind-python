f = open("names.txt", "r")

# f = open("abcd.txt", "r")  --> GIVES ERROR

# strings = f.readlines()
# new_strings= [i.strip('\n') for i in strings]
# print(new_strings)

strings = list(map(lambda x: x.strip('\n'), f.readlines()))
print(strings)
f.close()
