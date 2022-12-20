from __future__ import annotations

from asyncio import get_running_loop
from functools import partial
from inspect import isawaitable as _isawaitable
from typing import TYPE_CHECKING, Any, Awaitable, Callable, TypeVar, Union

if TYPE_CHECKING:
    from typing_extensions import ParamSpec

    P = ParamSpec("P")

    MaybeAwaitableFunc = Callable[P, "MaybeAwaitable[T]"]


T = TypeVar("T")
MaybeAwaitable = Union[T, Awaitable[T]]

__all__ = ["run_in_executor", "execute_func"]


async def run_in_executor(function, *args, **kwargs) -> Any:
    """|coro|

    Runs the given function in a sync executor

    Parameters
    ----------
    function
        The sync function to be executed
    *args
        Any positional args to be passed to the function
    **kwargs
        any kwargs to be passed to the function

    Returns
    ----------
    Any
        Whatever the given function returns
    """

    func = partial(function, *args, **kwargs)
    loop = get_running_loop()
    result = loop.run_in_executor(None, func)
    return result


async def execute_func(
    func: MaybeAwaitableFunc[P, T], /, *args: P.args, **kwargs: P.kwargs
) -> T:
    """Executes the given function as a function or coro (depending on which it is)

    Parameters
    ----------
    func: `MaybeAwaitableFunc[P, T]`
        the function/coro to be executed
    *args: `typing.Any`
        Any positional args to be passed to the function
    **kwargs: `typing.Any`
        And kwargs to be passed to the function

    Returns
    ----------
    Whatever the given function returns
    """

    value = func(*args, **kwargs)

    if _isawaitable(value):
        return await value
    else:
        return value  # type: ignore
