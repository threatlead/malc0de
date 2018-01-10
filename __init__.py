from .malc0de import Malcode
import logging
from logging import NullHandler

logging.getLogger(__name__).addHandler(NullHandler())
