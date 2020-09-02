from pathlib import Path
import sys
import click

from .core import (
    eliminate_newlines_after_function_definition_in_file_or_directory,
)


@click.command()
@click.argument("paths", required=True, nargs=-1)
@click.option(
    "--check",
    help="Don't write the files back, just return the status.",
    is_flag=True,
)
def cli(paths, check):
    """This CLI formats Python code in such a way that after the function definition
    header all newlines will be deleted.

    Return code 0 means nothing would change.  Return code 1 means some files would be reformatted. Return code 123 means there was an internal error.""
    pass.

    Passed PATHS can be either files or directories. In the latter case, all files in the
    folders will be formatted recursively.
    """
    try:
        paths = [Path(path) for path in paths]
        changes = []
        for path in paths:
            if path.is_file() and str(path).endswith(".py"):
                pass
            elif path.is_dir():
                pass
            else:
                raise ValueError(
                    f"PATH '{str(path)}' is neither a Python-file or directory."
                )
            c = eliminate_newlines_after_function_definition_in_file_or_directory(
                path=path, check=check
            )
            changes.append(c)
        sys.exit(max(changes))
    except Exception as exc:
        click.echo(click.style(str(exc), fg="red"))
        sys.exit(123)


if __name__ == "__main__":
    cli()
