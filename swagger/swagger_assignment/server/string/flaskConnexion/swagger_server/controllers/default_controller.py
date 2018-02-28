import connexion
import six

from swagger_server.models.output import OUTPUT  # noqa: E501
from swagger_server import util


def add_string_str_get(str):  # noqa: E501
    """add_string_str_get

     # noqa: E501

    :param str: String to be added
    :type str: str

    :rtype: OUTPUT
    """
    return str


def fetch_string_id_get(id):  # noqa: E501
    """fetch_string_id_get

     # noqa: E501

    :param id: id for which string to be retreived
    :type id: str

    :rtype: OUTPUT
    """
    return id
