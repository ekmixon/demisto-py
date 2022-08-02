# coding: utf-8

"""
    Demisto API

    This is the public REST API to integrate with the demisto server. HTTP request can be sent using any HTTP-client.  For an example dedicated client take a look at: https://github.com/demisto/demisto-py.  Requests must include API-key that can be generated in the Demisto web client under 'Settings' -> 'Integrations' -> 'API keys'   Optimistic Locking and Versioning\\:  When using Demisto REST API, you will need to make sure to work on the latest version of the item (incident, entry, etc.), otherwise, you will get a DB version error (which not allow you to override a newer item). In addition, you can pass 'version\\: -1' to force data override (make sure that other users data might be lost).  Assume that Alice and Bob both read the same data from Demisto server, then they both changed the data, and then both tried to write the new versions back to the server. Whose changes should be saved? Alice’s? Bob’s? To solve this, each data item in Demisto has a numeric incremental version. If Alice saved an item with version 4 and Bob trying to save the same item with version 3, Demisto will rollback Bob request and returns a DB version conflict error. Bob will need to get the latest item and work on it so Alice work will not get lost.  Example request using 'curl'\\:  ``` curl 'https://hostname:443/incidents/search' -H 'content-type: application/json' -H 'accept: application/json' -H 'Authorization: <API Key goes here>' --data-binary '{\"filter\":{\"query\":\"-status:closed -category:job\",\"period\":{\"by\":\"day\",\"fromValue\":7}}}' --compressed ```  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class FormDisplay(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'body_background_color': 'str',
        'body_font_color': 'str',
        'header_background_color': 'str',
        'header_font_color': 'str',
        'sender': 'str',
        'submit_button_background_color': 'str',
        'submit_button_font_color': 'str',
        'submit_text': 'str'
    }

    attribute_map = {
        'body_background_color': 'bodyBackgroundColor',
        'body_font_color': 'bodyFontColor',
        'header_background_color': 'headerBackgroundColor',
        'header_font_color': 'headerFontColor',
        'sender': 'sender',
        'submit_button_background_color': 'submitButtonBackgroundColor',
        'submit_button_font_color': 'submitButtonFontColor',
        'submit_text': 'submitText'
    }

    def __init__(self, body_background_color=None, body_font_color=None, header_background_color=None, header_font_color=None, sender=None, submit_button_background_color=None, submit_button_font_color=None, submit_text=None):  # noqa: E501
        """FormDisplay - a model defined in Swagger"""  # noqa: E501

        self._body_background_color = None
        self._body_font_color = None
        self._header_background_color = None
        self._header_font_color = None
        self._sender = None
        self._submit_button_background_color = None
        self._submit_button_font_color = None
        self._submit_text = None
        self.discriminator = None

        if body_background_color is not None:
            self.body_background_color = body_background_color
        if body_font_color is not None:
            self.body_font_color = body_font_color
        if header_background_color is not None:
            self.header_background_color = header_background_color
        if header_font_color is not None:
            self.header_font_color = header_font_color
        if sender is not None:
            self.sender = sender
        if submit_button_background_color is not None:
            self.submit_button_background_color = submit_button_background_color
        if submit_button_font_color is not None:
            self.submit_button_font_color = submit_button_font_color
        if submit_text is not None:
            self.submit_text = submit_text

    @property
    def body_background_color(self):
        """Gets the body_background_color of this FormDisplay.  # noqa: E501


        :return: The body_background_color of this FormDisplay.  # noqa: E501
        :rtype: str
        """
        return self._body_background_color

    @body_background_color.setter
    def body_background_color(self, body_background_color):
        """Sets the body_background_color of this FormDisplay.


        :param body_background_color: The body_background_color of this FormDisplay.  # noqa: E501
        :type: str
        """

        self._body_background_color = body_background_color

    @property
    def body_font_color(self):
        """Gets the body_font_color of this FormDisplay.  # noqa: E501


        :return: The body_font_color of this FormDisplay.  # noqa: E501
        :rtype: str
        """
        return self._body_font_color

    @body_font_color.setter
    def body_font_color(self, body_font_color):
        """Sets the body_font_color of this FormDisplay.


        :param body_font_color: The body_font_color of this FormDisplay.  # noqa: E501
        :type: str
        """

        self._body_font_color = body_font_color

    @property
    def header_background_color(self):
        """Gets the header_background_color of this FormDisplay.  # noqa: E501


        :return: The header_background_color of this FormDisplay.  # noqa: E501
        :rtype: str
        """
        return self._header_background_color

    @header_background_color.setter
    def header_background_color(self, header_background_color):
        """Sets the header_background_color of this FormDisplay.


        :param header_background_color: The header_background_color of this FormDisplay.  # noqa: E501
        :type: str
        """

        self._header_background_color = header_background_color

    @property
    def header_font_color(self):
        """Gets the header_font_color of this FormDisplay.  # noqa: E501


        :return: The header_font_color of this FormDisplay.  # noqa: E501
        :rtype: str
        """
        return self._header_font_color

    @header_font_color.setter
    def header_font_color(self, header_font_color):
        """Sets the header_font_color of this FormDisplay.


        :param header_font_color: The header_font_color of this FormDisplay.  # noqa: E501
        :type: str
        """

        self._header_font_color = header_font_color

    @property
    def sender(self):
        """Gets the sender of this FormDisplay.  # noqa: E501


        :return: The sender of this FormDisplay.  # noqa: E501
        :rtype: str
        """
        return self._sender

    @sender.setter
    def sender(self, sender):
        """Sets the sender of this FormDisplay.


        :param sender: The sender of this FormDisplay.  # noqa: E501
        :type: str
        """

        self._sender = sender

    @property
    def submit_button_background_color(self):
        """Gets the submit_button_background_color of this FormDisplay.  # noqa: E501


        :return: The submit_button_background_color of this FormDisplay.  # noqa: E501
        :rtype: str
        """
        return self._submit_button_background_color

    @submit_button_background_color.setter
    def submit_button_background_color(self, submit_button_background_color):
        """Sets the submit_button_background_color of this FormDisplay.


        :param submit_button_background_color: The submit_button_background_color of this FormDisplay.  # noqa: E501
        :type: str
        """

        self._submit_button_background_color = submit_button_background_color

    @property
    def submit_button_font_color(self):
        """Gets the submit_button_font_color of this FormDisplay.  # noqa: E501


        :return: The submit_button_font_color of this FormDisplay.  # noqa: E501
        :rtype: str
        """
        return self._submit_button_font_color

    @submit_button_font_color.setter
    def submit_button_font_color(self, submit_button_font_color):
        """Sets the submit_button_font_color of this FormDisplay.


        :param submit_button_font_color: The submit_button_font_color of this FormDisplay.  # noqa: E501
        :type: str
        """

        self._submit_button_font_color = submit_button_font_color

    @property
    def submit_text(self):
        """Gets the submit_text of this FormDisplay.  # noqa: E501


        :return: The submit_text of this FormDisplay.  # noqa: E501
        :rtype: str
        """
        return self._submit_text

    @submit_text.setter
    def submit_text(self, submit_text):
        """Sets the submit_text of this FormDisplay.


        :param submit_text: The submit_text of this FormDisplay.  # noqa: E501
        :type: str
        """

        self._submit_text = submit_text

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(FormDisplay, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        return (
            self.__dict__ == other.__dict__
            if isinstance(other, FormDisplay)
            else False
        )

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
