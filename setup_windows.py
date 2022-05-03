import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["os"],
    "excludes": [
        "asyncio", "concurrent", "ctypes", "distutils", "email", "html", "http",
        "lib2to3", "logging", "multiprocessing", "pydoc_data", "test", "unittest", "urllib", "xml",
        "xmlrpc", "tkinter"],
    "includes": ["argparse", "random"],
    "include_files": ["README.md", "talks.txt", "LICENSE", "get_random_talk_out_of_all.bat",
                      "get_random_talk_weighted_to_most_recent.bat"],
}

base = None

setup(
    name="ConferenceTalkRandomizer",
    version="0.1",
    description="Listen to a random conference talk.",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base, target_name="ConferenceTalkRandomizer")],
)