#• Write a Python program to count the number of lines in a text file
file=open("demo.txt")
a=file.readlines()
print(len(a))
file.close()
