name = 'Barry Archer'
age = 50
height = 66 #inches
weight = 180 # lbs
eyes = 'blue'
teeth = 'white'
hair = 'brown'

print (f"Let's talk about {name}.")
print (f"He's {height} inches tall. That is {round (height * 2.54)} in centimeters")
print (f"He's {weight} pounds heavy. That is {round (weight / 2.2)} in kilos.")
print ("that is not too heavy.")
print (f"he's got {eyes} eyes and {hair} hair.")
print (f"His teeth are {teeth} depending on the coffee.")

#this line is tricky to get exactly right
total = age + height + weight
print (f"If I add  {age}, {height}, {weight} I get {total}.")
