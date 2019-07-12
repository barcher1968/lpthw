class Hexagon():
    def __init__(self, s):
        self.side_length = s

    def calculate_perimeter(self):
        return self.side_length * 6

hexagon = Hexagon (5)
print (hexagon.calculate_perimeter())    

