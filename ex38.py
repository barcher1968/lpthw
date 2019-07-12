ten_things = "Apples Oranges Crows Telephones Light Sugar"

print ("Wait, there are not ten things in that list!  Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 11:
    next_one = more_stuff.pop()
    print ("Adding: ", next_one)
    stuff.append(next_one)
    print (f"There are {len(stuff)} items now.")

print ("There we go: ", stuff)

print ("Lets do some things with stuff.")

print (stuff[0])
print (stuff[-2]) #whoa fancy
print (stuff.pop())
print (', '.join(stuff))  #what??? cool!
print ('#'.join(stuff[4:5])) # Super stellar!!