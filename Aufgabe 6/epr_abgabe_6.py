__author__ = "Chris"


def differences(values):
    """This function calculates the differences between the values in a list.
       This function is also iterative.

    Args:
        values: A list of values.

    Returns:
        A list of differences between the values in the list.
    """
    result = []
    for i in range(len(values) - 1):
        result.append(values [i+1] - values[i])
    return result


def r_differences(values):
    """This function calculates the differences between the values in a list.
       This function is also recursive.

    Args:
        values: A list of values.

    Returns:
        A list of differences between the values in the list.
    """
    if len(values) == 1:
        return []
    else:
        return [values[1] - values[0]] + r_differences(values[1:])


def palindrome(word):
    """This function checks if a word is a palindrome.
       This function is recursive.

    Args:
        word: A string.

    Returns:
        True if the word is a palindrome, False otherwise.
    """
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    return palindrome(word[1:-1])


def i_palindrome(word):
    """This function checks if a word is a palindrome.
       This function is iterative.

    Args:
        word: A string.

    Returns:
        True if the word is a palindrome, False otherwise.
    """
    for i in range(len(word)//2):
        if word[i] != word[-i-1]:
            return False
    return True

if __name__ == "__main__":
    print(differences([3, 6, 9, 12, 15, 18, 21, 24, 27]))  # [3, 3, 3, 3, 3, 3, 3, 3]
    print(r_differences([2, 4, 9, 8, 10, 15, 12, 18, 20]))  # [2, 5, -1, 2, 5, -3, 6, 2]
    print(palindrome("otto"))  # True
    print(i_palindrome("anna"))  # True
    print(palindrome("kevin"))  # False
    print(i_palindrome("chantal"))  # False
    