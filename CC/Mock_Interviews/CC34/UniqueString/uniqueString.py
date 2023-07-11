def is_unique(string):
    """
    Determine if the given string contains only unique characters.

    Spaces are not considered, and characters are not case sensitive (i.e., 'A' is the same as 'a').

    Args:
        string (str): The input string to check for uniqueness.

    Returns:
        bool: True if the string contains only unique characters (ignoring spaces), False otherwise.
    """

    string = string.lower()
    characters = set()

    for char in string:
        if char == " ":
            continue

        if char in characters:
            return False

        characters.add(char)

    return True
