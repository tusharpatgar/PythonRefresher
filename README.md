# Python Refresher

A small learning repository containing Python fundamentals, practice snippets, and examples collected while revisiting the language.

## Topics covered

The current examples include:

- Basic output, variables, types, and string operations
- Functions, parameters, return values, and type hints
- Conditional logic, loops, and recursion
- String traversal and cleanup
- Simple numeric and text exercises

Most exercise snippets are intentionally commented out so they can be selected and practiced individually. Review a file before running it: these are learning notes, not a packaged application or a test suite.

## Repository layout

```text
Examples/
  controlflow.py   # conditions, loops, recursion
  methods.py       # strings, iteration, functions
  print.py         # output, variables, functions, strings
src/
  pythonrefresher/ # minimal package scaffold
hello.py           # standalone heartbeat experiment
pyproject.toml     # project metadata
uv.lock            # uv lockfile
```

## Requirements

- Python 3.12 or later
- [uv](https://docs.astral.sh/uv/) is used by the project configuration

## Run an example

From the repository root:

```bash
python Examples/controlflow.py
python Examples/methods.py
```

The files contain commented practice snippets. Uncomment the exercise you want to try, then run the file again.

To run the minimal package entry point with uv:

```bash
uv run python -c "from pythonrefresher import main; main()"
```

## Development notes

- Keep each example focused on one Python concept.
- Prefer descriptive function and variable names.
- Add expected input/output examples when introducing a new exercise.
- Do not commit virtual environments, bytecode, editor files, or Jupyter checkpoint folders.

## License

No license is currently specified for this repository. Contact the repository owner before reusing its contents.
