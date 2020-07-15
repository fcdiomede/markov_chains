"""Generate Markov text from text files."""

from random import choice
import sys


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here

    return open(file_path).read()


def make_chains(text_string, gram_num):
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

    for index in range(len(words) - gram_num):
        #to account for unknown number of words making up chain
        #use list slicing to grab n number of words
        #convert that list slice back into a tuple
        ngram = tuple(words[index:gram_num + index])
        #the next work after n words will be the index + n
        following_word = words[index + gram_num]
        
        #try to append, if key does not yet exist set an empty list first
        chains.setdefault(ngram, []).append(following_word)

        # if word_pair in chains:
        #     chains[word_pair].append(following_word)
        # else:
        #     chains[word_pair] = [following_word]       

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    #generating a list of valid starting tuples
    #in this case, only tuples with capitalized first words
    starting_tuples = [word_tup for word_tup in chains
                        if word_tup[0][0].isupper()]

    ngram = choice(starting_tuples)

    words.extend(ngram)

    sentence_limit = 3
    sentence_count = 0

    while ngram in chains:

        next_word = choice(chains[ngram])
        words.append(next_word)

        #to build the next gram for an unknown length of chain
        #use list slicing to cut out first word in tuple
        end_of_gram = list(ngram)[1:]

        #add on my following word
        end_of_gram.append(next_word)

        #convert that list back into a tuple to match keys in dictionary
        ngram = tuple(end_of_gram)

        if next_word[-1] in [".","!","?"]:
            sentence_count += 1

        if sentence_count == sentence_limit:
            break

    return " ".join(words)


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, 2)

# Produce random text
random_text = make_text(chains)

print(random_text)
