def left_join(synonyms, antonyms):
    """
    Perform a LEFT JOIN operation on two hashmaps.

    Arguments:
    - synonyms (dict): A hashmap with word strings as keys and synonyms as values.
    - antonyms (dict): A hashmap with word strings as keys and antonyms as values.

    Returns:
    - list: The result of the LEFT JOIN operation as a list of lists. Each inner list
            contains the key from the 'synonyms' hashmap, the corresponding synonym,
            and the corresponding antonym (if it exists in the 'antonyms' hashmap).
    """
    result = []
    for key in synonyms:
        row = [key, synonyms[key], antonyms.get(key)]
        result.append(row)
    return result
