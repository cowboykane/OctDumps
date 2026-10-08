# oh magic 8ball..

# Prompt user for a question, select random
# response from list, print it out..elemetary..

import random

responses = ("It is certain.", "It is decidedly so.",
             "Without a doubt.", "Yes Definetely.",
             "totally, girl.", "Girl, I guess.",
             "Inshallah", "Reply hazy...Try agian.",
             "Ask again later.", "Better not tell you now.",
             "Don't count on it henny.", "My reply is no.",
             "My sources say no...", "Very doutful.",
             "Concentrate and ask again LOL"
             )

eight_ball = random.choice(responses)

user_question = input("Ask away: ")
print("Readin response...")
print(eight_ball)