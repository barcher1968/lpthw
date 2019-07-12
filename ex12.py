while True:
    try:
        age = int(input("How old are you? "))
        break
    except ValueError:
            print ("That is not a number, try again.")
while True:
    try:            
        height = int(input("How tall are you? "))
        break
    except ValueError:
            print ("That is not a number, try again.")
while True:
    try:            
        weight = int(input("How much do you weigh? "))
        break
    except ValueError:
            print ("That is not a number, try again.")
print (f"so you're {age} old and you're {height} tall.")