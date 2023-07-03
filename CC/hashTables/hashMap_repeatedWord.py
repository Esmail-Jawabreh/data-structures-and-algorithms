def repeated_word(input_string):
    """
    Find the first word to occur more than once in a string.

    Arguments:
    - input_string: A string in which to find the repeated word.

    Returns:
    - The first word that occurs more than once in the input string, or None if no word is repeated.
    """

    cleaned_string = "".join(
        char.lower() if char.isalnum() else " " for char in input_string
    )

    words = cleaned_string.split()

    word_count = {}

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
        if word_count[word] > 1:
            return word

    return None
