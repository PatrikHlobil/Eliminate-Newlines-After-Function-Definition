import re
from pathlib import Path
from typing import Union

import click


def eliminate_newlines_after_function_definition_in_string(code: str) -> str:
    """Eliminates all newlines after the function definition in a string, e.g.

    def foo(a):

        return a + 1

    will become:

    def foo(a):
        return a+1"""

    return re.sub(
        pattern=r"(def \w+\([^:]*\):)(\s*)\n",
        repl=r"\1\n",
        string=code,
        flags=re.M | re.S,
    )


def eliminate_newlines_after_function_definition_in_file(
    path: Path, check: bool = False
) -> bool:
    """Eliminates all newlines after the function definition in a file, e.g.

    def foo(a):

        return a + 1

    will become:

    def foo(a):
        return a+1

    If <check> = False, the file will not be touched and the return code indicated
    if the file would have to be formatted.

    Returns 0 if nothing has been changes and 1 otherwise."""

    with open(path) as f:
        content = f.read()

    content_formatted = eliminate_newlines_after_function_definition_in_string(
        code=content
    )

    if content_formatted != content:
        if not check:
            with open(path, "w") as f:
                f.write(content_formatted)
            click.echo(click.style(f"Reformatted file {str(path)}.", fg="yellow"))
        else:
            click.echo(click.style(f"Would reformat file {str(path)}.", fg="yellow"))
        return 1
    else:
        click.echo(
            click.style(f"File {str(path)} is already formatted. Skipping.", fg="green")
        )
        return 0


def eliminate_newlines_after_function_definition_in_file_or_directory(
    path: Path, check: bool = False
) -> bool:
    """Eliminates all newlines after the function definition in either a file or a
    directory (recursively in this case), e.g.

    def foo(a):

        return a + 1

    will become:

    def foo(a):
        return a+1

    If <check> = False, the file(s) will not be touched and the return code indicated
    if the file would have to be formatted.

    Returns 0 if nothing has been changes and 1 otherwise."""

    if path.is_file():
        return eliminate_newlines_after_function_definition_in_file(path, check=check)
    elif path.is_dir():
        formatted = []
        for p in path.glob("**/*.py"):
            formatted.append(
                eliminate_newlines_after_function_definition_in_file(p, check=check)
            )
        return max(formatted)
