string= "number of character"
frequency={}
 
for i in string:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1
print("Count of all characters in string is :\n "
      + str(frequency))
