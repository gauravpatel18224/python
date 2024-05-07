'''• How to Define a Class in Python? What Is Self? Give An Example Of 
A Python Class'''

class A:
    def get_data(self,a,b):
        self.a=a
        self.b=b
    def put_data(self):
        print("A : ",self.a)
        print("B : ",self.b)

a1=A()
a=int(input("Enter A : "))
b=int(input("Enter B : "))

a1.get_data(a,b)
a1.put_data()
