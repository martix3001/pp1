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

my_array = [4,1,8,7,2,6,3,3,5,6,7,354]
Arrays.print_in_col(my_array)
Arrays.display_in_row(my_array)
