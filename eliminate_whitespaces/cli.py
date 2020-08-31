from pathlib import Path
import sys
import click

from .eliminare_whitespaces import (
    eliminate_newlines_after_function_definition_in_file_or_directory,
)


@click.command()
@click.argument(
    "path",
    required=True,
)
@click.option(
    "--check",
    help="Don't write the files back, just return the status.",
    is_flag=True,
)
def cli(path, check):
    """This CLI formats Python code in such a way that after the function definition
    header all newlines will be deleted.

    Return code 0 means nothing would change.  Return code 1 means some files would be reformatted. Return code 123 means there was an internal error.""
    pass.

    Passed PATH can be either a file or a directory. In the latter case, all files in the
    folder will be formatted recursively.
    """
    try:
        path = Path(path)
        if path.is_file() and str(path).endswith(".py"):
            pass
        elif path.is_dir():
            pass
        else:
            raise ValueError(
                f"PATH '{str(path)}' is neither a Python-file or directory."
            )

        changed = eliminate_newlines_after_function_definition_in_file_or_directory(
            path=path, check=check
        )
        sys.exit(changed)
    except Exception as exc:
        click.echo(click.style(str(exc), fg="red"))
        sys.exit(123)


if __name__ == "__main__":
    cli()
