# spellcheck.py

def read_words(fname):
    """Read a file of unique words, one per line, and return a dictionary of the words.
    
    The keys are the words, and the values are all 1. Make sure to strip-off any
    whitespace characters from the beginning and end of each word.

    For example, suppose words.txt contained these 4 words:

        shoes
        hats
        glove
        socks
    
    Then:

        >>> words = read_words('words.txt')
        >>> words
        {'shoes': 1, 'hats': 1, 'glove': 1, 'socks': 1}
    """
    all_words = {}
    word_file = open(fname)
    for w in word_file:
        w = w.strip()
        all_words[w] = 1
    return all_words


def get_misspelled(line, word_dict):
    """Returns a list of all the words in line that are misspelled. 
    
    A word is considered misspelled if it has more than one character and also
    doesn't appear as a key in word_dict.

    >>> words = read_words('words.txt')
    >>> get_misspelled('I like a glove and socks', words)
    ['and', 'like']
    """
    misspelled = {}
    for w in line.split():
        if len(w) > 1 and w not in word_dict:
            misspelled[w] = 1
    unique_words = list(misspelled.keys())
    unique_words.sort()
    return unique_words


def clean_text(text):
    """Remove all non-letter characters from text.

    Keeps just alphabetic characters and spaces.

    >>> clean_text('Hello, world!')
    'Hello  world '
    """
    cleaned_text = ''
    for char in text:
        if char.isalpha() or char == ' ':
            cleaned_text += char # keep spaces and letters
        else:
            cleaned_text += ' '  # replace other characters with spaces
    return cleaned_text


def print_misspelled_words_in_file(fname, word_dict):
    """Prints a list of all the misspelled words in the file.

    Includes the line number of the misspelled words.

    Suppose short_story.txt contains these 3 lines:

        I have no shoes glove or socks just a shirt

    And words.txt contains these 4 words:

        shoes hats glove socks

    Then:

        >>> words = read_words('words.txt')
        >>> print_misspelled_words_in_file('short_story.txt', words)
        Line 1: have, no
        Line 3: or
        Line 4: just, shirt
    
    Hint: If lst is a list of strings, then ', '.join(lst) is a string of all
    the words separated by commas.
    """
    line_num = 1
    file = open(fname)
    for line in file:
        misspelled = get_misspelled(line, word_dict)
        if len(misspelled) > 0:
            bad_words = ', '.join(misspelled)
            print(f'Line {line_num}: {bad_words}')
        line_num += 1

if __name__ == '__main__':
    import doctest
    doctest.testmod()
