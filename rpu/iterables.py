from typing import Any, Iterable, Optional

__all__ = ["chunk", "get"]


def chunk(iterable: Iterable, max_size: int) -> Iterable[list[Any]]:
    """|iterable|

    Chunks the given iterable into chunks of the given size

    Parameters
    ----------
    iterable: `typing.Iterable`
        The iterable you want to chunk
    max_size: `int`
        the max size of the chunks
    """

    if max_size <= 0:
        raise TypeError("max_size must be bigger than 0")

    final = []
    current = 0

    for item in iterable:
        if current == max_size:
            yield final
            final = []
            current = 0

        final.append(item)
        current += 1

    if final:
        yield final


def get(iterable: Iterable, /, **attrs: Any) -> Any:
    """Gets an item from the given iterable with sertain attributes

    Parameters
    ----------
    iterable: `typing.Iterable`
        The item you want to be iterated through
    **attrs: `typing.Any`
        The attribute(s) to check for
    """

    for item in iterable:
        for attr in attrs.keys():
            if hasattr(item, attr):
                if getattr(item, attr) == attrs[attr]:
                    return item

    return None
