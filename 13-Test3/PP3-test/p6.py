class C():

    def __init__(self,arr):
        self.arr = arr

    def m(self,n):
        count = 0
        for i in range(len(self.arr)):
            if (self.arr[i][0] > 0 and self.arr[i][1] > 0):
                count += 1
        if(count >= n):
            ret = True
        else:
            ret = False    

        return ret    