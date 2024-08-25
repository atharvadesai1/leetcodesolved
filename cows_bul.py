# You are playing the Bulls and Cows game with your friend.

# You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

# The number of "bulls", which are digits in the guess that are in the correct position.
# The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
# Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

# The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.


def getHint(secret, guess):
    ans = ""
    secret = list(secret)
    guess = list(guess)
    bulls = 0
    i = 0
    while i < len(secret):
        if secret[i] == guess[i]:
            bulls += 1
            secret.pop(i)
            guess.pop(i)
        else:
            i += 1
        
    print(secret)
    print(guess)
    ans += str(bulls) + "A"

    i = 0
    cows = 0
    while i < len(guess):
        if guess[i] in secret:
            cows += 1
            secret.remove(guess[i])
        i += 1
    
    ans += str(cows) + "B"
    return ans


secret = "1807"
guess = "7810"
answer = getHint(secret, guess)
print(answer)