#• Write a Python program to count the frequency of words in a file.
from collections import Counter
file=open("demo.txt")
a=file.read().split()
print(Counter(a))
file.close()
