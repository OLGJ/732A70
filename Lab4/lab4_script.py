from pickle import FALSE
import re           # Import regex for string cleaning
from itertools import chain
from itertools import islice
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
        try:
            with open(self.textfile, 'r', encoding='utf_8_sig') as file:
                
                sentences = [row.lower().split() for row in file] # Splits into sentences
                
                all_words = lambda x: chain.from_iterable(x) # Acts as an unlisting

                regex = re.compile('[^a-zA-Z]') # Define regex
                cleaned_words = map(lambda x: regex.sub('', x), all_words(sentences)) 
                # Applies regex to unlisted elements

                self.cleaned_words = list(cleaned_words)
                

        # Exception error if file does not exist
        except FileNotFoundError as e:
            # [ ] If the file does not exist, you need to print "The file does not exist!" (ie not just crash).
            e = "The file doesn't exist"
            
            print(e)

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
        
        word_candidates = []
        for i, word in enumerate(wordcheck):
            word_candidates.append([])
            for index, item in enumerate(words):
                if word == item:
                    word_candidates[i].append(words[index:index+2])       
        
        
        most_common = []
        for word_list in word_candidates:
            word_pairs_flatten = [item for sublist in word_list for item in sublist] 
            result = Counter(word_pairs_flatten)
            most_common.append(result.most_common(4)) # We select the 4 most common words
        

        if self.write: # If user specified output file
            print("Output file created!")
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
        
shake = Shakespear('shakespeare.txt', "hii.txt")
shake.parse()
shake.output()


#### Additional questions
# We did some cleaning of the text by removing non-alphabetical characters, and apply .lower()
# to all text. As such it treats/converts all of the cases "lord", "Lord" and "lord." to "lord".