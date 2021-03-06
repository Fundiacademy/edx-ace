"""
:mod:`edx_ace.recipient` contains :class:`Recipient`, which captures all targeting
information needed to deliver a message to some user.
"""
import attr

from edx_ace.serialization import MessageAttributeSerializationMixin


@attr.s
class Recipient(MessageAttributeSerializationMixin):
    """
    The target for a message.

    Arguments:
        username (str): The username of the intended recipient.
        email_address (str): The email address of the intended recipient. Optional.
    """
    username = attr.ib()
    email_address = attr.ib(default=None)
