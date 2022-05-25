class transport:
    def __init__(self, marka,year,color):
        self.marka=marka
        self.year=year
        self.color=color

    def get_info(self):
        return f"Marka:{self.marka}, yili{self.year}, rangi:{self.color}"

class Avto(transport):
    def __init__(self,marka,year,color,model,transmission):
        super().__init__(marka,year,color)
        self.model = model
        self.transmission=transmission
    def get_info(self):
        return f"{super().get_info()} modeli:{self.model},transmissiyasi:{self.transmission}"

class Yukavto(Avto):
    def __init__(self,marka,year,color,model,transmission,tipi,yuk_vazni,km=0):
        super().__init__(marka,year,color,model,transmission)
        self.tipi=tipi
        self.yuk_vazni=yuk_vazni
        self.km=km
    def get_info(self):
        return f"{super().get_info()}, tipi:{self.tipi},yuk vazni:{self.yuk_vazni}, km:{self.km}"



kamaz=Yukavto("Kamaz",2000,"sariq","T-34","Avtomat","Samosvall","10 tonna", 100000000)
print(kamaz.get_info())





