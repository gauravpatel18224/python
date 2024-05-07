#• What is used to check whether an object o is an instance of class A?
class A:
    
    print("Class A ")
obj=A()

if isinstance(obj, (A)):
    print("obj is an instance ")
else:
    print("obj is not an instance")
