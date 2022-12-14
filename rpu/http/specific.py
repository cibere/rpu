from typing import Literal

__all__ = ["Route"]


class Route:
    __slots__ = ["method", "endpoint"]

    def __init__(
        self,
        *,
        method: Literal["POST", "GET", "DELETE", "PUT"],
        endpoint: str,
    ):
        """Creates a route instance

        Parameters
        ----------
        method: typing.Literal["POST", "GET"]
            The method for the request
        endpoint: `str`
            the endpoint for the request

        Attributes
        ----------
        method: typing.Literal["POST", "GET"]
            The method for the request
        endpoint: `str`
            the endpoint for the request
        """

        self.method = method
        self.endpoint = endpoint
