numbers = [11, 32, 34, 78, 98]

while True:
    answer = input("Guess a number or type q to quit:")
    if answer == "q":
       break
    try:
       answer = int(answer)
    except ValueError:
       print ("please type a number or q to quit.")
    if answer in numbers:
       print ("You guessed correctly")
    else:
       print("You guessed poorly")            