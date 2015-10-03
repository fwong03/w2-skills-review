# To work on the advanced problems, set to True
ADVANCED = False


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
    # Create a dictionary to hold unique word:count pairs and and
    # split our input string into a list we can iterate over.
    words = input_string.split()
    unique = {}

    # Iterate over our list and to prevent duplicates added due to
    # capitalization or punctuation, we convert the word to all lowercase
    # and strip out punctionation before checking if the word is in our
    # dictionary.
    for word in words:
        word = word.lower()
        word = word.strip("?.,:;!'\"_()-__")
        unique[word] = unique.get(word, 0) + 1

    return unique

# string = "Hello there, how are you? Hello hello, you you you you"
# print count_unique(string)


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
    common = []

    # This loop checks each item in one list against each item in the other.
    # If a match is found, the item is appended to our list.
    for item1 in list1:
        for item2 in list2:
            if item2 == item1:
                common.append(item2)

    return common


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
    # Convert each list into a set so we can do set math
    set1 = set(list1)
    set2 = set(list2)

    # Find the intersection of the two sets and convert it to a list
    unique_common_set = set1 & set2
    unique_common_list = list(unique_common_set)

    return unique_common_list


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
    # Create an empty set so we automatically get rid of duplicates as
    # we add pairs.
    sum_zero_set = set()

    # Sort the input list so equivalent pairs look the same when we
    # add them to our set.
    input_list.sort()

    # Loop iterate over the sorted input list, adding each number one
    # at a time to numbers following it. If the sum of the pair is zero,
    # we put the pair in a tuple and add the tuple to our set.
    for index1 in range(len(input_list) - 1):
        for index2 in range(index1 + 1, len(input_list)):
            if (input_list[index1] + input_list[index2] == 0):
                pair = (input_list[index1], input_list[index2])
                sum_zero_set.add(pair)

    # Since we want to return a list of lists, we convert the tuples
    # to lists and add these lists to the list we return.
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
    encoded = ""

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
    # Create an empty dictionary to add length: [list of words] value
    # pairs
    words_by_length = {}

    # Loop over the list, creating a new entry if the length key is not
    # already in the dictionary or, if the key already exists, appending
    # the word to the corresponding list.
    for word in words:
        key = len(word)

        if key not in words_by_length:
            words_by_length[key] = [word]
        else:
            words_by_length[key].append(word)

    # Create the list we'll ultimately return.
    final_list = []

    # To add to the final_list in ascending order, create a list of
    # sorted keys. We then create and add tuple-ized dictionary entries
    # in order of this list.
    word_keys = words_by_length.keys()

    for word in word_keys:
        pair = (word, words_by_length[word])
        final_list.append(pair)

    return final_list

print sort_by_word_length(["ok", "an", "apple", "a", "day"])

# def get_pirate_talk(phrase):
#     """Translate phrase to pirate talk.

#     Given a phrase, translate each word to the Pirate-speak equivalent.
#     Words that cannot be translated into Pirate-speak should pass through
#     unchanged. Return the resulting sentence.

#     Here's a table of English to Pirate translations:

#     English     Pirate
#     ----------  ----------------
#     sir         matey
#     hotel       fleabag inn
#     student     swabbie
#     boy         matey
#     madam       proud beauty
#     professor   foul blaggart
#     restaurant  galley
#     your        yer
#     excuse      arr
#     students    swabbies
#     are         be
#     lawyer      foul blaggart
#     the         th'
#     restroom    head
#     my          me
#     hello       avast
#     is          be
#     man         matey

#     For example:

#         >>> get_pirate_talk("my student is not a man")
#         'me swabbie be not a matey'

#     You should treat words with punctuation as if they were different
#     words:

#         >>> get_pirate_talk("my student is not a man!")
#         'me swabbie be not a man!'

#     """

#     return ""

# # End of skills. See below for advanced problems.
# # To work on them, set ADVANCED=True at the top of this file.
# ############################################################################


# def adv_get_top_letter(input_string):
#     """Given an input string, return a list of letter(s) which appear(s) the most the input string.

#     If there is a tie, the order of the letters in the returned
#     list should be alphabetical.

#     For example:
#         >>> adv_get_top_letter("The rain in spain stays mainly in the plain.")
#         ['i', 'n']

#     If there is not a tie, simply return a list with one item.

#     For example:
#         >>> adv_get_top_letter("Shake it off, shake it off. Shake it off, Shake it off.")
#         ['f']

#     Spaces do not count as letters.

#     """

#     return ''


# def adv_alpha_sort_by_word_length(words):
#     """Given a list of words, return a list of tuples, ordered by word-length.

#     Each tuple should have two items--a number that is a word-length,
#     and the list of words of that word length. In addition to ordering
#     the list by word length, order each sub-list of words alphabetically.
#     Now try doing it with only one call to .sort() or sorted(). What does the
#     optional "key" argument for .sort() and sorted() do?

#     For example:

#         >>> adv_alpha_sort_by_word_length(["ok", "an", "apple", "a", "day"])
#         [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

#     """

#     return []


# ##############################################################################
# # You can ignore everything below this.

# def print_dict(d):
#     # This method is just used to print dictionaries in key-alphabetical
#     # order, and is only used for our documentation tests. You can ignore it.
#     if isinstance(d, dict):
#         print "{" + ", ".join("%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
#     else:
#         print d


# def sort_pairs(l):
#     # Print sorted list of pairs where the pairs are sorted. This is used only
#     # for documentation tests. You can ignore it.
#     return sorted(sorted(pair) for pair in l)

# if __name__ == "__main__":
#     print
#     import doctest
#     for k, v in globals().items():
#         if k[0].isalpha():
#             if k.startswith('adv_') and not ADVANCED:
#                 continue
#             a = doctest.run_docstring_examples(v, globals(), name=k)
#     print "** END OF TEST OUTPUT"
#     print
