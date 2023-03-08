# age = input("enter your age:")
# fp = open('data.txt', 'w')
# fp.write(age)
# fp.close()


# fp = open('data.txt', 'r')
# print(fp.read())
# fp.close()

# f = open("data.txt", 'r', buffering=10 )
# if f:
#     print("create")
# print(f)

# ******* File object  ***************

# f = open("data.txt", 'r', buffering=10)
# fp = f.name
# m = f.mode
# e = f.encoding
# c = f.closed
# print("file name is", fp)
# print("file mode is", m)
# print("file encoding is", e)
# print("file is close or not", c)
"""
 reading data from file
1. read()
2. readline()
3.readlines()
 """
#read()
# f = open("data.txt", 'r')
# fp = f.read(15)
# p = f.read(5)
# print(fp)
# print(p)
# f.close()

#readline()
# f =  open("data.txt",'r')
# fp = f.readline()
# #print("here")
# print(fp)
# f.close()

#readlines()
# with open("data.txt", 'r') as foo:
#     f = foo.readlines()
#     for line in f:
#         print(line, end="")

# read data with for loop#
# with open("data.txt", 'r') as foo:
#     #print(list(foo))
#     for line in foo:
#          print(line, end="")

'''
 file method
 1) tell()  - used to find the current position of file pointer from beginning position start with 0
 2) seek () - used to change the position of file pointer
'''

# with open("data.txt",'r') as foo:
#     foo.readline()
#     print(foo.tell())
#     print(foo.read(5))
#     print(foo.tell())

with open("data.txt",'r') as foo:
    print(foo.tell())
    print(foo.read(10))
    print(foo.tell())
    print(foo.seek(6))
    print(foo.read(5))

'''
Find Number of characters,words and lines in File
'''
#
# with open("data.txt") as foo:
#     number_of_words = 0
#     number_of_charcters = 0
#     number_of_lines = 0
#     for line in foo:
#         number_of_lines +=1
#         lines =line.strip("\n")
#
#
#         words = line.split()
#         number_of_words += len(words)
#
#         number_of_charcters += len(line)
#
#     print(number_of_lines)
#     print(number_of_words)
#     print(number_of_charcters)



