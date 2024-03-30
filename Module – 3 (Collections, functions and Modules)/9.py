li1=[30,40,88,6,45,79,8]
li2=[34,44,88,60,5,97,9]

count=0
for i in li1:
    if i in li2:
        count += 1

print("true" if count>=1 else "false")


        
'''if count>=1:
    print("True")
else:
    print("false")'''
