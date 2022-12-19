class Music():
    
    def __init__(self, name,title,album,year):
        self.name = name 
        self.title = title
        self.album = album
        self.year = year
    
    def __str__(self):
        self.songdata = f"Performer: {self.name}\nSong: {self.title}\nAlbum: {self.album}\nYear: {self.year} "
        return self.songdata

    
piece1 = Music("hehe","lolol","dsadasd",2019)
piece2 = Music("hehe","lolol2","dsadasd2",2020)
piece3 = Music("hehe","lolol3","dsadasd3",2021)
print(piece1)  
print(piece2)
print(piece3)