class Phone():
    
    series = 1
    series_name = "Galaxy"
    def __init__(self,year):
        self.year = year
        self.id = Phone.series
        Phone.series += 1
       
    def __str__(self):
        self.name = Phone.series_name +" "+ str(self.id) +"-"+ str(self.year)
        self.phonename = f"{self.name}"
        return self.phonename


phone1 = Phone(2019)
phone2 = Phone(2020)
print(phone1)
print(phone2)        
               