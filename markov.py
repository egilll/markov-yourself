# -*- coding: utf-8 -*-

import markovify
import nltk
import re

class NewlineText(markovify.Text):
    def sentence_split(self, text):
        return re.split(r"\s*\n\s*", text)

with open("messages_from_this_name.txt") as f:
    text = f.read()



# Markovify by periods. 
#     This will produce more hilarious output,
#     but is not a 'correctly' trained Markov chain
#     since in messages_from_this_name.txt
#     messages are split by newline,
#     and periods are rare in chats.
text_model = markovify.Text(text)

# Output some long sentences
print('\n\n––––––––––––– 1 –––––––––––––')
for i in range(20):
    print(text_model.make_sentence(tries=3000))

# Output some short sentences
print('\n\n––––––––––––– 2 –––––––––––––')
for i in range(20):
    print(text_model.make_short_sentence(140))



# Markovify by newline. 
#     This will produce shorter & dryer sentences.
text_model_by_newlines = NewlineText(text)

# Output some long sentences
print('\n\n––––––––––––– 3 –––––––––––––')
for i in range(20):
    print(text_model_by_newlines.make_sentence(tries=3000))

# Output some short sentences
print('\n\n––––––––––––– 4 –––––––––––––')
for i in range(20):
    print(text_model_by_newlines.make_short_sentence(140))