class Horse():
    def __init__(self, name):
        self.name = name 

class Rider():
    def __init__(self, name, horse):
        self.name = name 
        self.horse = horse
        
horse = Horse("Trigger")        
Barry = Rider ("Barry Archer", horse)


print (Barry.horse.name)