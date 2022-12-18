from typing import Literal, Optional
from urllib.parse import urlencode

__all__ = ["QueryParams", "Headers", "Route"]


class Parameters:
    __slots__ = ["_internal"]

    def __init__(self, *, raw: dict[str, str] = {}):
        """Creates a parameters instance"""

        self._internal = raw

    def __getitem__(self, key: str) -> Optional[str]:
        return self._internal.get(key)

    def __setitem__(self, key: str, value: str) -> None:
        if not isinstance(key, str):
            raise TypeError(f"Expected key to be str, got {key.__class__} instead")
        if not isinstance(value, str):
            raise TypeError(f"Expected value to be str, got {value.__class__} instead")

        self._internal[key] = value

    def unpack(self) -> dict:
        """Unpacks the parameters into a dict

        Returns
        ----------
        dict[str, str]
        """

        return self._internal


class QueryParams(Parameters):
    def unpack(self) -> str:
        """Unpacks the parameters into a form that can be used in a url

        Returns
        ----------
        str
        """

        return urlencode(self._internal)


class Headers(Parameters):
    pass


class Route:
    __slots__ = ["method", "endpoint", "headers", "query_params"]

    def __init__(
        self,
        *,
        method: Literal["POST", "GET"],
        endpoint: str,
        headers: Optional[Headers] = None,
        query_params: Optional[QueryParams] = None,
    ):
        """Creates a route instance

        Parameters
        ----------
        method: typing.Literal["POST", "GET"]
            The method for the request
        endpoint: `str`
            the endpoint for the request
        headers: Optional[`Headers`]
            The headers
        query_params: Optional[`QueryParams`]
            the query params

        Attributes
        ----------
        method: typing.Literal["POST", "GET"]
            The method for the request
        endpoint: `str`
            the endpoint for the request
        headers: `Headers`
            The headers
        query_params: `QueryParams`
            the query params
        """

        self.method = method
        self.endpoint = endpoint
        self.headers = headers or Headers()
        self.query_params = query_params or QueryParams()
