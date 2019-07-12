# sets variables and values
people = 30
cars = 40
trucks = 15

# are there more cars than people
if cars > people:
    print ("We should take the cars")
# are there less cars than people 
elif cars < people:
    print ("we should not take the cars")
# are there an equal number of cars and people    
else:
    print ("We can't decide")
# are there more cars than trucks
if trucks > cars:
    print ("That is too many trucks.")
# are there less cars than trucks
elif trucks < cars:
    print ("Maybe we could take the trucks")
# are there an equal number of cars and trucks
else:
    print ("We still can't decide.")
# are there more people than trucks
if people > trucks:
    print ("Alright, lets just take the trucks.")
# are there an equal number of people and trucks    
else:
    print ("Fine, lets just stay home then.")
