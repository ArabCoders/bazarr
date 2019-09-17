# coding=utf-8
from __future__ import absolute_import
from subliminal import ProviderError


class TooManyRequests(ProviderError):
    """Exception raised by providers when too many requests are made."""
    pass


class APIThrottled(ProviderError):
    pass
