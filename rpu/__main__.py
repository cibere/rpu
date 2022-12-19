import inspect
import os
import platform
import shutil
import sys
import webbrowser

import rpu

from .cli import ConsoleClient

client = ConsoleClient()


@client.command(
    name="version",
    description="gives you the version of rpu you are running",
    brief="gives you the version of rpu your using",
    aliases=["v"],
)
def cmd_version():
    print(rpu.__version__)


@client.command(
    name="docs",
    description="opens rpu's documentation. If your using alpha/beta, latest docs will be brought up. If your using final then stable docs will be brought up.",
    brief="opens rpus docs",
    aliases=["d"],
)
def cmd_docs():
    version = "stable" if rpu.version_info.releaselevel == "final" else "latest"

    print(f"Opening the {version} docs in your browser")
    webbrowser.open(f"https://rpu.cibere.dev/{version}/index")


@client.command(
    name="system-info",
    description="gives you system information. Specifically rpu version, python version, and os",
    brief="gives you system info",
    aliases=["os", "s"],
)
def cmd_system_info():
    info = {}

    info["python"] = "v{0.major}.{0.minor}.{0.micro}-{0.releaselevel}".format(
        sys.version_info
    )
    info["rpu"] = "v{0.major}.{0.minor}.{0.micro}-{0.releaselevel}".format(
        rpu.version_info
    )
    info["OS"] = platform.platform()

    nl = "\n"
    print(nl.join([f"{item}: {info[item]}" for item in info]))


@client.command(
    name="remove-dependency",
    brief="removes the need to have rpu as a dependency",
)
def remove_dependency(folder: str, mode: str = "file"):
    """removes rpu has a dependency in your python package

    folder: the folder to be used
    mode: the mode to be used.

    Modes:
        file - every part of rpu you use gets put into a single file
        clone - rpu gets cloned into your package, though that allows users to do `your_package.rpu.something`
    """

    if not os.path.exists(folder):
        return print(f"Folder {folder} not found")

    if mode == "clone":
        before = rpu.__file__.removesuffix("\\__init__.py").replace("\\", "/")
        after = f"{folder}/rpu"
        shutil.copytree(before, after)
        print("Successfully cloned RPU")

    elif mode == "file":
        files = [file for file in os.listdir(f"{folder}") if str(file).endswith(".py")]
        for file in files:
            with open(f"{folder}/{file}", "r") as f:
                contents = f.read()

            import ast

            tree = ast.parse(contents)
            found = []

            for item in tree.body:
                if isinstance(item, ast.ImportFrom):
                    if str(item.module).startswith("rpu"):
                        found.extend([alias.name for alias in item.names])
                elif isinstance(item, ast.Expr):
                    if isinstance(item.value, ast.Call):
                        if isinstance(item.value.func, ast.Attribute):
                            if isinstance(item.value.func.value, ast.Name):
                                if item.value.func.value.id:
                                    found.append(item.value.func.attr)
                            elif isinstance(item.value.func.value, ast.Attribute):
                                if isinstance(item.value.func.value.value, ast.Name):
                                    if item.value.func.value.value.id == "rpu":
                                        found.append(item.value.func.attr)

                    elif isinstance(item.value, ast.Attribute):
                        if isinstance(item.value.value, ast.Name):
                            if item.value.value.id == "rpu":
                                found.append(item.value.attr)
                        elif isinstance(item.value.value, ast.Attribute):
                            if isinstance(item.value.value.value, ast.Name):
                                if item.value.value.value.id == "rpu":
                                    found.append(item.value.attr)

            if not found:
                return print(f"{file} does not use rpu")
            print(f'Found: {", ".join(found)}')

            final = []

            for item in found:
                try:
                    source_lines, _ = inspect.getsourcelines(getattr(rpu, item))
                    final.append("".join(source_lines))
                except Exception as e:
                    print(f"Could not find source code for {item}")
                    raise e

            with open(f"{folder}/rpu.py", "w") as f:
                f.write("\n\n".join(final))
            print("Done")

    else:
        return print("Invalid Mode. Valid Modes: file, clone")


client.run()
