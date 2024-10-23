#!/usr/bin/python3
def multiple_returns(sentence):
    """Returns a tuple with the length of a string and its first character."""
    if sentence == "":
        return (0, None)  # Return length 0 and None if the sentence is empty
    return (len(sentence), sentence[0])  # Return length and first character
