# Number guessing game project using python

lucky_no = 45

guess_count = 0
while guess_count < 3:
    num_guess = int(input("Guess the No: "))
    guess_count += 1
    if num_guess == lucky_no :
        print("Congrats you've guess the no {} correctly".format(num_guess))
        break
    else:
        print("you've guessed wrong no")
else:
    print("you've guessed all no wrong")