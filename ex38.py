ten_things = "Apples Oranges Crows Telephones Light Sugar"

print ("Wait, there are not ten things in that list!  Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print ("Adding: ", next_one)
    stuff.append(next_one)
    print (f"There are {len(stuff)} items now.")

print ("There we go: ", stuff)

print ("Lets do some things with stuff.")

print (stuff[1])
print ("This is the 1 index")
print (stuff[-1]) #whoa fancy
print ("This is the -1 index")
print (stuff.pop())
print ("This is stuff.pop")
print (', '.join(stuff)) #what??? cool!
print ("This is .join with ', 'as a separator")
print ('#'.join(stuff[3:5]))# Super stellar!!
print ("This extracts a slice from the list starting at index 3 and stopping at index 5, so it does not include 5 with a # separator")