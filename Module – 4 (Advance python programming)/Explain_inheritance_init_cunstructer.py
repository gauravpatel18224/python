'''
• Explain Inheritance in Python with an example? What is init? Or What 
Is A Constructor In Python?
'''
class A:
    def __init__(self):
        print("Class A init call ")
    def Get_Data(self,a,b):
        self.a=a
        self.b=b
class B(A):
    def __init__(self):
        print("Class B init call ")
    def Put_Data(self):
        print('A : ',self.a)
        print('B : ',self.b)
b1=B()
b1.Get_Data(10,20)
b1.Put_Data()
