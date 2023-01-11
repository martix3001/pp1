class C():

    def __init__(self,d):
        self.dic = d
    def m1(self,s,n):
        self.dic[s] = n
        return self.dic
    def m2(self,s):
        sum = 0
        for i in s:
            sum += self.dic[i]
        return sum  