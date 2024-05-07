#• Write a Python program to append text to a file and display the text.
file=open("demo.txt","a+")
file.write("Python")
file.seek(0)
print(file.read())
file.close
