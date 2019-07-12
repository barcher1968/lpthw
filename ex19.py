# Build a function called cheese and crackers with 2 values cheese count
# boxes of crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # Prints the sentence with the value cheese count in the sentence
    print(f"You have {cheese_count} cheeses!")
    # Prints the sentence with the value boxes of crackers in the sentence.
    print(f"You have {boxes_of_crackers} boxes of crackers")
    # standard print statements
    print("Man that is enough for a party!")
    print("Get a blanket.\n")

print("We can just give the function numbers directly:")
# calls the cheese and crackers funtion and inputs the values 20 and 30
cheese_and_crackers(20, 30)

print("OR, we can use variables from our script:")
# establishes other variables
amount_of_cheese = 10
amount_of_crackers = 50
# calls the function and inputs the newly established variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
# calls the funtions and hands it the values, this time with calculations
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
# this is a mix of the 2 above, where we call a variable and add to it
# with math
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
