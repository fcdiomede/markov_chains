"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here

    return open(file_path).read()


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    words = text_string.split()
    chains = {}

    for index in range(len(words) - 2):
        word_pair = (words[index], words[index + 1])
        following_word = words[index + 2]
        chains.setdefault(word_pair, []).append(following_word)
        # if word_pair in chains:
        #     chains[word_pair].append(following_word)
        # else:
        #     chains[word_pair] = [following_word]       

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    bigram = choice(list(chains.keys()))

    words.extend(bigram)

    while bigram in chains:
        next_word = choice(chains[bigram])
        words.append(next_word)
        bigram = (bigram[1], next_word)

    return " ".join(words)


input_path = "gettysburg.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
