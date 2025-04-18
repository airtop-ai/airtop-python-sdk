# This file was auto-generated by Fern from our API Definition.

from ..core.api_error import ApiError
from ..types.error_model import ErrorModel


class UnauthorizedError(ApiError):
    def __init__(self, body: ErrorModel):
        super().__init__(status_code=401, body=body)
