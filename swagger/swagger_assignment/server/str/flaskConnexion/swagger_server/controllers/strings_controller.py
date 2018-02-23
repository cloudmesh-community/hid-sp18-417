import connexion
import six

from swagger_server import util


def add_str(str):  # noqa: E501
    """Add the string

    This method will add the string from the query param to the data collection # noqa: E501

    :param str: The string to be processed
    :type str: str

    :rtype: None
    """
    return 'do some magic!'


def fetch_str(id):  # noqa: E501
    """Get the string by id

    This method fetch the string by id # noqa: E501

    :param id: The string to be processed
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def match_str(subStr, str):  # noqa: E501
    """String Match

    Find the matching data of two strings # noqa: E501

    :param subStr: The string to be matched
    :type subStr: str
    :param str: The string to be processed
    :type str: str

    :rtype: None
    """
    return 'do some magic!'


def parse_str(str):  # noqa: E501
    """List 1. all the unique characters; 2. numeric digits count

    Get all the unique characters in the string listed in an array and the total number of numeric digits in the string # noqa: E501

    :param str: The string to be processed
    :type str: str

    :rtype: None
    """
    return 'do some magic!'


def replace_str(oldStr, newStr, str):  # noqa: E501
    """Replace one old str with the new one

    Replace the old str with the new one with in a new string. # noqa: E501

    :param oldStr: Sub string to be replaced
    :type oldStr: str
    :param newStr: Sub string replacing the old value
    :type newStr: str
    :param str: The string to be processed
    :type str: str

    :rtype: None
    """
    return 'do some magic!'
