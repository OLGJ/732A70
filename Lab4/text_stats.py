#!/usr/bin/env python

import re
import string
import sys

def clean_line(line) :
    """takes a line string, extracts the words, and returns a list(possibly empty) of meaningful words in lowercase"""
    # ignore the lines starting with escape characters
    if repr(line).startswith("'\\") :
        return []
    # strip the line
    line = line.strip()
    # ignore if the stripped line is a number
    if line.isdigit() :
        return []
    # split the line
    line = line.split()
    # remove words containing digits
    line = [x for x in line if len(re.findall(r"\d+", x)) == 0]
    # clean every word
    for i, word in enumerate(line) :
        # remove the leading or trailing punctuations or special characters
        word = word.strip(string.punctuation + " ")
        # convert into lowercase
        word = word.lower()
        line[i] = word
    return line
    

def update_alphabet_counts(word, alphabet_counts) :
    """count each letter in the given word, and update the alphabet_counts dictionary"""
    for letter in word :
        if letter.isalpha() :
            alphabet_counts[letter] = alphabet_counts.get(letter, 0) + 1
        
def update_word_counts(word, predecessor, word_counts) :
    """increment the count of the given word by 1, and include the word as a successor of the predecessor"""
    if word in word_counts :
        word_counts[word][0] += 1
    else :
        word_counts[word] = [1, {}]
        
    word_counts[predecessor][1][word] = word_counts[predecessor][1].get(word, 0) + 1
        

def generate_text_stats() :
    """generates the text stats for the input file given as command line argument, and returns the text stats in the form of 2 dictionaries (alphabet_counts & word_counts)"""
    # dictionary to store the count of each alphabet
    alphabet_counts = {}
    # dictionary in which keys are words occuring in the text, and value is a list whose first element is the count of that key,
    # and second element is a dictionary of successors and their counts
    word_counts = {None : [0, {}]} # predecessor of the very first word parsed will be None
    
    # file to read must be provided by user, otherwise print a message and exit
    try :
        filename = sys.argv[1]
    except IndexError :
        print("Please provide a text file to read.")
        sys.exit()
    
    predecessor = None # initially predecessor is None before parsing the file
    # parse the file and print the output or store the output in the output_file
    try :
        with open(filename, encoding = "utf8") as file:
            for line in file :
                # clean the line
                line = clean_line(line)
                # parse the cleaned line
                for word in line :
                    update_alphabet_counts(word, alphabet_counts)
                    update_word_counts(word, predecessor, word_counts)
                    predecessor = word
    # if the filename provided by user does not exist, print a message        
    except FileNotFoundError :
        print("The file does not exist!")
        sys.exit()
        
    # sort the alphabet in descending order of frequency
    alphabet_counts = sorted(alphabet_counts.items(), key = lambda x: x[1], reverse = True)
    return alphabet_counts, word_counts
    

# code to execute only when this module is executed, and not when imported
if __name__ == "__main__" :
    alphabet_counts, word_counts = generate_text_stats()
    # output file provided by user (optional)
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    if output_file is None : # print the text stats
        # print frequency of each letter
        print("Frequency of letters in the text (in descending order):")
        for letter, frequency in alphabet_counts :
            print(f"{letter}: {frequency}")
        print()
        
        # print total number of words
        num_words = 0
        for value in word_counts.values() :
            num_words += value[0]
        print(f"Number of words: {num_words}")
        # print number of unique words
        print(f"Number of unique words: {len(word_counts)}")
        print()
        # print 5 most common words, along with 3 of their most common successors
        common_words = sorted(word_counts.items(), key = lambda x: x[1][0], reverse = True)[:5]
        print("5 most common words in the text:\n")
        for i in common_words :
            print(f"{i[0]} ({i[1][0]} occurrences)")
            # sort the successors of the word by descending order of count, and select at most 3
            most_common_successors = sorted(i[1][1].items(), key = lambda x: x[1], reverse = True)[:3]
            for j in most_common_successors :
                print(f"-- {j[0]}, {j[1]}")
            print()

    else : # write the text stats to the output file
        print(f"text stats written to the output file: {output_file}")
        with open(output_file, mode = "w", encoding = "utf8") as file :
            # write frequency of each letter
            file.write("Frequency of letters in the text (in descending order):\n")
            for letter, frequency in alphabet_counts :
                file.write(f"{letter}: {frequency}\n")
            file.write("\n")
        
            # write total number of words
            num_words = 0
            for value in word_counts.values() :
                num_words += value[0]
            file.write(f"Number of words: {num_words}\n")
            # write number of unique words
            file.write(f"Number of unique words: {len(word_counts)}\n")
            file.write("\n")
            # write 5 most common words, along with 3 of their most common successors
            common_words = sorted(word_counts.items(), key = lambda x: x[1][0], reverse = True)[:5]
            file.write("5 most common words in the text:\n")
            for i in common_words :
                file.write(f"{i[0]} ({i[1][0]} occurrences)\n")
                # sort the successors of the word by descending order of count, and select at most 3
                most_common_successors = sorted(i[1][1].items(), key = lambda x: x[1], reverse = True)[:3]
                for j in most_common_successors :
                    file.write(f"-- {j[0]}, {j[1]}\n")
                file.write("\n")
                
"""
Additional questions
[Q1] In what way did you "clean up" or divide up the text into words (in the program; the text files should be left unaffected)? This does not have to be perfect in any sense, but it should at least avoid counting "lord", "Lord" and "lord." as different words.

[A1] We implemented a function clean_line that takes a text line as a single string. It removes any line starting with a special character or containing any number. Otherwise it removes any special character or whitespace at the beginning or end, then breaks the line into potential words by splitting the line string at whitespaces. Then it cleans individual words by removing any leading or trailing special character or whitespace, and converts each word to lowercase. We observe that the text contains hyphenated words (like self-substantial) or words containing apostrophe (like mak’st), such words are treated as single words.
  
[Q2] Which data structures have you used (such as lists, tuples, dictionaries, sets, ...)? Why does that choice make sense? You do not have to do any extensive research on the topics, or try to find exotic modern data structures, but you should reflect on which of the standard data types (or variants thereof) make sense. If you have tried some other solution and updated your code later on, feel free to discuss the effects!

[A2] We have used dictionary for storing both the alphabet counts, and word counts. This choice seems most appropriate for our use case, as the most frequent operations are looking up a letter or a word to update its count or looking up a word to add a new successor or increment the count of an existing successor, and lookups are fast using a dictionary. Further for storing word counts, we have used a dictionary with each unique word as a key, and a list of length 2 as value. This list contains the count of the respective word as its first element, and the second element is a dictionary with each successor of the word as a key, and the count of that successor as value.
"""