import random

#words
word_bank = ["avenue", "axiom", "bagpipes", "banjo", "bikini", "blizzard", "cobwebs", "crypt", "espionage", "fluffy", 
"galaxy", "gossip", "hydrogen", "jelly", "jukebox", "keyhole", "queue", "quartz", "quiz", "rhythm",
"sphinx", "stretch", "subway", "transcript", "transplant", "waltz", "wizard", "zipper", "zombie", "zodiac"]

hint_bank = ["This word typically comes after a street name.", "something that is established as self evidently true.", 
"Scottish instrument", "kind of like a guitar", "it's a type of swimsuit", "a very cold storm", "this goes with halloween and spiders",
"it's underground", "government spying", "used to describe stuffed animals", "the milkyway is considered this", "[] girl. It's a popular TV show", 
"the simplest atom", "the type of fish that stings", "old way of playing music", "has to do with a lock and key", 
"another way to say line", "crystal people use for manifesting", "easier version of a test", "patterns in music and poetry", 
"it has a woman's head and a lion's body", "you should do this before working out.", "a form of public transportation", "document of all your grades",
"type of surgery that involves moving organs", "a classic ballroom dance", "think Harry Potter", "it's on most jackets", "they eat peoples brains", 
"What's your star sign?"]

congrats = ["Congrats!", "You got it!", "Yay! You got it!", "Great Job!", "Awesome, you got it!"]
bad = ["try again", "lol wrong", "incorrect", "That's wrong", "try a different letter"]

#generate random word and hint
word = random.choice(range(len(word_bank))) #index of the word
hint = (hint_bank[word]) #hint
word = (word_bank[word]) #the actual word
word_split = tuple(word)
guess = list(word)


for x in range(len(guess)):
    guess[x] = "-"

user_guess = "".join(guess)
counter = len(guess) +2

#game
print("Welcome to the game! Guess a letter or the whole word before your tries run out to win.")
print(f"your hint is: {hint}")
    
while user_guess != word and counter != 0 and counter > 0:
    letter = input(f"Your word is: {user_guess} Guess a letter or word! You have {counter} tries left. ")

    while letter.isalpha() != True:
        letter = input("Please enter a letter or word to guess: ")    
    
    letter = letter.lower()
    x = random.choice([0, 5])

    for x in range(len(guess)):
        if word_split[x] == letter:
            guess[x] = letter
            user_guess = "".join(guess)
            print(congrats[x])
        elif letter == word:
            user_guess = word
            
    counter = counter - 1
    
#end of game
if user_guess == word:
    print("Congrats! you guessed the word.")
else:
    print(f"Sorry you ran out of attempts. The correct word was {word}.")



#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

