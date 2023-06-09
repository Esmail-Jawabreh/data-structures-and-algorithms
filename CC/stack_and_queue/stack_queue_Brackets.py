def validate_brackets(string):
    """
    Validates if the brackets in a given string are balanced and properly matched.

    Args:
        string (str): The string containing brackets to be validated.

    Returns:
        bool: True if all brackets are balanced and properly matched, False otherwise.
    """
    
    stack = []
    opening_brackets = {"(", "[", "{"}
    closing_brackets = {")", "]", "}"}
    matching_brackets = {"(": ")", "[": "]", "{": "}"}

    for i, char in enumerate(string):
        if char in opening_brackets:
            stack.append((char, i))
        elif char in closing_brackets:
            if not stack:
                print(f"Error: Unmatched closing '{char}' at position {i}.")
                return False
            last_opening_bracket, position = stack.pop()
            if matching_brackets[last_opening_bracket] != char:
                print(
                    f"Error: Mismatched closing '{char}' at position {i}. Expected '{matching_brackets[last_opening_bracket]}' instead."
                )
                return False

    if stack:
        last_opening_bracket, position = stack.pop()
        print(
            f"Error: Unmatched opening '{last_opening_bracket}' at position {position}."
        )
        return False

    return True
