#!/usr/bin/env python3
from lab4_script import Shakespear
import datetime
import random
import sys


begin_time = datetime.datetime.now()

textfile = sys.argv[1]

sword = sys.argv[2]

nwords = int(sys.argv[3])

text = Shakespear(textfile)
text.parse()

cur_word = [sword] # Word to look for
picked = 0
msg = cur_word[0]
while any(text.find_word_decendant(cur_word)) and picked < nwords:

    # Retrieve all the descendants of cur_word
    descendants = text.find_word_decendant(cur_word)

    flat_list = [item for sublist in descendants for item in sublist]

    # Convert to dictionary and calculate the probability for each descendant
    dict_list = dict(flat_list[1:])
    nprob = sum(dict_list.values(), 0.0)
    dict_list_probabilities = {k: v / nprob for k, v in dict_list.items()}

    dkeys = list(dict_list_probabilities.keys())
    dvals = list(dict_list_probabilities.values())

    # Select one random weighted word
    cur_word = random.choices(dkeys, dvals, k = 1)
    msg = msg + " " + str(cur_word[0])
    picked += 1


print(msg)
print(datetime.datetime.now() - begin_time)

# ./generate_text.pyshakespeare.txt king 500
