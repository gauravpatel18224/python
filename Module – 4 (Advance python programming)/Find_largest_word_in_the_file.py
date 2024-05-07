#• Write a python program to find the longest words
file=open("demo.txt")
a=file.read()
a=a.split()
m=a[0]
for i in a:
    if len(i)>len(m):
        m=i
print(m)
file.close()
