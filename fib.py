import datetime

x = input ("Enter index value: ")
(x)=int(x)
#pass
dateFormat = "%Y-%m-%d %H:%M:%S"
count = 0
index = 20

def Fib (x):
    global count
    count += 1
    #if x == 0, return 0
    if x == 0:
        return (0)
    elif x == 1:
        return (1)    
    #if x == 1, return 1
    else:
        return Fib(x-1) + Fib(x-2)
# print (x)
# print (Fib(int(x)))
# x has to be positive
#  .pop(something) .append (maybe)      
print ("Start: %s" % datetime.datetime.now().strftime(dateFormat))
print ("Result: %s -> %s" % (index, Fib(index)))
print ("Call Count: %s" % count) # Fib was called this many times
print ("End: %s" % datetime.datetime.now().strftime(dateFormat))