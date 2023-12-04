#!/usr/bin/python3

def multiple_returns(sentence):
    """
    Returns a pair with the length of a string and its first character.
    
    Args:
        sentence: Input string.
        
    Returns:
        A pair containing the length of the string and its first character.
    """
    # Check if the sentence is not empty
    if len(sentence) > 0:
        return len(sentence), sentence[0]
    else:
        # Return None for the first character if the string is empty
        return len(sentence), None

