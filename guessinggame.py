import random
secret = random.randint(1, 99)  #picks a secret number
guess = 0
tries = 0

print "AHOY! Im the Dread Pirate Robers and I have a secret!"
print "It is a number from 1 to 99. I'll give you 6 tries to guess it!"

while guess != secret and tries < 6:
    guess = input("What's yer guess? ")
    if guess < secret:
        print "Too low, ye scurvy dog!"
        
    elif guess > secret:
        print "Too high, Landlubber!"
        tries = tries +1
if guess == secret:
                print "Avast! Ye got it! Found my secret, ye did!"
else:
    print "No more guesses! Better luck next time, Matey!"
    print "The secret number was", secret
                    
