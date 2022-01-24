
import random

words = ['android',"boy","dag","girl","computer","password"]

word = random.choice(words)
print("-" * len(words))
joon = 10

while joon > 0:
    user_character = input()

    if user_character in word:
        print("yes")
    else:
        joon = joon - 1