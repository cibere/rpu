from typing import Any, AsyncIterable, Optional

__all__ = ["chunk", "get"]


async def chunk(iterable: AsyncIterable, max_size: int) -> AsyncIterable[list[Any]]:
    """|async-iterable|

    Chunks the given iterable into chunks of the given size

    Parameters
    ----------
    iterable: `typing.AsyncIterable`
        The iterable you want to chunk
    max_size: `int`
        the max size of the chunks
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


async def get(iterable: AsyncIterable, /, **attrs: Any) -> Optional[Any]:
    """|coro|

    Gets an item from the given iterable with sertain attributes

    Parameters
    ----------
    iterable: `typing.AsyncIterable`
        The item you want to be iterated through
    **attrs: `typing.Any`
        The attribute(s) to check for
    """

    async for item in iterable:
        for attr in attrs.keys():
            if hasattr(item, attr):
                if getattr(item, attr) == attrs[attr]:
                    return item

    return None
