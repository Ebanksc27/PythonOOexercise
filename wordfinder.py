"""Word Finder: finds random words from a dictionary."""


import random

class WordFinder:
    """
    A class for reading words from a file and providing random word retrieval.

    Attributes:
        file_path (str): The path to the file containing words.
        words (list): A list of words read from the file.

    Methods:
        read_file: Read words from the file.
        random: Return a random word from the list of words.
    """

    def __init__(self, file_path):
        """
        Initialize the WordFinder object with a file path and read the words from the file.

        Args:
            file_path (str): The path to the file containing words.
        """
        self.file_path = file_path
        self.words = []
        self.read_file()

    def read_file(self):
        """
        Read words from the file and store them in the words list attribute.
        """
        with open(self.file_path, 'r') as file:
            for line in file:
                word = line.strip()
                self.words.append(word)

    def random(self):
        """
        Return a random word from the list of words.

        Returns:
            str: A random word from the list.
        """
        return random.choice(self.words)
    
    def __repr__(self):
        """
        Returns a string representation of the WordFinder object.

        Returns:
            str: String representation of the object.
        """
        return f"<WordFinder file_path='{self.file_path}' words={self.words}>"
    
# Create a WordFinder instance with the path to the words file
wf = WordFinder("words.txt")

# Print the number of words read
print(len(wf.words), "words read")

# Generate a random word
print(wf.random())

# Generate another random word
print(wf.random())

# Generate another random word
print(wf.random())


class SpecialWordFinder(WordFinder):
    """
    A subclass of WordFinder that excludes blank lines and comments.

    Methods:
        read_file: Read words from the file, excluding blank lines and comments.
    """

    def read_file(self):
        """
        Read words from the file, excluding blank lines and comments.
        """
        with open(self.file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith('#'):
                    self.words.append(line)

# Create a SpecialWordFinder instance with the path to the words file
swf = SpecialWordFinder("words.txt")

# Print the number of words read
print(len(swf.words), "words read")

# Generate a random word
print(swf.random())

# Generate another random word
print(swf.random())

# Generate another random word
print(swf.random())

wf = WordFinder("words.txt")
"""
>>> len(wf.words)  # Check the number of words read
9

>>> wf.random()  # Get a random word
'banana'

>>> wf.random()  # Get another random word
'orange'

>>> wf.random()  # Get another random word
'apple'

>>> wf  # Examine the WordFinder object
<WordFinder file_path='words.txt' words=['banana', 'orange', 'apple', 'kiwi', 'mango', 'pear', 'grape', 'pineapple', 'lemon']>
"""



