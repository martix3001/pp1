class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channel_list = []
    def turn_on(self):
        self.is_on = True
    def turn_off(self):
        self.is_on = False
    def show_status(self):
        if(self.is_on):
            print("TV is on,","Channel no: ",self.channel_no)
        else:
            print("Tv is off")
    def set_channel(self,new_channel_no):
        self.channel_no = new_channel_no   

    def set_channels_list(self,channel_list):
        self.channel_list.append(channel_list)

    def show_channels(self):
        print(self.channel_list)





tv1 = TV()
tv1.show_status()
tv1.turn_on()
tv1.show_status()
tv1.show_channels()
tv1.set_channels_list(["TV1","TV2","Polsat","TVN","Filmbox"])
tv1.show_channels()
tv1.set_channel(2)
tv1.show_status()
tv1.turn_off()
tv1.show_status()
