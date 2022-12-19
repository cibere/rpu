from rpu.iterables import chunk

# creating a raw list to chunk
before = [
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
]

# actualling chunking the list, and setting the max size to 5
chunked_data = chunk(before, max_size=5)

# chunk creates a generator object, so we have to flatten it in a list
after = list(chunked_data)

# printing the chunked list
print(after)
