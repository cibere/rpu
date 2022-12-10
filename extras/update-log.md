# Update Log

## 0.0.2 (so far)

**Breaking Changes**

- `name`, `description`, and `brief` in `rpu.cli.ConsoleClient` are not optional. If `name` is not given, it will be the functions name. If `description` is not given, it will be the commands docstring.

**Additions**

None

**Bug Fixes**

- Fixed bug where default help cmd in cli would not show description if brief was an empty string

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
