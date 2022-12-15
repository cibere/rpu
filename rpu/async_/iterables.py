from typing import Any, AsyncIterable, Optional

__all__ = ["chunk", "get"]
from typing import TypeVar

T = TypeVar("T")


async def chunk(iterable: AsyncIterable[T], max_size: int) -> AsyncIterable[list[T]]:
    """|async-iterable|

    Chunks the given iterable into chunks of the given size

    Parameters
    ----------
    iterable: `typing.AsyncIterable`
        The iterable you want to chunk
    max_size: `int`
        the max size of the chunks

    Notes
    ----------
        If the given iterable is sync, use `rpu.iterables.chunk` instead
    """

    if max_size <= 0:
        raise TypeError("max_size must be bigger than 0")

    final = []
    current = 0

    async for item in iterable:
        if current == max_size:
            yield final
            final = []
            current = 0

        final.append(item)
        current += 1

    if final:
        yield final


async def get(iterable: AsyncIterable[T], /, **attrs: Any) -> Optional[T]:
    """|coro|

    Gets an item from the given iterable with sertain attributes

    Parameters
    ----------
    iterable: `typing.AsyncIterable`
        The item you want to be iterated through
    **attrs: `typing.Any`
        The attribute(s) to check for

    Notes
    ----------
        If the given iterable is sync, use `rpu.iterables.get` instead
    """

    async for item in iterable:
        for attr in attrs.keys():
            if hasattr(item, attr):
                if getattr(item, attr) == attrs[attr]:
                    return item

    return None
