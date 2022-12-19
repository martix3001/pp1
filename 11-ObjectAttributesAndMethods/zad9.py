import random

class Arrays():

    @staticmethod
    def print_in_col(array):
        for c in array:
            print(c)
    @staticmethod
    def display_in_row(array):
        row = ""
        for i in range(len(array)-1):
            row += str(array[i]) + ","
        row += str(array[-1])    
        print(row)
    @staticmethod
    def appending(number_of_array_elements, value_of_array_elements):
        arr =[]
        for i in range((number_of_array_elements)):
            arr.append(value_of_array_elements)
        print(arr)   

    @staticmethod
    def radomizator(number_of_array_elements, value_from, value_to):
        arr = []
        for i in range((number_of_array_elements)):
            arr.append(random.randint(value_from,value_to))
        return arr
    @staticmethod
    def zliczacz(array, value_from, value_to):        
        count = 0
        for i in array:
            if i >= value_from and i <= value_to:
                count += 1
        print(count)        

my_array = [4,1,8,7,2,6,3,3,5,6,7,354]
Arrays.appending(4,10)
arr = Arrays.radomizator(20,-7,8)
Arrays.zliczacz(arr,-1,1)
Arrays.display_in_row(my_array)