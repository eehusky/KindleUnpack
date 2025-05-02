#!/usr/bin/env python
# vim:fileencoding=UTF-8:ts=4:sw=4:sta:et:sts=4:ai
from loguru import logger

logger.disable(__name__)

from .kindleunpack import unpackBook as unpack_book
