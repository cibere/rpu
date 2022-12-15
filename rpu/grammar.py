from typing import Union

__all__ = ["Plural", "possessive", "ordinal"]


class Plural:
    def __init__(self, num: Union[int, float], /):
        """Returns the plural version of the given text

        Parameters
        ----------
        num: Union[`int`, `float`]
            the number you want to use for getting the plural of text

        Notes
        ----------
            Is this giving an incorrect plural version? Create an issue on the github repo (or PR it yourself :D)

        Useage
        ----------
        Example: `Plural(5):the_text` -> `5 the_texts`
        """

        self.num = num

    def __format__(self, text: str) -> str:
        if abs(self.num) != 1:
            text += "s"

        return f"{self.num} {text}"


def possessive(text: str, /) -> str:
    """Returns the possessive version of the given text

    Parameters
    ----------
    text: `str`
        The text you want the possessive version of

    Returns
    ----------
    str
        The possessive version of the text
    """

    if text.endswith("s"):
        text += "'"
    else:
        text += "'s"

    return text


def ordinal(number: int, /) -> str:
    """Returns the ordinal version of a number

    Parameters
    ----------
    number: `int`
        the number to be turned ordinal

    Returns
    ----------
    str
        the ordinal version

    Examples
    ----------
    >>> ordinal(5)
    ... 5th

    >>> ordinal(2)
    ... 2nd
    """

    return f"{number}{'tsnrhtdd'[(number//10%10!=1)*(number%10<4)*number%10::4]}"


def int_to_word(number: int, /) -> str:
    """Returns the word version of an integer

    Parameters
    ----------
    number: `int`
        the number to be turned into its word version

    Notes
    ----------
        If number is 10 or above, it will return its number form

    Returns
    ----------
    str
        the word version

    Examples
    ----------
    >>> int_to_word(5)
    ... five

    >>> int_to_word(10)
    ... 10
    """

    return {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
    }.get(number, str(number))
