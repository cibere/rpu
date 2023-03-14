from __future__ import annotations

import asyncio
from functools import partial
from inspect import isawaitable as _isawaitable
from typing import (
    TYPE_CHECKING,
    Any,
    Awaitable,
    Callable,
    Coroutine,
    TypeVar,
    Union,
    overload,
)

if TYPE_CHECKING:
    from typing_extensions import ParamSpec

    P = ParamSpec("P")

    MaybeAwaitableFunc = Callable[P, "MaybeAwaitable[T]"]


T = TypeVar("T")
MaybeAwaitable = Union[T, Awaitable[T]]

__all__ = ["run_in_executor", "execute_func", "asyncio_task"]


@overload
def asyncio_task(
    *,
    name: str | None = ...,
) -> Callable[
    [Callable[P, Coroutine[Any, Any, None]]], Callable[P, Coroutine[Any, Any, None]]
]:
    ...


@overload
def asyncio_task(
    func: Callable[P, Coroutine[Any, Any, None]],
) -> Callable[P, Coroutine[Any, Any, None]]:
    ...


def asyncio_task(
    func: Callable[P, Coroutine[Any, Any, None]] | None = None,
    /,
    *,
    name: str | None = None,
) -> Callable[
    [Callable[P, Coroutine[Any, Any, None]]], Callable[P, Coroutine[Any, Any, None]]
] | Callable[P, Coroutine[Any, Any, None]]:
    """Turns the function it's used on, into an asyncio task which gets started whenever the coroutine is executed.

    Parameters
    ----------
    func
        This is here so you can use the decorator without calling it, you should not pass anything for this.
    name
        When its called, you can pass a name kwarg which will be used as the task's name when creating it.

    Returns
    ----------
    None
        Nothing, since tasks can't return anything

    Examples
    ----------
    ```
    @asyncio_task
    async def foo(bar: str):
        ...
    ```
    ```
    @asyncio_task(name='foo-12')
    async def foo(bar: str):
        ...
    ```
    """

    def decorator(
        func: Callable[P, Coroutine[Any, Any, None]]
    ) -> Callable[P, Coroutine[Any, Any, None]]:
        async def inner(*args: P.args, **kwargs: P.kwargs) -> None:
            asyncio.create_task(func(*args, **kwargs), name=name)

        return inner

    return decorator(func) if func else decorator


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
    loop = asyncio.get_running_loop()
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
