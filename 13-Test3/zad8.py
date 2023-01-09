class C():
    def __init__(self,dic):
        self.dic = dic
        pass
    def m(self,n):
        l = []
        li = ""
        for i in self.dic:
            sum = 0
            k = 0
            for j in range(len(self.dic[i])):
                sum += self.dic[i][j]
                k += 1
            avr = sum/k
            if avr >= n :
                l.append(i)
        l.sort()        
        for i in range(len(l)-1):
           li += f'{l[i]},'   
        if(len(l)>0):
             li += f'{l[-1]}'     
        return li       

                

s = C({"Peter":[4,5,4], "Harry":[2,5], "Barbara":[3,3,3,5,5,5]})
print(s.m(5))