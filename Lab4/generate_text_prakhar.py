from random import choices
import sys
from text_stats import generate_text_stats

# generate text stats
_, word_counts = generate_text_stats()
# print error message if the word not given by user or the given word not in the given text file
try :
    cur_word = sys.argv[2]
    if cur_word not in word_counts :
        print("Starting word not found in the given file.")
        sys.exit()
except IndexError :
    print("Please provide a starting word to generate text.")
    sys.exit()
# print error message if the number of words not given by user or the argument cannot be converted into an integer, or the argument is negative
try :
    max_words = int(sys.argv[3])
    if max_words <= 0 :
        print("Please provide a non negative integer for the maximum number of words to generate.")
        sys.exit()
except IndexError :
    print("Please provide the maximum number of words to generate.")
    sys.exit()
except ValueError :
    print("Please provide a valid integer for the maximum number of words to generate.")
    sys.exit()
    
# start building the text
msg = cur_word
for i in range(max_words) :
    try :
        cur_word = choices(tuple(word_counts[cur_word][1].keys()), weights = tuple(word_counts[cur_word][1].values()), k = 1)[0]
    except IndexError :
        print(msg)
        sys.exit()
    msg = msg + " " + cur_word
# print the generated text
print(msg)