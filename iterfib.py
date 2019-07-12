import datetime

x = input ("Enter index value: ")
(x)=int(x)
dateFormat = "%Y-%m-%d %H:%M:%S"
count = 0
index = 20

def F_iter(x):
    global count
    count += 1
    if (x == 0):
              print (0)
    elif (x == 1):
              print (1)
    elif (x > 1):
              fx = 1
              fx1 = 1
              fx2 = 1
              for x in range(2, x):
                      fx = fx + fx1
                      fx1 = fx2
                      fx2 = fx
              #print ("Start: %s" % datetime.datetime.now().strftime(dateFormat))
              #print ("Result: %s -> %s" % (index, F_iter(index)))
              print ("Call Count: %s" % count) # Fib was called this many times
              #print ("End: %s" % datetime.datetime.now().strftime(dateFormat))         
              print (fx)
              #print ("Start: %s" % datetime.datetime.now().strftime(dateFormat))
              #print ("Result: %s -> %s" % (index, F_iter(index)))
              print ("Call Count: %s" % count) # Fib was called this many times
              #print ("End: %s" % datetime.datetime.now().strftime(dateFormat))
              
F_iter(x)
