#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
import random  

tails = 1
heads = 0

heads_or_tails = random.randint(0,1)

if heads_or_tails == 0:
    print("Heads")
if heads_or_tails == 1:
    print("Tails")
