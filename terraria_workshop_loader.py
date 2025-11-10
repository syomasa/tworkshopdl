import pathlib
import argparse
import sys
import subprocess
import os

from subprocess import CalledProcessError


TERRARIA_GAME_ID = "105600"


class CLIParser(argparse.ArgumentParser):
    def __init__(self):
        super().__init__(
            prog="tworkshopdl",
            description=(
                "Cli utility for downloading terraria workshop content "
                "such as mods and texturepacks"
            ),
        )

        self.add_argument(
            "--download-dir",
            type=str,
            help=(
                "Path to download dir. Default is steam workshop folder "
                "on linux .local/share/Steam/steamapps/workshop/content "
                "and on windows <STEAM_INSTALL_PATH>\\steamapps\\workshop\\content. "
                "See steamcmd documentation for more information"
            ),
            default="",
            metavar="PATH",
        )

        self.add_argument(
            "-p",
            "--parents",
            action="store_true",
            help="Creates parent directories if they are not existing and --download-dir is specified",
        )

        self.add_argument(
            "workshop_id", type=str, help="Id to workshop file you want to download"
        )

    def parse_args(self, args: list[str] | None = None):
        args = super().parse_args(args)

        if args.parents and not args.download_dir:
            print(
                "ERROR: --parents is only supported when used with --download-dir",
                file=sys.stderr,
            )
            sys.exit(1)

        return args


def handle_path(args):
    if args.download_dir:
        args.download_dir = pathlib.Path(args.download_dir).resolve()

    if args.download_dir and not args.parents:
        if not os.path.exists(args.download_dir):
            print(f"ERROR: Path ({args.download_dir}) doesn't exist", file=sys.stderr)
            sys.exit(1)

    if args.download_dir and args.parents:
        try:
            path = pathlib.Path(args.download_dir)
            path.mkdir(parents=True, exist_ok=True)
        except FileExistsError:
            print(
                "ERROR: Directory path exists already as file. Please use another path",
                file=sys.stderr,
            )
            sys.exit(1)

    return args


def run_steamcmd(args):
    command = ["steamcmd"]
    if args.download_dir:
        command.extend(["+force_install_dir", str(args.download_dir)])

    command.extend(
        [
            "+login",
            "anonymous",
            "+workshop_download_item",
            TERRARIA_GAME_ID,
            str(args.workshop_id),
            "+exit",
        ]
    )

    try:
        subprocess.run(command, shell=False, check=True)
    except CalledProcessError as process_error:
        # TODO: Proper error messages
        print(process_error, file=sys.stderr)
        sys.exit(1)
    except FileNotFoundError:
        print(
            "ERROR: Could not find steamcmd. Are you sure you have steam installed and in PATH",
            file=sys.stderr,
        )
        sys.exit(1)


if __name__ == "__main__":
    parser = CLIParser()
    args = parser.parse_args()
    args = handle_path(args)
    run_steamcmd(args)
    sys.exit(0)
