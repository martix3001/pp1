class C():

    @staticmethod
    def m1(number):
        new_num = 0
        k = 0
        while number >0 :
            n = number % 10 
            if (n%2 == 0):
                new_num += n*(10**k)
                k += 1
            number = int(number/10)
        return new_num
    @staticmethod
    def m2(number):
        prev = 9
        while number >0 :
            n = number % 10
            if (n <= prev):
                prev = n
            else:
                return False
            number = int(number/10)    
        return True
    @staticmethod
    def m3(number):
        returnal = ""
        for i in range(0,10,1):
            num = number
            while num > 0 :
                sth = True
                n = num % 10
                if (i == n):
                    sth = False
                    break
                num = int(num/10) 
            if(sth):
                returnal += str(i)          
        return returnal



print(C.m1(79381))
print(C.m2(125579)) 
print(C.m2(4557879)) 
print(C.m3(23557))
print(C.m3(12340)) 
