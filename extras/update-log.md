# Update Log

## 1.2.0 (so far)

**Breaking Changes**

- Removed `chars`

**Additions**

- `rpu.async_.specific.asyncio_task`

**Bug Fixes**

None

## 1.1.0

**Breaking Changes**

- Removed built in pypi-like system

**Additions**

None

**Bug Fixes**

None

## 1.0.0

**Breaking Changes**

- removed `numbers.int_to_word` and `numbers.word_to_int`
- removed `http.QueryParams`, `http.Headers`
- `rpu.http` is now a folder instead of a file
- `http.Route` has been moved to `rpu.http.specific.Route`

**Additions**

- `rpu.http.codes.ClientErrorHTTPCodes`, `rpu.http.codes.InfoHTTPCodes`, `rpu.http.codes.RedirectHTTPCodes`, `rpu.http.codes.ServerErrorHTTPCodes`, `rpu.http.codes.SuccessHTTPCodes`, `rpu.http.codes.HTTPCodes`

**Bug Fixes**

None

## 0.0.3

**Breaking Changes**

- Support for python `3.8` has been dropped
- The `text/number` arg in `rpu.grammar.Plural`, `rpu.grammar.possessive`, `rpu.grammar.ordinal`, and `rpu.numbers.int_to_word` is now positional only

**Additions**

- Added TypeVars to `rpu.async_.iterables` and `rpu.iterables`
- `rpu.numbers`
- `rpu.dicts`
- `rpu.http`
- `rpu.objects`
- `rpu.async_.specific.execute_func`
- `rpu.chars`

**Bug Fixes**

- Fixed bug where CLI command always returned cmd not found
- fixed bug where pylance yelled at `rpu.cli`

## 0.0.2

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
