# Update Log

## 0.0.2 (so far)

**Breaking Changes**

- `name`, `description`, and `brief` in `rpu.cli.ConsoleClient` are not optional. If `name` is not given, it will be the functions name. If `description` is not given, it will be the commands docstring.
- all async stuff have been moved under the `rpu.async_` folder

**Additions**

- `rpu.consts`
- `rpu.async_.specific`
- `rpu.async_.iterables`
- `rpu.grammar.ordinal`

**Bug Fixes**

- Fixed bug where default help cmd in cli would not show description if brief was an empty string
- Fixed bug where pylance would yell at you when chunking
- fixed bug with `get` erroring when you try to use what it finds

## 0.0.1

**Breaking Changes**

None

**Additions**

- `rpu.grammar`
- `rpu.async_`
- `rpu.iterables`
- docs
- `rpu.cli`
- CLI commands

**Bug Fixes**

None
