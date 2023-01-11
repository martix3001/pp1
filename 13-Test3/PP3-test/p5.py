class C():
    
    def __init__(self,name,sur,age,yr):
        self.name = name
        self.sur = sur
        self.age = age
        self.yr = yr
    def __str__(self):
        if (self.age >= 18):
            nam = self.name.upper()
            rt = f'{self.sur.upper()}{nam[0]}{self.yr}'
        else:
            nam = self.name.lower()
            rt = f'{self.sur.lower()}{nam[0]}{self.yr}'   

        return rt