class C():
    def __init__(self,arr):
        self.exp = arr
    def __str__(self):
        expr = ""
        sum = 0
        for i in range(len(self.exp) - 1):
            expr += f'{self.exp[i]}+'
            sum += self.exp[i]
        sum += self.exp[-1]     
        expr += f'{self.exp[-1]}={sum}'
        return expr

        
p1 = C([5,12])
p2 = C([6,0,15])


print(p1)
print(p2)
