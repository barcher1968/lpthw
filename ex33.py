
i = input("What is your starting index? ")
i = int (i)
#i = int(i)
j = input ("What is your incrementer? ")
#input (int j)
j = int (j)

numbers = []

def numb (i, j):
    
    while i < 10:
        print (f"At the top i is {i}")
        numbers.append (i)

        i = i + j
        print ("Numbers now: ", numbers)
        print  (f"At the bottom i is {i}.")

print ("The numbers: ")

for num in numbers:
    print (num)

numb (i, j)  
