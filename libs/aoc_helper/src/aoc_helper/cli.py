import importlib.metadata
import importlib.resources
import platform
from pathlib import Path
from typing import Any

import click


def get_version(ctx: click.Context, _param: click.Parameter, value: Any):
    if not value or ctx.resilient_parsing:
        return

    aoc_helper_version = importlib.metadata.version("aoc_helper")
    click.echo(
        f"Python {platform.python_version()}\naoc_helper {aoc_helper_version}",
        color=ctx.color,
    )
    ctx.exit()


version_option = click.Option(
    ["--version"],
    help="Show the aoc_helper version.",
    expose_value=False,
    callback=get_version,
    is_flag=True,
    is_eager=True,
)


@click.command("create", short_help="Create files for a new day's puzzle.")
@click.option("--day", "-d", help="The day number.", required=True, type=int)
def create_command(day: int):
    if not 1 <= day <= 25:
        raise click.BadParameter("--day/-d must be within [1, 25].")

    root_dir = Path.cwd()
    data_dir = root_dir / "data"
    script_dir = root_dir / "python"

    if not data_dir.exists():
        raise click.UsageError("'data/' not found in the current directory.")
    if not script_dir.exists():
        raise click.UsageError("'python/' not found in the current directory.")

    data_path = data_dir / f"day{day}.txt"
    script_path = script_dir / f"day{day}.py"

    if data_path.exists():
        raise click.UsageError(f"{data_path} exists.")
    if script_path.exists():
        raise click.UsageError(f"{script_path} exists.")

    with open(data_path, "w") as outfile:
        _ = outfile.write("sample data")
    with open(script_path, "w") as outfile:
        content = importlib.resources.read_text(
            "aoc_helper", "script_template.py"
        ).format(data_file=data_path.name)
        _ = outfile.write(content)


cli = click.Group(name="aoc", help="Advent of Code helper.", params=[version_option])
cli.add_command(create_command)


def main():
    cli.main()


if __name__ == "__main__":
    main()
