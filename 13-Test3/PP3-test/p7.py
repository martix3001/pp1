class C():

    @staticmethod
    def m(n):
        prev= 9
        while n > 0:
            cyf = n % 10
            if(cyf <= prev):
                prev = cyf
                n = int(n/10)
            else:
                return False    
        return True        