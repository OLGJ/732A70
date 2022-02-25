#!/usr/bin/env python3
#from lab4_script import par as text
import lab4_script #as text_stats
import random
#import lab4_script as dirdir
from lab4_script import Shakespear



################
#python3 -m venv /home/olojo524/Documents/732A70
#source bin/activate

my_Str = "Hi"
print(type(lab4_script))
print(type(Shakespear))
#
b = Shakespear('zzz.txt')
b.parse()
#print(b.parse())
c, d = b.parse()
flat_list = [item for sublist in b.find_word_decendant(['the']) for item in sublist]
dict_list = dict(flat_list)
nprob = sum(dict_list.values(), 0.0)
dict_list_probabilities = {k: v / nprob for k, v in dict_list.items()}
dkeys = list(dict_list_probabilities.keys())
dvals = list(dict_list_probabilities.values())

cur_word = random.choices(dkeys, dvals, k = 1)

my_Str = my_Str + " " + cur_word[0]
print(my_Str)





cd = [[123]]
if not any(cd):
    print("YOOYYOYO")

