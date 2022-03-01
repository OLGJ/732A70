#!/usr/bin/env python3
from itertools import chain
import sys
import os
import re           # Import regex for string cleaning
from itertools import chain
from collections import Counter


class Shakespear:

    def __init__(self, textfile, write = None):
        self.textfile = textfile
        self.write = write

        if not self.textfile:
            # To check if user did not provide a textfile
            raise ValueError("Inte bra")

    def parse(self):
        """Parse the file into single words with UTF-8 BOM encoding"""

        with open(self.textfile, 'r', encoding='utf_8_sig') as file:

            sentences = [row.lower().split() for row in file] # Splits into sentences

            all_words = lambda x: chain.from_iterable(x) # Acts as an unlisting

            regex = re.compile('[^a-zA-Z]') # Define regex
            cleaned_words = map(lambda x: regex.sub('', x), all_words(sentences))
            # Applies regex to unlisted elements

            self.cleaned_words = list(cleaned_words)
            self.total_words = len(self.cleaned_words)

            return self.cleaned_words, self.total_words

    def find_word_decendant(self, wordlist):
        """
        Takes input of strings(words) in a list to locate decendants for.
        Returns a list (of lists for each word to look for) with (word, occurences)
        """
        words = self.cleaned_words
        n = self.total_words
     
        word_candidates = []
        for _, word in enumerate(wordlist):
            word_candidates.append([words[index:index+2] for index, item in enumerate(words) if word == item]) # Get word and consequent word
            
        most_common = [Counter(chain.from_iterable(frequent_word)).most_common() for frequent_word in word_candidates]
        
        return most_common

    def output(self):
        """Output:
            nwords = number of words the text contain
            nunique = number of unique words
            mostcommon = print five most common, their frequency and n-occurences
        """
        words = self.cleaned_words

        alphabetic_frequency =  Counter(chain.from_iterable(words))

        word_freq = Counter(words).most_common(5)
        # The words we want to check 3 decendants
        wordcheck = [word_tuple[0] for word_tuple in word_freq]


        most_common = self.find_word_decendant(wordcheck)

        if (self.write is not None): # If user specified output file

            with open(self.write, 'w') as file:
                    # Task 1
                    print(f"The frequency of each alphabetical character:", file=file)
                    for char, value in alphabetic_frequency.most_common():
                        print(char, value, file=file)

                    # Task 2
                    print(f"The number of words are {len(list(words))}", file=file)

                    # Task 3
                    print(f"The number of unique are {len(set(list(words)))}", file=file)

                    # Task 4
                    print(f"The most common words are:", file=file)

                    for i, word in enumerate(most_common):
                        print(f"{word_freq[i][0]} ({word_freq[i][1]} occurences)", file=file)
                        for w in word[1:4]:
                            print(f"-- {w[0]}, {w[1]}", file=file)

        ######### Printing part ###########
        # Task 1
        print(f"The frequency of each alphabetical character:")
        for char, value in alphabetic_frequency.most_common():
            print(char, value)

        # Task 2
        print(f"The number of words are {len(list(words))}")

        # Task 3
        print(f"The number of unique are {len(set(list(words)))}")

        # Task 4
        print(f"The most common words are:\n")

        for i, word in enumerate(most_common):
            print(f"{word_freq[i][0]} ({word_freq[i][1]} occurences)")
            for w in word[1:4]:
                print(f"-- {w[0]}, {w[1]}")

### Invoking script from terminal
def main():
    """
    Handles if operative system is windows or else.
    Invoke instance depending on number of arguments
    """
    operative = False
    if os.name == 'nt':
        operative = True

    if operative:
        print("Operative system is Windows")

        if len(sys.argv) < 3:

            try:
                print("No outputfile passed - invoking script withouth generating output to a file")
                shake = Shakespear(sys.argv[1])
                shake.parse()
                shake.output()
            # IndexError if no fileargument was passed
            except IndexError as e:
                e = "Provide a textfile to read"
                print(e)
            # Exception error if file does not exist
            except FileNotFoundError as f:
                    f = "The file does not exist!"
                    print(f)


        else:
            try:
                print("Outputfile passed - 2nd argument will be created")
                shake = Shakespear(sys.argv[1], sys.argv[2])
                shake.parse()
                shake.output()
                        # IndexError if no fileargument was passed
            except IndexError as e:
                e = "Provide a textfile to read"
                print(e)
            # Exception error if file does not exist
            except FileNotFoundError as f:
                    f = "The file does not exist!"
                    print(f)
    else:

        if len(sys.argv) <= 2:

            try:
                print("Operative system is not windows")
                shake = Shakespear(sys.argv[0])
                shake.parse()
                shake.output()
                        # IndexError if no fileargument was passed
            except IndexError as e:
                e = "Provide a textfile to read"
                print(e)
            # Exception error if file does not exist
            except FileNotFoundError as f:
                    f = "The file does not exist!"
                    print(f)
        else:
            try:
                print("Outputfile passed - 2nd argument will be created")
                shake = Shakespear(sys.argv[0], sys.argv[1])
                shake.parse()
                shake.output()
                        # IndexError if no fileargument was passed
            except IndexError as e:
                e = "Provide a textfile to read"
                print(e)
            # Exception error if file does not exist
            except FileNotFoundError as f:
                    f = "The file does not exist!"
                    print(f)

if __name__ == "__main__":
    main()
    print("Running as main.")

else:
    print("I was imported!")



#### Additional questions
# We did some cleaning of the text by removing non-alphabetical characters, and apply .lower()
# to all text. As such it treats/converts all of the cases "lord", "Lord" and "lord." to "lord".
