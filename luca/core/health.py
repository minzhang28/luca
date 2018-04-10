import logging

from ..util.util import json_response

logger = logging.getLogger(__name__)


def health():
    return json_response(status=200)
