class WholeBiteException(Exception):
    """Base exception for WholeBite AI."""
    pass


class PromptNotFound(WholeBiteException):
    pass


class JSONParsingError(WholeBiteException):
    pass


class LLMResponseError(WholeBiteException):
    pass


class ValidationError(WholeBiteException):
    pass