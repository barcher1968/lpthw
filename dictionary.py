me = {
    "height":"short", 
    "fav_author":"Althoff",
    "fav_food": "Michelles"
    }



n = input ("ask height, fav_author, fav_food:")
if n in me:
    me = me[n]
    print (me)
else:
    print ("Not found")



