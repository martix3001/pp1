class C():

    def __init__(self,number):
        self.exp = number
    def m1(self):
        self.exp += 0
        print(self.exp)
    def m2(self):
        self.exp += 1
        print(self.exp)
    def m3(self):
        self.exp -= 1  
        print(self.exp)
        
    def m4(self,n):
        self.exp += n  
        print(self.exp) 
          


c = C(5)

c.m1()
c.m2()
c.m1()
c.m4(-8)
c.m1()
c.m3()
c.m1()
c.m4(10)
c.m1() 


