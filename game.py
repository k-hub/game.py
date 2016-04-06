
# Greet the Player.
name = raw_input("Hi, what's your name? ")

while True:
    print "%s, let's play a guessing game!" % name
    print "%s, I'm thinking of a number between 1 and 100. Try to guess my number." % name

    # Generate random number.
    from random import randint
    rand = randint(1, 100)
    print "random number: ", rand

    # Track number of tries.
    tries = 0
    while True:
        # Check if user input is an integer.
        try:
            guess = int(raw_input("Guess my number: "))
        except:
            print "This is not an integer."
            guess = int(raw_input("Tell me your guess. "))

        # Check if guess is within range.
        if guess > 100 or guess < 1:
            print "Your guess is out of range. Please pick a number from 1 to 100."
        elif guess > rand:
            print "Your guess is too high, try again."
            tries += 1
        elif guess < rand:
            print "Your guess is too low, try again."
            tries += 1
        else:
            tries += 1
            print "Congratulations, %s, you guessed my number in %s tries!" % (name, tries)
            break

    # Ask if user wants to play again or quit the game.
    play_again = raw_input("Would you like to play again? Y/N > ")
    if play_again == "Y" or play_again == "y":
        print "Okay let's play!"
    else:
        print "Goodbye!"
        break
