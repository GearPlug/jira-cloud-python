class BaseError(Exception):
    def __init__(self, message, response, *args, **kwargs):
        super().__init__(message, *args, **kwargs)
        self.response = response


class UnknownError(BaseError):
    pass


class InvalidIDError(BaseError):
    pass


class NotFoundIDError(BaseError):
    pass


class NotAuthenticatedError(BaseError):
    pass


class PermissionError(BaseError):
    pass
