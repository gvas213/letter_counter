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

# generate random word and hint
word = random.choice(range(len(word_bank)))
hint = word
guess = len((word_bank[word]))
computer_word = []
user_word = []

#user prompts
