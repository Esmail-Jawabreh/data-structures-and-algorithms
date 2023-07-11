def most_common_word(book):
    """
    Determines the most common word in a book.

    The function takes a string representing a book as an argument and returns
    the word that appears most frequently. The word count is case-insensitive,
    meaning words like 'Cat', 'CAT', and 'cat' are considered the same. Punctuation
    is ignored, and spaces are not counted as words.

    Args:
        book (str): A string representing the book.

    Returns:
        str: The most common word in the book.
    """
    words = book.lower().split()
    word_freq = {}

    for word in words:
        word = word.strip(".,!?")

        if not word:
            continue

        word_freq[word] = word_freq.get(word, 0) + 1

    most_common = None
    highest_freq = 0

    for word, freq in word_freq.items():
        if freq > highest_freq:
            most_common = word
            highest_freq = freq

    return most_common
