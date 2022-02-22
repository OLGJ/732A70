import re           # Import regex for string cleaning
from itertools import chain
from collections import Counter

class Shakespear:

    def __init__(self, textfile, *args):
        self.textfile = textfile
        self.args = args

        if not self.textfile:
            # To check if user did not provide a textfile
            raise ValueError("Inte bra")

            
        if self.args:
            # To check if user provides output argument
            output = args

    def parse(self):
        """Parse the file into single words with UTF-8 BOM encoding"""
        try:
            with open(self.textfile, 'r', encoding='utf_8_sig') as file:
                
                sentences = [row.lower().split() for row in file] # Splits into sentences
                
                all_words = lambda x: chain.from_iterable(x) # Acts as an unlisting

                regex = re.compile('[^a-zA-Z]') # Define regex
                cleaned_words = map(lambda x: regex.sub('', x), all_words(sentences)) # Applies regex to unlisted elements

                self.cleaned_words = list(cleaned_words) # Convert generator object to list
                

        # Exception error if file does not exist
        except FileNotFoundError as e:
            # [ ] If the file does not exist, you need to print "The file does not exist!" (ie not just crash).
            e = "The file doesn't exist"
            
            print(e)

    def write(self):
        if self.args:
            with open(self.args, 'w') as file:
                pass
            #    string = f'Student {name} scored {attributes["Algebra"]} on the Algebra exam and {attributes["History"]} on the History exam.'
            #    file.write(string)
            #    file.write('\n')
        else:
            pass

    def output(self):
        """Output:
            nwords = number of words the text contain
            nunique = number of unique words
            mostcommon = print five most common, their frequency and n-occurences
        """
        words = self.cleaned_words
        setwords = list(set(words))
        tempw = words[1:10]
        
        word_freq = Counter(words).most_common(5)
        #noccurr = word_freq.most_common(5)
         
        print(f"The number of words are {len(list(words))}")
        print(f"The number of unique are {len(set(list(words)))}")
        print(f"The most common words are:\n")
        for word, frq in word_freq:
            print(f"{word}: {frq}")

        
        
        
        

shake = Shakespear('shakespeare.txt')
shake.parse()
cleaned = shake.output()
