# To work on the advanced problems, set to True
ADVANCED = True


def count_unique(input_string):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of times
    that word appears in the string as values.


    For example:

        >>> print_dict(count_unique("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time:

        >>> print_dict(count_unique("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different:

        >>> print_dict(count_unique("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}

    """
    # Split input string into a list we can iterate over.
    words = input_string.split()

    # Create a dictionary to hold unique word:count pairs.
    unique = {}

    # Iterate over the list and increase the corresponding word count
    # in the dictionary by one. If the word is not already in the 
    # dictionary, we create a new entry with a count of one.
    for word in words:
        unique[word] = unique.get(word, 0) + 1

    return unique


def find_common_items(list1, list2):
    """Produce the set of common items in two lists.

    Given two lists, return a list of the common items shared between
    the lists.

    IMPORTANT: you may not not 'if ___ in ___' or the method 'index'.


    For example:

        >>> sorted(find_common_items([1, 2, 3, 4], [1, 2]))
        [1, 2]

    If an item appears more than once in at least one list and is present
    in both lists, return it each time:

        >>> sorted(find_common_items([1, 2, 3, 4], [1, 1, 2, 2]))
        [1, 1, 2, 2]

    (And the order of which has the multiples shouldn't matter, either):

        >>> sorted(find_common_items([1, 1, 2, 2], [1, 2, 3, 4]))
        [1, 1, 2, 2]

    """
    # Create dictionary to hold number:# repeats pairs
    common_count = {}

    # Iterate over one list and check against every number in the 
    # other list. If the numbers match, the corresponding value for that
    # number in the dictionary is increased by one. If the number isn't
    # already in the dictionary, an entry is created.
    for num1 in list1:
        for num2 in list2:
            if num2 == num1:
                common_count[num1] = common_count.get(num1, 0) + 1
    
    # Because we want to return a list, here we create a list and repeat 
    # each number that is a key in the dictionary for the max number of times
    # it appears in at least one of the lists.
    common_list = []
    for num in common_count:
        for i in range(common_count[num]):
            common_list.append(num)

    return common_list


def find_unique_common_items(list1, list2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items shared between
    the lists.

    IMPORTANT: you may not not 'if ___ in ___' or the method 'index'.


    Just like `find_common_items`, this should find [1, 2]:

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [1, 2]))
        [1, 2]

    However, now we only want unique items, so for these lists, don't show
    more than 1 or 2 once:

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [1, 1, 2, 2]))
        [1, 2]

    """
    # Convert each list into a set so we can do set math.
    set1 = set(list1)
    set2 = set(list2)

    # Find the intersection of the two sets and return it as a list.
    unique_common_set = set1 & set2

    return list(unique_common_set)


def get_sum_zero_pairs(input_list):
    """Given a list of numbers, return list of x,y number pair lists where x + y == 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.


    For example:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself):

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1, 0]) )
        [[-2, 2], [-1, 1], [0, 0]]

    """
    # Sort the input list so equivalent pairs look the same when we
    # add them to our set.
    input_list.sort()

    # An empty set to add sum-to-zero pairs.
    sum_zero_set = set()

    # Special case: if there is even just one zero is in the list, we add it 
    # as a sum-to-zero pair.
    if 0 in input_list:
        sum_zero_set.add((0,0))

    # Loop iterate over the sorted input list, adding each number one
    # at a time to numbers following it. If the sum of the pair is zero,
    # we put the pair in a tuple and add the tuple to our set.
    for index1 in range(len(input_list) - 1):
        for index2 in range(index1 + 1, len(input_list)):
            if (input_list[index1] + input_list[index2] == 0):
                pair = (input_list[index1], input_list[index2])
                sum_zero_set.add(pair)

    # Since we want to return a list of lists, we convert the tuples
    # to lists and add them to the list we return.
    unique_pairs = []

    for pair in sum_zero_set:
        unique_pairs.append(list(pair))

    return unique_pairs


def remove_duplicates(words):
    """Given a list of words, return the list with duplicates removed.

    Do this without using a Python set.

    For example:

        >>> sorted(remove_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(remove_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

    """
    # Add each word in the input list as keys to a dictionary to
    # automatically get rid of duplicates.
    word_dict = {}

    for word in words:
        word_dict[word] = word_dict.get(word, 0)

    return word_dict.keys()


def encode(phrase):
    """Given a phrase, return the encoded string.

    Replace all "e" characters with "p",
    replace "a" characters with "d", replace "t" characters with "o",
    and "i" characters with "u".

    For example:

        >>> encode("You are a beautiful, talented, brilliant, powerful musk ox.")
        'You drp d bpduouful, odlpnopd, brulludno, powprful musk ox.'
    """
    # An empty string we'll be adding our encoded characters to.
    encoded = ""

    # A dictionary our loop will use to look up which character replacements.
    encode_pairs = { 'e': 'p',
                    'a': 'd',
                    't': 'o',
                    'i': 'u'}

    for char in phrase:
        encoded += encode_pairs.get(char, char)

    return encoded


def sort_by_word_length(words):
    """Given list of words, return list of ascending [(len, [words])].

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items--the length of the words for that
    word-length, and the list of words of that word length.

    For example:

        >>> sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['ok', 'an']), (3, ['day']), (5, ['apple'])]

    """
    # Create an empty dictionary to add length: [list of words] pairs.
    words_by_length = {}

    # Loop over the list, creating a new entry if the length is not
    # already a key in the dictionary or, if the key already exists, appending
    # the word to the corresponding list.
    for word in words:
        key = len(word)
        if key not in words_by_length:
            words_by_length[key] = [word]
        else:
            words_by_length[key].append(word)

    # We want to return a list so here we create an empty one we'll be adding to.
    final_list = []

    # Create a list of sorted dictionary keys so we can add them to the list in
    # ascending order.
    word_keys = words_by_length.keys()

    # Tuple-ize the dictionary entries and add them to the list.
    for word in word_keys:
        pair = (word, words_by_length[word])
        final_list.append(pair)

    return final_list


def get_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak equivalent.
    Words that cannot be translated into Pirate-speak should pass through
    unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    boy         matey
    madam       proud beauty
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    lawyer      foul blaggart
    the         th'
    restroom    head
    my          me
    hello       avast
    is          be
    man         matey

    For example:

        >>> get_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words:

        >>> get_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'

    """
    # Dictionary of words to replace.
    english_to_pirate = { 'sir': 'matey',
                        'hotel': 'fleabag inn',
                        'student': 'swabbie',
                        'boy': 'matey',
                        'madam': 'proud beauty',
                        'professor': 'foul blaggart',
                        'restaurant': 'galley',
                        'your': 'yer',
                        'excuse': 'arr',
                        'students': 'swabbies',
                        'are': 'be',
                        'lawyer': 'foul blaggart',
                        'the': 'th\'',
                        'restroom': 'head',
                        'my': 'me',
                        'hello': 'avast',
                        'is': 'be',
                        'man': 'matey',
                        }
    
    # Split the phrase into a list of words we can iterate over.
    words = phrase.split()

    # A list to add pirate-translated words to as we loop over the words in
    # the original phrase.
    pirated_words = []

    for word in words:
        word = word.lower()
        pirated_words.append(english_to_pirate.get(word, word))

    # Convert the list of pirate-translated words into a string.
    translated = " ".join(pirated_words)

    return translated

# End of skills. See below for advanced problems.
# To work on them, set ADVANCED=True at the top of this file.
############################################################################


def adv_get_top_letter(input_string):
    """Given an input string, return a list of letter(s) which appear(s) the most the input string.

    If there is a tie, the order of the letters in the returned
    list should be alphabetical.

    For example:
        >>> adv_get_top_letter("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example:
        >>> adv_get_top_letter("Shake it off, shake it off. Shake it off, Shake it off.")
        ['f']

    Spaces do not count as letters.

    """
    # Convert the input string into one long string with no spaces.
    words = input_string.split()
    long_ass_string = "".join(words)

    # First, we want to count how many times each character appears in the string.
    # This is the empty dictionary we'll use to keep track.
    words_app = {}

    # Loop over the string and add each character that appears as a key. The
    # number of times the character appears is its corresponding value.
    for char in long_ass_string:
        words_app[char] = words_app.get(char, 0) + 1

    # Now we know how many times each character appears, we can then organize
    # the dictionary to have number of repeats as keys, and a list of characters
    # that repeat that number of times as values.
    unique_chars = words_app.keys()
    num_words = {}

    for char in unique_chars:
        key = words_app[char]
        if key not in num_words:
            num_words[key] = [char]
        else:
            num_words[key].append(char)

    # We want to return the list of most repeated characters, so we sort the
    # keys and return the value of the last one.
    sorted_keys = sorted(num_words)
    largest_count = sorted_keys[-1]

    return num_words[largest_count]


def adv_alpha_sort_by_word_length(words):
    """Given a list of words, return a list of tuples, ordered by word-length.

    Each tuple should have two items--a number that is a word-length,
    and the list of words of that word length. In addition to ordering
    the list by word length, order each sub-list of words alphabetically.
    Now try doing it with only one call to .sort() or sorted(). What does the
    optional "key" argument for .sort() and sorted() do?

    For example:

        >>> adv_alpha_sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]


    """

    # Create an empty dictionary to add length: [list of words] pairs.
    words_by_length = {}

    # Loop over the list, creating a new entry if the length is not
    # already a key in the dictionary or, if the key already exists, appending
    # the word to the corresponding list.
    for word in words:
        key = len(word)
        if key not in words_by_length:
            words_by_length[key] = [word]
        else:
            words_by_length[key].append(word)

    # We want to return a list so here we create an empty one we'll be adding to.
    final_list = []

    # Create a list of sorted dictionary keys so we can add them to the list in
    # ascending order.
    word_keys = words_by_length.keys()

    # Sort each value list alphabetically, tupelize the dictionary entry, and
    # add them to the list.
    for word in word_keys:
        value = sorted(words_by_length[word])
        pair = (word, value)
        final_list.append(pair)

    return final_list

# ##############################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is just used to print dictionaries in key-alphabetical
    # order, and is only used for our documentation tests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join("%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is used only
    # for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)

if __name__ == "__main__":
    print
    import doctest
    for k, v in globals().items():
        if k[0].isalpha():
            if k.startswith('adv_') and not ADVANCED:
                continue
            a = doctest.run_docstring_examples(v, globals(), name=k)
    print "** END OF TEST OUTPUT"
    print
