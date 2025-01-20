from pathlib import Path
import click
import shutil


@click.command()
@click.option(
    "--directory",
    type=click.Path(exists=True, file_okay=False, dir_okay=True, readable=True),
    default=f"{Path.cwd()}\\task1",
    help="DEFAULT_DIRECTORY-> The directory to process (default: folder -task1 in current working directory). USAGE: run task1.py to read the contents of default folder that i created for homework or run task1.py --directory /path/to/yours/folder",
)
@click.option(
    "--destination_directory",
    type=click.Path(exists=True, file_okay=False, dir_okay=True, readable=True),
    default=f"{Path.cwd()}\\dist",
    help="DESTINATION_DIRECTORY-> The directory to copy files from (default: folder -dist in current working directory). USAGE: run task1.py --custom_directory /path/to/yours/folder",
)
def read_folder(directory, destination_directory):
    """Read the contents of a folder."""
    print("for help run: python task1.py --help")
    source_path = Path(directory)
    destination_path = Path(destination_directory)

    print(
        f"Reading the contents of the folder: {source_path}, Destination directory: {destination_path}"
    )

    if not source_path.exists():
        print("The folder does not exist.")
        return

    if not any(source_path.iterdir()):
        print("The folder is empty.")
        return
    destination_path.mkdir(parents=True, exist_ok=True)

    for file in source_path.rglob("*"):
        if file.is_file():
            file_extention = file.suffix[1:]
            print(f"File: {file.name}, {file_extention}")
            if not file_extention:
                file_extention = "no_extension"
            folder_name = destination_path / file_extention
            folder_name.mkdir(exist_ok=True)
            destination = folder_name / file.name
            if destination.exists():
                destination = destination.with_name(
                    f"{destination.stem}_copy{destination.suffix}"
                )
            shutil.copy2(file, destination)


if __name__ == "__main__":
    read_folder()
