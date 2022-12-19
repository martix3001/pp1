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
        print (arr)
    @staticmethod
    def zliczacz(array, value_from, value_to):        
        hello = 1

my_array = [4,1,8,7,2,6,3,3,5,6,7,354]
Arrays.appending(3,3)
Arrays.radomizator(7,10,20)
Arrays.display_in_row(my_array)