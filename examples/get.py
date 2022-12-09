from rpu.iterables import get


# creating a temp class with a `index` class
class Foo:
    def __init__(self, index):
        self.index = index


# creating a raw class
raw = [Foo(0), Foo(1), Foo(2), Foo(3)]

# finding the item with an index of 5
found = get(raw, index=5)

# printing the found items index
print(found.index)
