def fun(*strings):
    output_string =""
    for i in strings:
        output_string+=i[0]
    return output_string
    print()

print(fun("abc"))
print(fun("abc","xyz"))
print(fun("abc","xyz","pqr"))
print(fun("abc","xyz","pqr","stu"))
